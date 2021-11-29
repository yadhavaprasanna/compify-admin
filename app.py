
from flask import Flask,render_template,request

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db=firestore.client()

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def homepage():
    return render_template("homepage.html")
@app.route("/task",methods=['GET','POST'])
def task():
    if request.method== 'POST':
        canNotify=bool(request.form['canNotify'])
        createdOn=request.form['createdOn']
        description=request.form['description']
        displayPicUrl=request.form['displayPicUrl']
        isActive=bool(request.form['isActive'])
        maxRc=int(request.form['maxRc'])
        
        minRc=int(request.form['minRc'])
        name=request.form['name']
        time=int(request.form['time'])
       
        taskdata={
            'canNotify':canNotify,
            'createdOn':createdOn,
            'description':description,
            'displayPicUrl':displayPicUrl,
            'isActive':isActive,
            'maxRc':maxRc,
            'minRc':minRc,
            'name':name,
            'time':time
        }
        db.collection('tasks').add(taskdata)
        
        return "success ";
    return render_template('task.html')
   
@app.route("/shop",methods=['GET','POST'])
def shop():
    if request.method== 'POST':
        description=request.form['description']
        destroy=bool(request.form['destroy'])
        
        displayPicUrl=request.form['displayPicUrl']
        expiryDate=request.form['expiryDate']
        isActive=bool(request.form['isActive'])
        latLong=request.form['latLong']
        name=request.form['name']
        qrId=request.form['qrId']
        redeemAmount=int(request.form['redeemAmount'])
        redeemedBy=request.form['redeemedBy']
        
    

    

        shopdata={
            'description':description,
            'destroy':destroy,
           
            'displayPicUrl':displayPicUrl,
            'expiryDate':expiryDate,
            'isActive':isActive,
            'latLong':latLong,
            'name':name,
            'qrId':qrId,
            'redeemAmount':redeemAmount,
            'redeemedBy':redeemedBy
        }
        db.collection('shops').add(shopdata)
        
        return "success ";
    return render_template('shop.html')




@app.route("/faq",methods=['GET','POST'])
def faq():
    if request.method== 'POST':
        answer=request.form['answer']
        order=int(request.form['order'])
        question=request.form['question']
        url=request.form['url']
        
    

    

        faqdata={
            'answer':answer,
            'order':order,
           
            'question':question,
            'url':url,
            
        }
        db.collection('faq').add(faqdata)
        
        return "success ";
    return render_template('faq.html')  





    

@app.route("/user",methods=['GET','POST'])
def user():
    return render_template("user.html")
@app.route("/feedback",methods=['GET','POST'])
def feedback():
    return render_template("feedback.html")




if __name__=='__main__':
    app.run(debug=True)