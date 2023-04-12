from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from Algorithm.MainRunner import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coughData.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class cough(db.Model):
    id = db.Column(db.Integer, primary_key=True) # specific id of each instance
    coughCount = db.Column(db.Integer) # holds the number of coughs
    dateCreated = db.Column(db.DateTime, default=datetime.now) # when the cough data is downloaded 
    dataName = db.Column(db.String(200)) 
        # default name of cough data instance

    def __repr__(self):
       return '<Data %r>' % self.id




@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':

        # Send files to main and recieve cough count
        audioData = request.files['audioData']
        accData = request.files['accData']
        coughValue, flagValue, coughTimeStamps, flagTimeStamps = main(audioData, accData)
        timezone = pytz.timezone('US/Mountain') 
        dataName = "Cough Count on " + datetime.now(timezone).strftime("%I:%M%p")

        new_cough = cough(coughCount = coughValue, dataName = dataName)

        db.session.add(new_cough)
        db.session.commit()

        return render_template('home.html', coughValue=coughValue, flagValue=flagValue, coughTimeStamps=coughTimeStamps, flagTimeStamps=flagTimeStamps)

    else:
        return render_template('home.html')
        

@app.route('/history', methods=['GET'])  # GETTING OPERATIONAL ERRORS. WIP
def history():
    coughData = cough.query.order_by(cough.dateCreated).all() # Looks at database in order created and grab all
    return render_template('history.html', coughData=coughData)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = cough.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/history')
    except:
        return 'There was a problem deleting that task'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True) 