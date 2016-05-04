#Paybook Lite Python

A light and simple web application to demonstrate how to take advantage of the Paybook Financial API (Sync) to pull information from Mexican Banks and Tax Authority.

## Requirements
1. Python
2. [Flask](http://flask.pocoo.org/)
2. [Pymongo](https://api.mongodb.org/python/current/) Only for DB
3. [Resquests](http://docs.python-requests.org/en/master/) HTTP for Humans
4.Sync API key 

## Install (cli / terminal)
1. git clone https://github.com/Paybook/Lite.Python/

## Configure
1. Insert your api key in /cloud/dependencies/_Constants.py
```Python
  	# -​*- coding: utf-8 -*​-import oss
	PAYBOOK_LINK = 'https://sync.paybook.com/v1/'
	API_KEY = "YOUR_PAYBOOK_KEY_HERE"
```
2. Configure your mongoDB in /cloud/dependencies/_DB.py
```Python
  	client = MongoClient("YOUR_DB_HERE")
	db = client['lite']
	users = db['users']
	accounts = db['accounts']
```

## Execute (cli / terminal)
1. In paybook-lite directory type **python main.py** command
2. Open a browser [http://localhost:5000/signup](http://localhost:5000/signup)
3. Create a new user
4. Login [http://localhost:5000/login](http://localhost:5000/login)
5. Add a site account in catalogs [http://localhost:5000/catalogs](http://localhost:5000/catalogs)
