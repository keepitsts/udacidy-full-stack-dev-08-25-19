# **Welcome to Oracle Books!**


## Introduction

Oracle Books is an online store that sells books, music, and movies. We at Oracle Books hope that you will find something that interest you at our store. The Oracle Books Application is and application that displays our inventory. Users who create accounts with our application are able to create, edit, and delete their own items and categories. No need to worry about another user modifying your content, our website uses the state of the art Google OAuth to project your information.

The Oracle Books application is a RESTful web application that uses the Python Flask Framework and Google OAuth authentication. This applications uses CRUD, (create, read, update, and delete) to allow users to view and modify categories and items.



## Dependencies and Prerequisites

1. [SQLAlchemy](https://www.sqlalchemy.org/)

2. [Flask](https://palletsprojects.com/p/flask/)

3. [Jinja Template Engine](https://palletsprojects.com/p/jinja/)

4. HTML

5. [Bootstrap](https://getbootstrap.com/)

6. [Google OAuth](https://developers.google.com/identity/sign-in/web/)


### Python Dependencies

1. project.py

    * Main Imports
        ```
   	    from flask: Flask, render_template, request, redirect, jsonify, url_for, flash
   		from sqlalchemy import create_engine
   		from sqlalchemy.orm import sessionmaker
        from database_setup import Base, Category, StoreItem, User
        ```

    * Imports for the login function
        ```
        from flask import session as login_session
        import random
        import string
        ```

    * Imports for Google OAuth
    	```
        from oauth2client.client import flow_from_clientsecrets
        from oauth2client.client import FlowExchangeError
        import httplib2
        import json
        from flask import make_response
        import requests
        ```


2. database_setup.py
    
    ```
    import os
    import sys
    from sqlalchemy import Column, ForeignKey, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import relationship
    from sqlalchemy import create_engine
    ```

3. store_items.py

    ```
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from database_setup import Category, Base, StoreItem, User
    ```


## Setup/Installation

### Backend

1. database_setup.py

   The `database_setup.py` file sets up the database for this application. The database for this application contains ...the following tables: Category, StoreItem, and User. The SQLAlchemy Object Relational Mapper, (ORM) is used to create the classes that serve as the bases for the tables in the database for this project.

2. store_items.py

   The `store_items.py` file inserts the initial categories and items that can be seen in this application. Like the `database_setup.py` file the `store_items.py` file also uses the SQLAlchemy ORM for its functionality. 
   The `store_items.py` uses the CRUD, (create, read, update, and delete) functionality to add categories and items to the database for this application.

3. project.py

   The `project.py` contains the server and additional application logic that runs the Oracle Books application. SQLAlchemy uses CRUD functions which allows users to read and modify the data in the application. The server that runs the application is created by the Flask framework.

4. OAuth Authentication

   This application uses Google OAuth to authenticate users and allow users to login to Oracle Books with their Google account.


### Frontend

The user interface for the Oracle Books application was created using HTML and the Bootstrap framework for styling. The python code is inserted into the HTML using the Jinja template engine. Jinja uses HTML escaping to insert the Python code into the HTML so that code can be seen by the users of the application.



## Usage

1. Create the database for the application by running `python database_setup.py` in the terminal window.

2. Insert the initial categories and items into the database by running `python store_items.py` 
in the terminal window .

3. Start the Flask server by running `python project.py` in the terminal window.

4. Once the server starts, the URL `http://localhost:8000` will appear in the terminal window. Copy and paste that link into your browser, and press enter.

5. When you first enter the application, you will see the public page. If you are not logged in you will only be able to view the categories and items on the public page. you will not be able to modify or create items or categories.

6. In order to have the full user experience login to the application by clicking on the login button. After you click on the login button you will see a Google Sign in button.

7. Click on the Google Sign in button to log into the application. Once you log into the application, you will be able to create items, and modify the items that you created.



## Works Cited

1. Udacity "Full Stack Developer Nanodegree" Course Material.

2. [Udacity Full Stack Foundations](https://github.com/udacity/Full-Stack-Foundations)

3. [Udacity OAuth2.0](https://github.com/udacity/OAuth2.0)

4. [Udacity ud330](https://github.com/udacity/ud330)

5. [ddavignon/item-catalog](https://github.com/ddavignon/item-catalog)

6. [SDey96/Udacity-Item-Catalog-Project](https://github.com/SDey96/Udacity-Item-Catalog-Project)

7. [Google Sign-in for Websites](https://developers.google.com/identity/sign-in/web/)

8. [StackOverflow check if .one() is empty sqlAlchemy](https://stackoverflow.com/questions/24985989/check-if-one-is-empty-sqlalchemy)





