# -​*- coding: utf-8 -*​-import os
from cloud.dependencies import db as _DB
from cloud.dependencies import constants as _Constants
from cloud.dependencies import paybook  as _Paybook
import datetime
import requests
from flask import render_template, redirect, url_for


def index(session):
	if 'username' in session:
		return render_template('index.html', session = session['username'])		
	return render_template('index.html', session = None)

def login(session, request):
	if 'username' not in session:
		if request.method == 'POST':
			api_key = _Constants.API_KEY
			email = request.values['email']
			id_user = _DB.get_id_user(email)
			psw = request.values['password']
			if _DB.log_in(session,email,psw):
				return _Paybook.login(session, email, api_key, id_user)
			else:
				return render_template('login.html', err = "Usuario o contraseña incorrectos".decode('utf-8'))
		else:
			return render_template('login.html', err = None)
	else:
		return redirect(url_for('index'))

def signup(session, request):
	if 'username' not in session:
		if request.method == 'POST':		
			email = request.values['email']
			psw = request.values['password']
			user = {}
			user['user'] =  email
			user['password'] = psw
			user['date'] =  datetime.datetime.utcnow()			
			if _DB.search_user_in_db(email):
				return render_template('signup.html', err = "Usuario en uso")
			else:
				conn = _Paybook.signup(email)
				if conn.status_code == 200:
					user['id_user'] = conn.json()['response']['id_user']
					session['id_user'] = conn.json()['response']['id_user']
					_DB.create_user(user)
					_DB.search_users()
					return redirect(url_for('login'))
				else:
					return render_template('signup.html', err = "Usuario no pudo ser creado")
		else:
			return render_template('signup.html', err = None)
	else:
		return redirect(url_for('index'))

def logout(session):
	if 'username' in session:		
		session.pop('username', None)
		session.pop('token', None)
		session.pop('id_user', None)
		session.pop('catalog', None)
		return redirect(url_for('login'))
	return redirect(url_for('index'))