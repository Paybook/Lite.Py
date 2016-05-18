# -​*- coding: utf-8 -*​-

# ██╗     ██╗████████╗███████╗    ███████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗
# ██║     ██║╚══██╔══╝██╔════╝    ██╔════╝╚██╗██╔╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝
# ██║     ██║   ██║   █████╗      █████╗   ╚███╔╝ ███████║██╔████╔██║██████╔╝██║     █████╗  
# ██║     ██║   ██║   ██╔══╝      ██╔══╝   ██╔██╗ ██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  
# ███████╗██║   ██║   ███████╗    ███████╗██╔╝ ██╗██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗
# ╚══════╝╚═╝   ╚═╝   ╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝
      
# External:
import os
import sys
from json import dumps
import json
from flask import Flask
from flask import request
from flask.ext.cors import CORS, cross_origin
import logging

# Paybook SDK:
from paybook.sdk import Error as _Paybook_Error
from paybook.sdk import Paybook as _Paybook

# Local:
import utilities as _Utilities

# ------ BEGIN of Config script:
PAYBOOK_API_KEY = None
DEFUALT_VALUE = 'YOUR_API_KEY_GOES_HERE'
try:
	with open('config.json') as data_file:   
		print 'Reading config file ... ' 
		default_config = json.load(data_file)
except:
	default_config = {
		"paybook_api_key" : DEFUALT_VALUE
	}#End of default_config
	print 'Creating your config.json file ... '
	with open('config.json', 'w') as configfile:
		json.dump(default_config,configfile)
	print 'Remember to set your Paybook API Key at config.json file my friend'
	sys.exit()
try:
	PAYBOOK_API_KEY = default_config['paybook_api_key']
	if PAYBOOK_API_KEY == DEFUALT_VALUE:
		print 'Remember to set your Paybook API Key at config.json file my friend'
		sys.exit()
	else:
		print 'Setting Paybook API Key: ' + PAYBOOK_API_KEY
except:
	print 'Invalid config file'
	sys.exit()
print 'Server started successfully\n'
print 'Enjoy your Paybook SYNC experience \\0/\n\n'
# ------ END of Config script

# App:
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = os.urandom(24)
logger = _Utilities.setup_logger('app')
paybook = _Paybook(PAYBOOK_API_KEY,db_environment=True,logger=logger)

@app.route("/sessions")
def sessions():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/sessions')
		token = request.args.get('token')
		logger.debug(token)
		logger.debug('Executing ... ')
		session_response = paybook.validate_session(token)
		logger.debug('Sending response ... ')
		session_response = _Utilities.Success(session_response).get_response()
	except _Paybook_Error as e:# Just an example of how to catch a Paybook API error using SDK
		session_response = e.get_response()
	except Exception as e:
		session_response = _Utilities.internal_server_error(e)
	return session_response

@app.route("/signup", methods=['POST'])
def signup():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/signup')
		params = json.loads(request.data)
		logger.debug(params)
		username = params['username']
		password = params['password']
		logger.debug('Executing ... ')
		signup_response = paybook.signup(username,password)
		logger.debug('Sending response ... ')
		signup_response = _Utilities.Success(signup_response).get_response()
	except _Paybook_Error as e:# Just an example of how to catch a Paybook API error using SDK
		signup_response = e.get_response()
	except Exception as e:
		signup_response = _Utilities.internal_server_error(e)
	return signup_response

@app.route("/login", methods=['POST'])
def login():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/login')
		params = json.loads(request.data)
		logger.debug(params)
		username = params['username']
		password = params['password']
		logger.debug('Executing ... ')
		login_response = paybook.login(username,password)
		logger.debug('Sending response ... ')
		login_response = _Utilities.Success(login_response).get_response()
	except _Paybook_Error as e:
		login_response = e.get_response()
	except Exception as e:
		login_response = _Utilities.internal_server_error(e)
	return login_response

@app.route("/catalogues")
def catalogues():
	try:
		logger = logging.getLogger('app')
		token = request.args.get('token')
		is_true = request.args.get('is_true')
		logger.debug(token)
		logger.debug('Executing ... ')
		catalogs_response=None
		if is_true:
			catalogs_response = paybook.catalogues(token,is_true=True)
		else:
			catalogs_response = paybook.catalogues(token)
		logger.debug('Sending response ... ')
		catalogs_response = _Utilities.Success(catalogs_response).get_response()
	except _Paybook_Error as e:
		catalogs_response = e.get_response()
	except Exception as e:
		catalogs_response = _Utilities.internal_server_error(e)
	return catalogs_response

@app.route("/credentials", methods=['POST'])
def credentials():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/credentials')
		params = json.loads(request.data)
		logger.debug(params)
		token = params['token']
		id_site = params['id_site']
		db_credentials = params['credentials']
		logger.debug('Executing ... ')
		credentials_response = paybook.credentials(token,id_site,db_credentials)
		logger.debug('Sending response ... ')
		credentials_response = _Utilities.Success(credentials_response).get_response()
	except _Paybook_Error as e:
		credentials_response = e.get_response()
	except Exception as e:
		credentials_response = _Utilities.internal_server_error(e)
	return credentials_response

@app.route("/credentials")
def get_credentials():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/credentials')
		token = request.args.get('token')
		logger.debug(token)
		logger.debug('Executing ... ')
		credentials_response = paybook.get_credentials(token)
		logger.debug('Sending response ... ')
		credentials_response = _Utilities.Success(credentials_response).get_response()
	except _Paybook_Error as e:
		credentials_response = e.get_response()
	except Exception as e:
		credentials_response = _Utilities.internal_server_error(e)
	return credentials_response

@app.route("/credentials", methods=['DELETE'])
def delete_credentials():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/credentials')
		params = json.loads(request.data)
		logger.debug(params)
		token = params['token']
		id_credential = params['id_credential']
		logger.debug('Executing ... ')
		delete_response = paybook.delete_credentials(token,id_credential)
		logger.debug('Sending response ... ')
		delete_response = _Utilities.Success(delete_response).get_response()
	except _Paybook_Error as e:
		delete_response = e.get_response()
	except Exception as e:
		delete_response = _Utilities.internal_server_error(e)
	return delete_response

@app.route("/status")
def status():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/status')
		token = request.args.get('token')
		id_site = request.args.get('id_site')
		logger.debug(token)
		logger.debug(id_site)
		logger.debug('Executing ... ')
		status_response = paybook.status(token,id_site)
		logger.debug('Sending response ... ')
		status_response = _Utilities.Success(status_response).get_response()
	except _Paybook_Error as e:
		status_response = e.get_response()
	except Exception as e:
		status_response = _Utilities.internal_server_error(e)
	return status_response

@app.route("/twofa", methods=['POST'])
def twofa():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/twofa')
		params = json.loads(request.data)
		logger.debug(params)
		token = params['token']
		id_site = params['id_site']
		fatwo = params['twofa']
		logger.debug('Executing ... ')
		twofa_response = paybook.twofa(token,id_site,fatwo)
		logger.debug('Sending response ... ')
		twofa_response = _Utilities.Success(twofa_response).get_response()
	except _Paybook_Error as e:
		twofa_response = e.get_response()
	except Exception as e:
		twofa_response = _Utilities.internal_server_error(e)
	return twofa_response

@app.route("/accounts")
def accounts():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/accounts')
		token = request.args.get('token')
		id_site = request.args.get('id_site')
		logger.debug(token)
		logger.debug(id_site)
		logger.debug('Executing ... ')
		site_accounts = paybook.accounts(token,id_site)
		logger.debug('Sending response ... ')
		accounts_response = _Utilities.Success(site_accounts).get_response()
	except _Paybook_Error as e:
		accounts_response = e.get_response()
	except Exception as e:
		accounts_response = _Utilities.internal_server_error(e)
	return accounts_response

@app.route("/transactions")
def transactions():
	try:
		logger = logging.getLogger('app')
		logger.debug('\n/transactions')
		token = request.args.get('token')
		id_account = request.args.get('id_account')
		logger.debug(token)
		logger.debug(id_account)
		logger.debug('Executing ... ')
		account_transactions = paybook.transactions(token,id_account)
		logger.debug('Sending response ... ')
		transactions_response = _Utilities.Success({'transactions':account_transactions}).get_response()
	except _Paybook_Error as e:
		transactions_response = e.get_response()
	except Exception as e:
		transactions_response = _Utilities.internal_server_error(e)
	return transactions_response

if __name__ == "__main__":
	app.debug = True
	app.run()


