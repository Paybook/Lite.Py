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
from flask import Flask, Response
from flask import request
from flask_cors import CORS, cross_origin
import logging
import utilities as _Utilities
import endpoints
import paybook
import paybook.sdk as paybook_sdk

cmd_params = _Utilities.get_cmd_params(sys.argv[1:])
paybook_api_key = cmd_params['api_key']
# database_path = cmd_params['database']

paybook_sdk.Paybook(paybook_api_key)
print '\nSetting API Key to: ' + str(paybook_api_key)
print 'Server started successfully\n'
print 'Enjoy your Paybook SYNC experience V_0.1 \\0/\n\n'

# App:
app = Flask(__name__,static_folder='public')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = os.urandom(24)
logger = _Utilities.setup_logger('app')

@app.route('/', methods=['GET'])
def index():
	print 'endpoints.index'
	return endpoints.index()

@app.route("/signup", methods=['POST'])
def signup():
	print 'endpoints.signup'
	return endpoints.signup()

@app.route("/login", methods=['POST'])
def login():
	print 'endpoints.login'
	return endpoints.login()

@app.route("/catalogues")
def catalogues():
	print 'endpoints.catalogues'
	return endpoints.catalogues()

@app.route("/credentials", methods=['POST'])
def credentials():
	print 'endpoints.credentials'
	return endpoints.credentials()

@app.route("/credentials")
def get_credentials():
	print 'endpoints.get_credentials'
	return endpoints.get_credentials()

@app.route("/credentials", methods=['DELETE'])
def delete_credentials():
	print 'endpoints.delete_credentials'
	return endpoints.delete_credentials()

@app.route("/accounts")
def accounts():
	print 'endpoints.accounts'
	return endpoints.accounts()

@app.route("/transactions")
def transactions():
	print 'endpoints.transactions'
	return endpoints.transactions()

# @app.route("/twofa", methods=['POST'])
# def twofa():
# 	try:
# 		logger = logging.getLogger('app')
# 		logger.debug('\n/twofa')
# 		params = json.loads(request.data)
# 		logger.debug(params)
# 		token = params['token']
# 		id_site = params['id_site']
# 		fatwo = params['twofa']
# 		logger.debug('Executing ... ')
# 		twofa_response = paybook.twofa(token,id_site,fatwo)
# 		logger.debug('Sending response ... ')
# 		twofa_response = _Utilities.Success(twofa_response).get_response()
# 	except _Paybook_Error as e:
# 		twofa_response = e.get_response()
# 	except Exception as e:
# 		twofa_response = _Utilities.internal_server_error(e)
# 	return twofa_response

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0")
