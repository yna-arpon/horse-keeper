from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from Algorithm.MainRunner import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coughData.db'
db = SQLAlchemy(app)

class cough(db.Model):
    id = db.Column(db.Integer, primary_key=True) # specific id of each instance
    coughCount = db.Column(db.Integer) # holds the number of coughs
    dateCreated = db.Column(db.DateTime, default=datetime.date) # when the cough data is downloaded 
    dataName = db.Column(db.String(100), default='Cough Count on ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S")) 
        # default name of cough data instance - user can change



@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        # Send files to main and recieve cough count
        audioData = request.files['audioData']
        accData = request.files['accData']
        coughValue = main(audioData, accData) # using trial.py right now as a dummy function in place of mainRunner

        # Display cough count results
        return render_template('home.html', coughValue=coughValue)
    else:
        return render_template('home.html')
        

@app.route('/history')  # GETTING OPERATIONAL ERRORS. WIP
def history():
    if request.method == 'POST':
        cough_content = request.form['content'] # get our input (testing. final should be from homepage)
        new_file = cough(content=cough_content)
        try:
            db.session.add(new_file)
            db.session.commit()
            return redirect('/history')
        except:
            return 'There was an issue adding your file'
        
    else:
        files = cough.query.order_by(cough.dateCreated).all() # ordering by date created. can use first, etc. use for sort function
        return render_template('history.html', files=files)
    render_template('history.html')
    

@app.route('/delete/<int:id>')
def delete(id):
    data_to_delete = "pass"

    try:
        db.session.delete(data_to_delete)
        db.session.commit()
        return redirect('/history')
    except:
        return 'There was a problem deleting the file'

if __name__ == "__main__":
    app.run(debug=True) 