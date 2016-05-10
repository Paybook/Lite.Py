# -​*- coding: utf-8 -*​-
import requests
from cloud.dependencies import db as _DB
from cloud.dependencies import constants as _Constants
from json import dumps
from flask import render_template, redirect, url_for

def catalogs(session):
	conn = requests.get(_Constants.PAYBOOK_LINK + 'catalogues/sites', params = {"token": session['token']})
	session['catalog'] = conn.json()['response']
	accounts_registred = {}	
	query = _DB.get_accounts(session['id_user'])
	if query is not None:
		for item in query:
			accounts_registred[item['name']] = item['id_site']
	return render_template('catalogs.html', dicc = conn.json()['response'], accounts = accounts_registred)	

def credentials(session, data, institution):
	conn = requests.post(_Constants.PAYBOOK_LINK + 'credentials', data = dumps(data))
	if conn.status_code == 200:
		data['ownerId'] = session['id_user']
		data['name'] = institution
		data['data'] = conn.json()['response']
		data.pop('token',None)
		if _DB.credential_exists(data['ownerId'], data['name']):
			_DB.modify_credentials_in_db(data)			
		else:
			_DB.create_credentials(data)						
		return dumps(conn.json())

def sync_account(response, data):
	headers = {'Content-type' : 'application/json'}		
	token_json_form = {}
	token_json_form['token'] = data['token']
	conn = requests.post(response['twofa'],headers=headers, data = dumps(data))
	status = requests.get(response['status'], params = token_json_form)		
	return dumps(status.json())

def login(session, email, api_key, id_user):
	conn = requests.post(_Constants.PAYBOOK_LINK + 'sessions', data = {"api_key": api_key, "id_user": id_user})
	if conn.status_code == 200:
		session['id_user'] = id_user
		session['username'] = email
		session['token'] = conn.json()['response']['token']		
		return redirect(url_for('catalogs'))
	else:
		return render_template('login.html', err = "Usuario o contraseña incorrectos".decode('utf-8'))

def signup(email):
	conn = requests.post(_Constants.PAYBOOK_LINK + 'users', data = {"api_key":_Constants.API_KEY, "name":email})
	return conn

def get_accounts(data):
	accounts = accounts = requests.get(_Constants.PAYBOOK_LINK + 'accounts', params = data)	
	if accounts.status_code == 200:
		return render_template('accounts.html', data = accounts.json()['response'])
	else:
		return dumps({'Status':'Unsuccess'})

def get_transactions(data):
	transactions = requests.get(_Constants.PAYBOOK_LINK + 'transactions', params = data)
	if transactions.status_code == 200:
		return render_template('transactions.html', data = transactions.json()['response'])
	else:
		return dumps({'Status':'Unsuccess'})	
