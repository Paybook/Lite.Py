# -​*- coding: utf-8 -*​-import os
from cloud.dependencies import paybook as _Paybook
from cloud.dependencies import db as _DB
from cloud.dependencies import constants as _Constants
from json import dumps
from flask import render_template, redirect, url_for

def catalogs(session):
	if 'username' in session:
		return _Paybook.catalogs(session)
	else:
		return redirect(url_for('login'))

def credentials(session, request):
	if 'username' in session:
		if request.method == 'POST':			
			institution = request.values['name']
			data_to_send = {}
			data_to_send['token'] = session['token']
			data_to_send['name'] = "donmikeazul@hotmail.com"
			for item in session['catalog']:
				if institution == item['name']:					
					data_to_send['id_site'] = item['id_site']
					data_to_send['credentials'] = {}
					for index in item['credentials']:
						credential = item['credentials'][index]
						credential_name = credential['name']
						data_to_send['credentials'][credential_name] = request.values[credential_name]
					break
			return _Paybook.credentials(session, data_to_send, institution)				
			

def sync_account(session, request):
	if 'username' in session:
		if request.method == 'POST':
			token = request.values['token']
			institution = request.values['name']
			data = {}
			data['twofa'] = {}
			data['twofa']['token'] = token
			data['token'] = session['token']
			for item in session['catalog']:
				if institution == item['name']:
					data['id_site'] = item['id_site']					
					break
			response = _DB.get_response(session['id_user_db'], institution)
			response['institution'] = institution
			regrex = _Paybook.sync_account(response, data)
			#f = open('response.json', 'w')
			#f.write(dumps(regret, sort_keys=True, indent=4, separators=(',', ': ')))
			return regrex

def widget(session, request):
	if 'username' in session:
		data = {}
		data['token'] = session['token']
		return render_template('widget.html', data = dumps(data))
		
	else:
		return redirect(url_for('login'))

def get_accounts(session, id_site):
	if 'username' in session:
		data_to_send = {}
		data_to_send['token'] = session['token']
		data_to_send['id_site'] = id_site
		return _Paybook.get_accounts(data_to_send)
	else: 
		return redirect(url_for('login'))

def get_transactions(session, id_account):
	if 'username' in session:
		data_to_send = {}
		data_to_send['token'] = session['token']
		data_to_send['id_account'] = id_account		
		return _Paybook.get_transactions(data_to_send)
	else: 
		return redirect(url_for('login'))