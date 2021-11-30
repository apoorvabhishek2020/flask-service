from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb://admin:password@mongodb/user-account?authSource=admin")
db = mongodb_client.db

@app.route("/add_one", methods=['POST'])
def add_one(): 
    name=request.form['name']   
    age=request.form['age']
    db.users.insert_one({'name': name, 'age': age})
    return redirect("/")    

@app.route("/")
def home():    
    return render_template('home.html')

@app.route("/users")
def user():
    users = db.users.find()
    userList=[]
    for user in users:
        userList.append(user)
    return render_template('user.html', users=userList)

if(__name__=="__main__"):
    app.run(host='0.0.0.0',port=5005,debug=True)
