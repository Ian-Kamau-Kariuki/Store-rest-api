# STORE REST API

## Installation

1.Clone Repo

```
https://github.com/Ian-Kamau-Kariuki/Store-rest-api.git
```

2.Install Virtual Environment

```
pip3 install virtualenv
```

3.Create virtual environment

```
virtualenv env
```

4.Activate virtual environment in parent directory of your "env"

For Linux systems and MAC

```
source env/bin/avtivate
```

For Windows

```
env\lib\activate.bat
```

5.Install requierements
```
pip install - r requirements.txt
```

6.Run app

```
python app.py
```

# ENDPOINTS

GET /items-----------> This returns a list of items, each in JSON format.

GET /item/name-----> This returns one specific item uniquely identified by its name. No items may have the same name.

POST /item/name----> Creates a new item. If the item already exists, it will fail.

PUT item/name------> Creates a new item or Update an exixting item. 

DEL item/name------> Deletes an item uniquely identified by its name.

POST /auth-----------> Generates the jwt token.

POST /register-------> Registers users.

GET /stores----------> This returns a list of stores, each in JSON format

GET /store/name----> This returns one specific store uniquely identified by its name. No two stores may have the same name.

POST store/name----> Creates a new store.

DEL /store/name----> Deletes store uniquely identified by its name.



## Implementation
This project is implemented using Flask, Flask-RESTful, Flask-JWT and Flask-SQLAlchemy

Deployed on Heroku.
