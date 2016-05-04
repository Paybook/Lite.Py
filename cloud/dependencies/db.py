# -​*- coding: utf-8 -*​-import os
from pymongo import MongoClient
from json import dumps

client = MongoClient("YOUR_DB_HERE")
db = client['lite']
users = db['users']
accounts = db['accounts']

def log_in(session,user, psw):
	query = users.find_one({'user':user})
	if query is not None:
		if query['user'] == user and query['password'] == psw:
			session['id_user_db'] = str(query['_id'])			
			return True
		else:
			return False
	else:
		return False

def search_user_in_db(user):	
	query = users.find_one({'user':user})
	if query is not None:				
		return True
	else:		
		return False

def get_accounts(OwnerId):
	query = accounts.find({'OwnerId':OwnerId})	
	return query	

def get_response(OwnerId, account_name):
	query = accounts.find_one({'$and':[{'OwnerId': OwnerId},{'name': account_name}]})
	return query['data']

def account_exists(OwnerId, account_name):
	query = accounts.find_one({'$and':[{'OwnerId': OwnerId},{'name': account_name}]})
	if query is not None:
		return True
	else:
		return False

def modify_credentials_in_db(dicc):
	accounts.update({'OwnerId': dicc['OwnerId'], 'name':dicc['name']},{'$set':{'credentials':dicc['credentials'],'data': dicc['data']}})