from app import app
from flask import render_template,redirect, request, flash,g,session,url_for
from models import *

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET","POST"])
def signup():
    return render_template("signup.html")

@app.route("/signedup", methods=["GET","POST"])
def signedup():
    
    username = request.form['username']
    password = request.form['password']
    homefolder = request.form['homefolder']
    grantsudo = request.form['grantsudo']
    shelltype = request.form['shelltype']
    

    if not session.get("logged_in"):
        insert_account_holder(username,password,homefolder,grantsudo,shelltype)
    return render_template("homepage.html",username=username)
