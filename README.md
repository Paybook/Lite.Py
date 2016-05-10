#Paybook Lite Python

A light and simple web application to demonstrate how to take advantage of the Paybook Financial API (Sync) to pull information from Mexican Banks and Tax Authority.

## Requirements
1. Python v2.7.10
2. [Flask] (http://flask.pocoo.org/) v0.10.1
3. [Resquests](http://docs.python-requests.org/en/master/) HTTP for Humans v2.7.0
4. Sync API key 

## Install (cli / terminal)
1. git clone https://github.com/Paybook/Lite.Python/

## Configure
1. Insert your api key in /cloud/dependencies/_Constants.py
   The database is created in RAM setting DB with the special name ```Python ":memory:"``` (Each time the application is restarted the database is deleted)
```Python
  	# -​*- coding: utf-8 -*​-import oss
	PAYBOOK_LINK = 'https://sync.paybook.com/v1/'
	API_KEY = "YOUR_PAYBOOK_KEY_HERE"
	DB = ":memory:"
	DEBUG_MODE = False
```

## Execute (cli / terminal)
1. In paybook-lite directory type **python main.py** command
2. Open a browser [http://localhost:5000/signup](http://localhost:5000/signup)
3. Create a new user 
4. Login [http://localhost:5000/login](http://localhost:5000/login)
5. Add a site account in catalogs [http://localhost:5000/catalogs](http://localhost:5000/catalogs)
