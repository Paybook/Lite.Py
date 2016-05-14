# -​*- coding: utf-8 -*​-

# ██╗     ██╗████████╗███████╗    ███████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗
# ██║     ██║╚══██╔══╝██╔════╝    ██╔════╝╚██╗██╔╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝
# ██║     ██║   ██║   █████╗      █████╗   ╚███╔╝ ███████║██╔████╔██║██████╔╝██║     █████╗  
# ██║     ██║   ██║   ██╔══╝      ██╔══╝   ██╔██╗ ██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  
# ███████╗██║   ██║   ███████╗    ███████╗██╔╝ ██╗██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗
# ╚══════╝╚═╝   ╚═╝   ╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝
                                                                                           
# External:
import os
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
import constants as _Constants
import utilities as _Utilities

PAYBOOK_API_KEY = "YOUR_API_KEY"

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = os.urandom(24)
logger = _Utilities.setup_logger('app')
paybook = _Paybook(PAYBOOK_API_KEY,db_environment=True,logger=logger)

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
		logger.debug(token)
		logger.debug('Executing ... ')
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
		accounts_response = _Utilities.Success({'accounts':site_accounts}).get_response()
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
		params = json.loads(request.data)
		logger.debug(params)
		token = params['token']
		id_account = params['id_account']
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
	






