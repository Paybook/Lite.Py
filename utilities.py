# -​*- coding: utf-8 -*​-

import logging
from logging.handlers import TimedRotatingFileHandler
from flask import json
from flask import make_response
import sys
import getopt

def setup_logger(name):
	file_name = name + '.log'
	complete_file_name = './' + file_name
	logging_level = logging.DEBUG
	formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(module)s - %(funcName)s:%(lineno)d - %(message)s','%Y-%m-%d %H:%M:%S')
	formatter = logging.Formatter('%(message)s')		
	logging_handler = TimedRotatingFileHandler(complete_file_name, when='midnight')
	logging_handler.setFormatter(formatter)
	logger = logging.getLogger(name)
	logger.setLevel(logging_level)		
	logger.addHandler(logging_handler)
	return logger

class Error(Exception):

	http_code = ''
	content = ''

	def __init__(self,content,code):
		self.http_code = code
		self.content = content

	def get_json(self):
		error_json = self.content
		return json.dumps(error_json)

	def get_response(self):
		return make_response(self.get_json(),self.http_code)

class Success(Exception):

	http_code = 200
	content = ''

	def __init__(self,content):
		self.content = content

	def get_json(self):
		success_json = self.content
		return json.dumps(success_json)

	def get_type(self):
		return _Pauli_Constants.RESPONSE_TYPES['SUCCESS']
	
	def get_response(self):
		return make_response(self.get_json(),self.http_code)

def internal_server_error(e):
	print 'Wops! Internal Server Error :('
	print e
	return Error('Internal Server Error',500).get_response()

def get_cmd_params(argv):
	cmd_params = {
		'api_key' : None,
		'database' : None
	}#End of params
	a_param = None
	d_param = None
	try:
		opts, args = getopt.getopt(argv,"a:d:",["apikey=","database="])
	except Exception as e:
		print 'Error getting params ... '
		print e
		sys.exit()
	for opt, arg in opts:
		if opt == '-a' or opt == '--apikey':
			cmd_params['api_key'] = arg
			a_param = True
		if opt == '-d' or opt == '--database':
			cmd_params['database'] = arg
			d_param = True
	if cmd_params['api_key'] is None or a_param is None:
		print '-a param is required (paybook api key)'
		sys.exit()
	# if cmd_params['database'] is None or d_param is None:
	# 	print '-d param is required (database file path)'
	# 	sys.exit()
	return cmd_params




