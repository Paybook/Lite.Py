
# Paybook Python Lite

Before starting remember you must create a config.json file with your Paybo API Key \0/

 ```{
    "paybook_api_key" : YOUR_API_KEY_GOES_HERE
  }
  ```

**Signup**
----
  Register a new user to Paybook

* **URL**

  http://<_your_ip_>:5000/signup

* **Method:**
  
  <_Content-type:application/json_>

  `POST` 

   **Required:**
 
   `username=[string]`
   `password=[string]`

* **Success Response:**
  
   `{'signed_up':true}`
 
* **Error Response:**
  
  `{'signed_up':false}`


* **Sample Call:**

 ```curl
  curl -X POST -H "Content-type:application/json" -d '{"username":"some_username","password":"some_password"}' http://127.0.0.1:5000/signup
  ```

**Login**
----
  Login an exisiting user

* **URL**

  http://<_your_ip_>:5000/login

* **Method:**
  
  <_Content-type:application/json_>

  `POST` 

   **Required:**
 
   `username=[string]`
   `password=[string]`

* **Success Response:**
  
   `{'token':'your_session_token'}`
 
* **Error Response:**
  
  `{'token':false}`


* **Sample Call:**

 ```curl
  curl -X POST -H "Content-type:application/json" -d '{"username":"some_username","password":"some_password"}' http://127.0.0.1:5000/login
  ```

**Catalogs**
----
  Retrieve the set of institutions available

* **URL**

  http://<_your_ip_>:5000/catalogs

* **Method:**
  
  <_Content-type:application/json_>

  `GET`

   **Required:**
 
   `token=[string]`

* **Success Response:**
  
   `{'catalogs':[Catalogs]}`
 
* **Error Response:**
  
  `{'catalogs':[]}`


* **Sample Call:**

 ```
  curl -X GET -H "Content-type:application/json" -d '{"token":"your_token"}' http://127.0.0.1:5000/catalogs
  ```

**Credentials**
----
  Register credentials for a specific institution

* **URL**

  http://<_your_ip_>:5000/credentials

* **Method:**
  
  <_Content-type:application/json_>

  `POST`

   **Required:**
 
   `token=[string]`
   `id_site=[string]`
   `credentials_user=[string]`
   `credentials_password=[string]`

* **Success Response:**
  
   `{'credentials':NEW_CREDENTIALS}`
 
* **Error Response:**
  
  {'catalogs':false}`


* **Sample Call:**

 ```
 curl -X POST -H "Content-type:application/json" -d '{"token":"your_token","id_site":"some_id_site","credentials_user":"some_credential","credentials_password":"some_password"}
' http://127.0.0.1:5000/credentials
  ```

**Status**
----
  Get the sync status of a specific institution

* **URL**

  http://<_your_ip_>:5000/status

* **Method:**
  
  <_Content-type:application/json_>

  `GET`

   **Required:**
 
   `token=[string]`
   `id_site=[string]`

* **Success Response:**
  
   `{'status':STATUS}`
 
* **Error Response:**
  
  {'status':false}`


* **Sample Call:**

 ```
curl -X GET -H "Content-type:application/json" -d '{"token":"your_token","id_site":"some_id_site"}
' http://127.0.0.1:5000/status
  ```
  
**Accounts**
----
  Get the accounts registered in a specific institution

* **URL**

  http://<_your_ip_>:5000/accounts

* **Method:**
  
  <_Content-type:application/json_>

  `GET`

   **Required:**
 
   `token=[string]`
   `id_site=[string]`

* **Success Response:**
  
   `{'accounts':[Accounts]}`
 
* **Error Response:**
  
  {'accounts':[]}`


* **Sample Call:**

 ```
curl -X GET -H "Content-type:application/json" -d '{"token":"your_token","id_site":"some_id_site"}
' http://127.0.0.1:5000/accounts
  ```
  
**Transactions**
----
  Get the accounts registered in a specific account

* **URL**

  http://<_your_ip_>:5000/transactions

* **Method:**
  
  <_Content-type:application/json_>

  `GET`

   **Required:**
 
   `token=[string]`
   `id_account=[string]`

* **Success Response:**
  
   `{'transactions':[Transactions]}`
 
* **Error Response:**
  
  {'transactions':[]}`


* **Sample Call:**

 ```
curl -X GET -H "Content-type:application/json" -d '{"token":"your_token","id_account":"some_id_account"}
' http://127.0.0.1:5000/transactions
  ```


