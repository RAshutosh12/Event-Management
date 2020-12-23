from flask import Flask, render_template, request, url_for, redirect
from supportClass import eventFormEntries
from mongoDBSetup import mongodbConnectionCheck

app = Flask(__name__)

#MongoDB setup
eventCollection = mongodbConnectionCheck()

#Rounting of Web Application!!!!!!
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('creation'))
    return render_template('homePage.html')

@app.route('/eventCreation',methods=['GET','POST'])
def creation():
    
    print("GET Method Run") 
    if request.method == 'POST':

        #Save POST data in respective variables
        eN = request.form.get('event_name')
        tS = request.form.get('team_size')
        pS = request.form.get('partners_name')
        eDt = request.form.get('event_date')
        eT =request.form.get('event_type')
        eD = request.form.get('event_desc')
        eO = request.form.get('event_owner')

        totalEvents = eventCollection.estimated_document_count()
        eID = "EventID-"+ str(totalEvents + 1)

        #print(eID)
        #Create object of formEntry inputs
        dataObj = eventFormEntries(eID , eN , pS , eDt , eT , tS , eO , eD)
        # print(dataObj.eventDate , dataObj.eventType)
        
        dataObj.mergeUserInputTemplate(eventCollection)

    return render_template('eventCreationForm.html')


if __name__ == '__main__':
    app.run(debug=True)