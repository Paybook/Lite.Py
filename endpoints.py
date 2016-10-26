# -​*- coding: utf-8 -*​-

import logging, json
from flask import request, redirect, url_for
import utilities as _Utilities
import db as _DB
import paybook.sdk as paybook_sdk

def index():
	return redirect(url_for('static', filename='index.html'))

def signup():
	try:
		# Log call and get params:
		logger = logging.getLogger('app')
		logger.debug('\n/signup')
		params = json.loads(request.data)
		logger.debug(params)
		username = params['username']
		password = params['password']
		logger.debug('Executing ... ')
		# Data base and paybook logic:
		signup_response = {
			'sdk_message' : 'User already exists'
		}#End of signup_response
		db_user = _DB.User(username,password)# This is the app user (stored in app's data base)
		user_exist = db_user.do_i_exist()
		logger.debug('User exist: ' + str(user_exist))
		if not user_exist:
			logger.debug('Singning up user ... ')
			pb_user = paybook_sdk.User(name=username)# This is the paybook user (stored in paybook's data base)
			signup_response = pb_user.get_json()
			db_user.set_id_user(signup_response['id_user'])
			db_user.save()
			signup_response['sdk_message'] = 'User signed up'
		logger.debug('Sending response ... ')
		signup_response = _Utilities.Success(signup_response).get_response()
	except paybook_sdk.Error as error:
		signup_response = error.get_json()
	return signup_response

def login():
	try:
		# Log call and get params:
		logger = logging.getLogger('app')
		logger.debug('\n/login')
		params = json.loads(request.data)
		logger.debug(params)
		username = params['username']
		password = params['password']
		logger.debug('Executing ... ')
		# Data base and paybook logic:
		db_user = _DB.User(username,password)
		logger.debug('DB authentication ... ')
		if db_user.login():
			id_user = db_user.get_id_user()
			logger.debug('Id user: ' + str(id_user))
			pb_user = paybook_sdk.User(id_user=id_user)
			session = paybook_sdk.Session(user=pb_user)
			login_response = _Utilities.Success(session.get_json()).get_response()
		else:
			login_response = _Utilities.Error('Invalid username or password',400).get_response()
	except paybook_sdk.Error as error:
		login_response = error.get_json()
	return login_response

def catalogues():
	try:
		# Log call and get params:
		logger = logging.getLogger('app')
		logger.debug('\n/catalogues')
		logger.debug(request.args)
		token = request.args.get('token')
		is_test = request.args.get('is_test')
		if is_test == 'true':
			is_test = True
		else:
			is_test = False
		logger.debug('Token: ' + token)
		logger.debug('Test: ' + str(is_test))
		logger.debug('Executing ... ')
		# Paybook logic:
		session = paybook_sdk.Session(token=token)
		sites = paybook_sdk.Catalogues.get_sites(session=session,is_test=is_test)
		catalogs_response = []
		for site in sites:
			catalogs_response.append(site.get_json())
		logger.debug('Catalogues: ' + str(len(catalogs_response)))
		logger.debug('Sending response ... ')
		catalogs_response = _Utilities.Success(catalogs_response).get_response()
	except paybook_sdk.Error as error:
		catalogs_response = _Utilities.Error(error.message,error.code).get_response()
	return catalogs_response

def credentials():
	try:
		# Log call and get params:
		logger = logging.getLogger('app')
		logger.debug('\n/credentials')
		params = json.loads(request.data)
		logger.debug(params)
		token = params['token']
		id_site = params['id_site'] if 'id_site' in params else None
		credentials = params['credentials']
		logger.debug('Executing ... ')
		# Paybook logic:
		session = paybook_sdk.Session(token=token)
		logger.debug('Creating credentials ... ')
		logger.debug(credentials)
		credentials = paybook_sdk.Credentials(session=session,id_site=id_site,credentials=credentials)
		logger.debug('Id credential: ' + credentials.id_credential)
		logger.debug('Twofa: ' + credentials.twofa)
		logger.debug("curl -X POST -d '{\"twofa_key\":\"token\",\"token\":\"4f3e7fe982f18898f970e4805b4774a3\",\"twofa\":\"" + credentials.twofa + "\",\"twofa_value\":\"test\",\"id_credential\":\"" + credentials.id_credential + "\"}' http://localhost:5000/twofa --header \"Content-Type:application/json\"")
		logger.debug('Sending response ... ')
		credentials_response = _Utilities.Success(credentials.get_json()).get_response()
	except paybook_sdk.Error as error:
		credentials_response = _Utilities.Error(error.message,error.code).get_response()
	return credentials_response

def get_credentials():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/credentials')
		token = request.args.get('token')
		logger.debug('Token: ' + token)
		logger.debug('Executing ... ')
		session = paybook_sdk.Session(token=token)
		credentials_list = paybook_sdk.Credentials.get(session=session)
		site_organizations = paybook_sdk.Catalogues.get_site_organizations(session=session)
		test_site_organizations = paybook_sdk.Catalogues.get_site_organizations(session=session,is_test=True)
		site_organizations = site_organizations + test_site_organizations
		data_by_id_site_organization = {}
		for site_organization in site_organizations:
			data_by_id_site_organization[site_organization.id_site_organization] = {
				'avatar' : site_organization.avatar,
				'name' : site_organization.name
			}#End of data_by_id_site_organization[site_organization.id_site_organization]
		credentials_response = []
		for credentials in credentials_list:
			credentials_json = credentials.get_json()
			credentials_json['avatar'] = data_by_id_site_organization[credentials_json['id_site_organization']]['avatar']
			credentials_json['name'] = data_by_id_site_organization[credentials_json['id_site_organization']]['name']
			credentials_response.append(credentials_json)
		logger.debug('Credentials: ' + str(len(credentials_response)))
		logger.debug('Sending response ... ')
		credentials_response = _Utilities.Success(credentials_response).get_response()
	except paybook_sdk.Error as error:
		credentials_response = _Utilities.Error(error.message,error.code).get_response()
	return credentials_response

def delete_credentials():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/credentials')
		params = json.loads(request.data)
		logger.debug(params)
		token = params['token']
		id_credential = params['id_credential']
		logger.debug('Executing ... ')
		session = paybook_sdk.Session(token=token)
		credentials_deleted = paybook_sdk.Credentials.delete(session=session,id_credential=id_credential)
		logger.debug('Sending response ... ')
		delete_response = _Utilities.Success(credentials_deleted).get_response()
	except paybook_sdk.Error as error:
		delete_response = _Utilities.Error(error.message,error.code).get_response()
	return delete_response

def accounts():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/accounts')
		token = request.args.get('token')
		id_site = request.args.get('id_site')
		logger.debug(token)
		logger.debug(id_site)
		if id_site == 'null':
			id_site = None
		options = {}
		if id_site is not None:
			logger.debug('Filtering by id_site ' + id_site + ' ... ')
			options['id_site'] = id_site
		logger.debug('Executing ... ')
		session = paybook_sdk.Session(token=token)
		accounts = paybook_sdk.Account.get(session=session,options=options)
		accounts_response = []
		for account in accounts:
			accounts_response.append(account.get_json())
		logger.info('Accounts: ' + str(len(accounts_response)))
		logger.debug('Sending response ... ')
		accounts_response = _Utilities.Success(accounts_response).get_response()
	except paybook_sdk.Error as error:
		accounts_response = _Utilities.Error(error.message,error.code).get_response()
	return accounts_response

def transactions():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/transactions')
		token = request.args.get('token')
		id_account = request.args.get('id_account')
		logger.debug(token)
		logger.debug(id_account)
		id_site = request.args.get('id_site')
		id_account = request.args.get('id_account')
		skip = request.args.get('skip')
		limit = request.args.get('limit')
		if id_site == 'null':
			id_site = None
		if id_account == 'null':
			id_account = None
		if skip == 'null':
			skip = None
		if limit == 'null':
			limit = None
		logger.debug('Executing ... ')
		session = paybook_sdk.Session(token=token)
		options = {}
		if id_site is not None:
			logger.debug('Filtering by id_site ' + id_site + ' ... ')
			options['id_site'] = id_site
		if id_account is not None:
			logger.debug('Filtering by id_account ' + id_account + ' ... ')
			options['id_account'] = id_account
		if skip is not None:
			logger.debug('Skiping ' + skip + ' ... ')
			options['skip'] = skip
		if limit is not None:
			logger.debug('Adding limit ' + limit + ' ... ')
			options['limit'] = limit
		transactions = paybook_sdk.Transaction.get(session=session,options=options)
		transactions_response = []
		for transaction in transactions:
			transactions_response.append(transaction.get_json())
		logger.debug('Transactions: ' + str(len(transactions_response)))
		logger.debug('Sending response ... ')
		transactions_response = _Utilities.Success({'transactions':transactions_response}).get_response()
	except paybook_sdk.Error as error:
		transactions_response = _Utilities.Error(error.message,error.code).get_response()
	return transactions_response

def twofa():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/twofa')
		params = json.loads(request.data)
		logger.debug(params)
		token = params['token']
		id_credential = params['id_credential']
		credentials_twofa = params['twofa']
		twofa_key = params['twofa_key']
		twofa_value = params['twofa_value']
		logger.debug('Executing ... ')
		session = paybook_sdk.Session(token=token)
		credentials = None
		credentials_list = paybook_sdk.Credentials.get(session=session)
		for c in credentials_list:
			if c.id_credential == id_credential:
				credentials = c
		credentials.twofa = credentials_twofa
		credentials.twofa_config = {
			'name' : twofa_key
		}#End of twofa_config
		twofa_set = credentials.set_twofa(session=session,twofa_value=twofa_value)
		logger.debug('Towfa value set: ' + str(twofa_set))		
		logger.debug('Sending response ... ')
		twofa_response = _Utilities.Success(twofa_set).get_response()
	except paybook_sdk.Error as error:
		twofa_response = _Utilities.Error(error.message,error.code).get_response()
	return twofa_response


