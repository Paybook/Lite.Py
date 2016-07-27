import sqlite3
import datetime
import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

connection = sqlite3.connect(project_path + '/paybook.db',check_same_thread=False)
cur = connection.cursor()

users_table_cmd = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
users_table_exist = cur.execute(users_table_cmd).fetchone()
if not users_table_exist:
	cur.execute('''CREATE TABLE users (username text, password text, id_user text, date text, token text)''')

class User():	

	def __init__(self,*args,**kwargs):
		if len(args) == 2:
			self.username = args[0]
			self.password = args[1]
			self.token = None
		if len(args) == 1:
			self.token = args[0]
			self.username = None
			self.password = None

	def save(self):
		date = datetime.datetime.utcnow()
		insert_user = [(self.username,self.password ,self.id_user,date,''),]
		cur.executemany('INSERT INTO users VALUES (?,?,?,?,?)', insert_user)
		connection.commit()	
	
	def set_token(self,token):
		self.token = token
		update_user = [(self.token,self.username),]
		cur.executemany('''UPDATE users SET token = ? WHERE username = ? ''',update_user)
		connection.commit()

	def set_id_user(self,id_user):
		self.id_user = id_user

	def get_id_user(self):
		if self.token is not None:
			cur.execute('SELECT * FROM users WHERE token=?',(self.token,))
		else:
			username = self.username
			cur.execute('SELECT * FROM users WHERE username=?',(username,))
		user = cur.fetchone()
		return user[2]

	def do_i_exist(self):
		username = self.username
		cur.execute('SELECT * FROM users WHERE username=?',(username,))
		user = cur.fetchone()	
		if user is not None:
			return True
		else:
			return False

	def login(self):
		username = self.username
		cur.execute('SELECT username, password FROM users WHERE username=?',(username,))
		user_and_psw = cur.fetchone()
		username = None
		password = None
		if user_and_psw is not None:
			username = user_and_psw[0]
			password = user_and_psw[1]		
		if username == self.username and password == self.password:	
			return True
		else:		
			return False


			