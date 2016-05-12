#Paybook Lite Python

A light and simple web application to demonstrate how to take advantage of the Paybook Financial API (Sync) to pull information from Mexican Banks and Tax Authority.

## Requirements
1.  [Python] (https://python.org) v2.7.10
2.  [Flask] (http://flask.pocoo.org/) v0.10.1

   ```sh
   $ pip install Flask
   ```
3.  [Resquests](http://docs.python-requests.org/en/master/) HTTP for Humans v2.7.0

   ```sh
   $ pip install requests
   ```
4.  Sync API key

## Install (cli / terminal)

```sh
$ git clone https://github.com/Paybook/lite-python paybook-lite
```

## Configure
1. Create the file cloud/dependencies/constants.py and add your api key in API_KEY variable
   The database is created in localstorage with the name ```Python "localstorage"```
```Python
# -​*- coding: utf-8 -*​-import oss
PAYBOOK_LINK = 'https://sync.paybook.com/v1/'
API_KEY = "YOUR_PAYBOOK_KEY_HERE"
DB = "localstorage"
DEBUG_MODE = False
```

## Execute (cli / terminal)
1. In paybook-lite directory type **python main.py** command
2. Open a browser [http://localhost:5000/signup](http://localhost:5000/signup)
3. Create a new user
4. Login [http://localhost:5000/login](http://localhost:5000/login)
5. Add a site account in catalogs [http://localhost:5000/catalogs](http://localhost:5000/catalogs)
