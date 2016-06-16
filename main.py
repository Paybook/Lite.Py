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
from flask import Flask, Response, url_for, redirect
from flask import request
from flask_cors import CORS, cross_origin
import logging
import getopt

# Paybook SDK:
from paybook.sdk import Error as _Paybook_Error
from paybook.sdk import Paybook as _Paybook
import utilities as _Utilities

argv = sys.argv[1:]
PAYBOOK_API_KEY = None
a_param = None
try:
	opts, args = getopt.getopt(argv,"a",["apikey="])
except Exception as e:
	print 'Error getting params ... '
	print e
	sys.exit()
for opt, arg in opts:
	if opt in ("-a", "--apikey"):
		if len(args):
			PAYBOOK_API_KEY = args[0]
		a_param = True
if PAYBOOK_API_KEY is None or a_param is None:
	print '--a param is required'
	sys.exit()

print '\nSetting API Key to: ' + str(PAYBOOK_API_KEY)
print 'Server started successfully\n'
print 'Enjoy your Paybook SYNC experience \\0/\n\n'
# ------ END of Config script

# App:
app = Flask(__name__,static_folder='public')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = os.urandom(24)
logger = _Utilities.setup_logger('app')
paybook = _Paybook(PAYBOOK_API_KEY,db_environment=True,logger=logger)

@app.route('/', methods=['GET'])
def index():
	return redirect(url_for('static', filename='index.html'))

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
		if id_site == 'null':
			id_site = None
		logger.debug('Executing ... ')
		site_accounts = paybook.accounts(token,id_site=id_site)
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
		id_site = request.args.get('id_site')
		id_account = request.args.get('id_account')
		if id_site == 'null':
			id_site = None
		if id_account == 'null':
			id_account = None
		logger.debug('Executing ... ')
		account_transactions = paybook.transactions(token,id_account=id_account,id_site=id_site)
		logger.debug('Transactions: ' + str(len(account_transactions)))
		logger.debug('Sending response ... ')
		transactions_response = _Utilities.Success({'transactions':account_transactions}).get_response()
	except _Paybook_Error as e:
		transactions_response = e.get_response()
	except Exception as e:
		transactions_response = _Utilities.internal_server_error(e)
	return transactions_response












if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0")
