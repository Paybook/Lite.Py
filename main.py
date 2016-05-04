# -​*- coding: utf-8 -*​-
import os
from json import dumps
from flask import Flask
from flask import render_template, url_for , request, redirect, session, escape
from cloud.app import session as _Session
from cloud.app import sync as _Sync

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
	return _Session.index(session)	

@app.route("/login", methods=['GET', 'POST'])
def login():
	return _Session.login(session,request)	

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	return _Session.signup(session, request)	

@app.route("/catalogs")
def catalogs():
	return _Sync.catalogs(session)

@app.route("/credentials", methods=['GET', 'POST'])
def credentials():
	return _Sync.credentials(session, request)	

@app.route("/sync_account", methods=['GET', 'POST'])
def sync_account():
	return _Sync.sync_account(session, request)	

@app.route("/accounts/<credential_id>", methods=['GET', 'POST'])
def show_accounts(credential_id):
	return _Sync.get_accounts(session, credential_id)

@app.route("/account/<id_account>", methods=['GET', 'POST'])
def show_transactions(id_account):
	return _Sync.get_transactions(session, id_account)

@app.route("/widget")
def widget():
	return _Sync.widget(session, request)

@app.route("/logout")
def logout():
	return _Session.logout(session)	

if __name__ == "__main__":
	app.debug = False
	app.run()	
	url_for('static', filename='bootstrap.css')
	url_for('static', filename='bootstrap.min.css')
	url_for('static', filename='bootstrap.min.js')
	url_for('static', filename='bootstrap.js')
	url_for('static', filename='jquery.js')