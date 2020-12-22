from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('creation'))
    return render_template('homePage.html')

@app.route('/eventCreation',methods=['GET','POST'])
def creation():
    
    print("GET Method Run") 
    if request.method == 'POST':

        #Save posted info in variables
        eN = request.form.get('event_name')
        eno = request.form.get('team_size')
        pS = request.form.get('partners_name')
        eD = request.form.get('event_date')
        eT =request.form.get('event_type')
        eD = request.form.get('event_desc')
        eO = request.form.get('event_owner')

        # #Create object of userEntry inputs
        # data = userEntry(jP,pN,op,pG,pT,uId,pD,os,dF,dTA)

        # #Search in database if project already added
        # if myCol.find_one({'_id': data.projectName}) == None:

        #     #Merge with template
        #     doc=mergeUserInputTemplate(data)
        #     logger.info("--Project Data merged and redirecting for review--")
        #     return redirect(url_for('reviewEntryPage',doc=doc))

        # else:
        #     logger.warning("--Project already present in databse--")
        #     return render_template('error.html')

    return render_template('eventCreationForm.html')


if __name__ == '__main__':
    app.run(debug=True)