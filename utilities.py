# -​*- coding: utf-8 -*​-

import logging
from logging.handlers import TimedRotatingFileHandler
from flask import json
from flask import make_response

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