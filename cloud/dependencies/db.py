# -​*- coding: utf-8 -*​-import os
import sqlite3
from json import dumps, loads
from cloud.dependencies import constants as _Constants
#from pymongo import MongoClient
#from json import dumps

connection = sqlite3.connect(_Constants.DB, check_same_thread=False)
cur = connection.cursor()

# Create table
tb_create_users = """CREATE TABLE users (username text, password text, id_user text, date text)"""
tb_exists_users = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
if not cur.execute(tb_exists_users).fetchone():
    cur.execute(tb_create_users)

tb_create_credentials = """CREATE TABLE credentials (ownerId text, institution_name text, id_site text, credentials text, data text)"""
tb_exists_credentials = "SELECT name FROM sqlite_master WHERE type='table' AND name='credentials'"
if not cur.execute(tb_exists_credentials).fetchone():
    cur.execute(tb_create_credentials)


def sqliter(string):
	return (string,)

def parse_accounts(accounts_sql):	
	accounts = []
	for item in accounts_sql:
		account = {}
		account_name = item[1]
		account_id = item[2]
		account['name'] = account_name
		account['id_site'] = account_id
		accounts.append(account)
	return accounts

def parse_sync_data(sync_data):
	data = sync_data[0]
	data_json = loads(data)
	return data_json

def log_in(session,user, psw):	
	_user = sqliter(user)
	cur.execute('SELECT username, password FROM users WHERE username=?', _user)
	user_and_psw = cur.fetchone()
	username = None
	password = None
	if user_and_psw is not None:
		username = user_and_psw[0]
		password = user_and_psw[1]		
	if username == user and password == psw:		
		return True
	else:		
		return False

def create_user(user):	
	username = user['user']
	password = user['password']
	id_user = user['id_user']
	date = user['date']
	insert_user = [(username ,password ,id_user ,date),]	
	cur.executemany('INSERT INTO users VALUES (?,?,?,?)', insert_user)
	# Save (commit) the changes	
	connection.commit()	

def search_user_in_db(user_name):	
	user = sqliter(user_name)
	cur.execute('SELECT * FROM users WHERE username=?', user)
	user = cur.fetchone()	
	if user is not None:
		return True
	else:
		return False

def get_id_user(username):	
	user = sqliter(username)	
	cur.execute('SELECT id_user FROM users WHERE username=?', user)
	result = cur.fetchone()
	id_user = None
	if result != None:
		id_user = result[0]
	return id_user	

def get_accounts(ownerId):	
	ownerId = sqliter(ownerId)
	cur.execute('SELECT * FROM credentials WHERE ownerId=?', ownerId)
	accounts = cur.fetchall()
	return parse_accounts(accounts)	

def get_response(ownerId, account_name):	
	ownerId = ownerId
	institution_name = sqliter(account_name)
	cur.execute('SELECT data FROM credentials WHERE ownerId=:ownerId AND institution_name=:institution_name', {"ownerId": ownerId, "institution_name": account_name})
	data = cur.fetchone()	
	return parse_sync_data(data)

def credential_exists(ownerId, account_name):	
	sqlt_ownerId = sqliter(ownerId)	
	institution_name = sqliter(account_name)
	cur.execute('SELECT * FROM credentials WHERE ownerId=:ownerId AND institution_name=:institution_name', {"ownerId": ownerId, "institution_name": account_name})
	credentials = cur.fetchone()	
	if credentials is not None:
		return True
	else:
		return False

def create_credentials(dicc):	
	ownerId = dicc['ownerId']
	institution_name = dicc['name']
	id_site = dicc['id_site']
	credentials = dumps(dicc['credentials']) 
	data = dumps(dicc['data'])
	insert_credentials = [(ownerId, institution_name, id_site, credentials, data),]
	cur.executemany('INSERT INTO credentials VALUES (?,?,?,?,?)', insert_credentials)
	connection.commit()

def modify_credentials_in_db(dicc):	
	ownerId = sqliter(dicc['ownerId'])
	institution_name = sqliter(dicc['name'])
	credentials = dumps(data['credentials'])
	data = dumps(dicc['data'])
	cur.execute('UPDATE credentials SET credentials=:credentials WHERE ownerId=:ownerId AND institution_name=:institution_name', {"ownerId": ownerId, "institution_name": account_name, "credentials": credentials, "data": data})	

def search_users():	
	cur.execute('SELECT * FROM users')
	user = cur.fetchall()	
