from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from algorithm.MainRunner import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coughData.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class cough(db.Model):
    id = db.Column(db.Integer, primary_key=True) # specific id of each instance
    coughCount = db.Column(db.Integer) # holds the number of coughs
    dateCreated = db.Column(db.DateTime, default=datetime.now) # when the cough data is downloaded 
    dataName = db.Column(db.String(100), default='Cough Count on ' + datetime.now().strftime(" %H:%M:%S")) 
        # default name of cough data instance - user can change

    def __repr__(self):
       return '<Data %r>' % self.id




@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':

        # Send files to main and recieve cough count
        audioData = request.files['audioData']
        accData = request.files['accData']
        coughValue, flagValue = main(audioData, accData) 

        new_cough = cough(coughCount = coughValue)

        db.session.add(new_cough)
        db.session.commit()

        return render_template('home.html', coughValue=coughValue, flagValue=flagValue)

    else:
        return render_template('home.html')
        

@app.route('/history', methods=['GET'])  # GETTING OPERATIONAL ERRORS. WIP
def history():
    coughData = cough.query.order_by(cough.dateCreated).all() # Looks at database in order created and grab all
    return render_template('history.html', coughData=coughData)
    

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True) 