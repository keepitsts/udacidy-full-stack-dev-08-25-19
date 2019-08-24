# Import Dependencies
from flask import Flask, render_template
from flask import request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, StoreItem, User

# Imports for the login function
from flask import session as login_session
import random
import string

# Imports for Google OAuth
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)


# Connects the Google Client ID to this flask application.
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

APPLICATION_NAME = "Oracle Books"

# Connect to the database
# engine = create_engine('sqlite:///storeitemsinventory.db')

# Connects to the database with users.
engine = create_engine('sqlite:///storeitemsinventorywithusers.db')

Base.metadata.bind = engine

# Create a Session
DBSession = sessionmaker(bind=engine)
session = DBSession()


# JSON API Endpoints

# @app.route('/')
@app.route('/api/v1.0/category/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[c.serialize for c in categories])


@app.route('/api/v1.0/category/storeItems/JSON')
def showStoreItemJSON():
    storeItem = session.query(StoreItem).all()
    return jsonify(storeItem=[s.serialize for s in storeItem])


@app.route("/api/v1.0/catalog/<int:category_id>/inventory/JSON")
def showCategoryItemsJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(StoreItem).filter_by(category_id=category_id).all()

    return jsonify(StoreItems=[i.serialize for i in items])


@app.route("/api/v1.0/catalog/<int:category_id>/<int:inventory_id>/JSON")
def storeItemsJSON(category_id, inventory_id):
    store_item = session.query(StoreItem).filter_by(id=inventory_id).first()
    return jsonify(store_item=store_item.serialize)


@app.route('/api/v1.0/category/<int:item_id>/oneItem')
def viewOneItem(item_id):
    view_item = session.query(StoreItem).one()
    return jsonify(view_item=view_item.serialize)


# The following code is the code for Google OAuth login.
"""
This function is the login function that allows users to log into
this application with their Google credentials. This function also creates
an anti forgery token.
"""


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


"""
Adding a /gconnect route that response to POST requests. Also adding a
gconnect method that accepts the authorization code from the client,
exchanges it for an access token, uses it to make an API call to the
OAuth server and responds eo the client.
"""


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate the state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code.
    request.get_data()
    code = request.data.decode('utf-8')

    try:
        # Upgrade the authorization code into a credentials object.
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    # Submit request, parase response.
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error'), 500))
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is for the intended user.
    googleUser_id = credentials.id_token['sub']
    if result['user_id'] != googleUser_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID"), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verfiy that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's"), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_googleUser_id = login_session.get('googleUser_id')
    if stored_access_token is not None and \
            googleUser_id == stored_googleUser_id:
        response = make_response(json.dumps(
            'Current user is already connectes'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session fro later use.
    login_session['access_token'] = access_token
    login_session['googleUser_id'] = googleUser_id

    # Get user information.
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # See if the user exists, if it doesn't make a new one.
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome,'
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']

    output += ''' " style = "width: 300px; height: 300px;border-radius:
    150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;">'''

    flash("you are now logged in as %s" % login_session['username'])
    return output


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).first()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).first()
        return user.id
    except Exception:
        return None


# DISCONNET = Revoke a current user's token and reset their login_session.

@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps(
            'Curent user is not connected'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print('in gdisconnect access token is %s', access_token)
    print('User name is: ')
    print(login_session['username'])
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' \
        % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print('result is ')
    print(result)
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['googleUser_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for the given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


""" The following routes and functions pull data from the Store Items
Inventory database and inserts the data into html templates. """

# Categories


# Show all categories.
@app.route('/')
@app.route('/catalog')
def showCategories():
    categories = session.query(Category).all()
    if 'username' not in login_session:
        return render_template('publicCatalog.html', categories=categories)
    # return "These are the categories."
    else:
        return render_template('categories.html', categories=categories)


# Public Catalog
# @app.route('/')
@app.route('/catalog/public/')
def publicCatalog():
    categories = session.query(Category).all()
    return render_template('publicCatalog.html', categories=categories)


# Create a new category.
@app.route('/catalog/category/new/', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'],
                               user_id=login_session['user_id'])
        session.add(newCategory)
        session.commit()
        flash("New Category %s Successfully Created!" % newCategory.name)
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')


# Edit a category.
@app.route('/catalog/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(
        Category).filter_by(id=category_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedCategory.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this category. Please create your own category in order to edit.');}</script><body onload='myFunction()''>"  # noqa
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            session.add(editedCategory)
            session.commit()
            flash("Category Successfully Edited! %s" % editedCategory)
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category=editedCategory)


# Delete a category.
@app.route('/catalog/category/<int:category_id>/delete/',
           methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(
        Category).filter_by(id=category_id).one_or_none()
    if 'username' not in login_session:
        return redirect('/login')
    if categoryToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this category. Please create your own category in order to delete.');}</script><body onload='myFunction()''>"  # noqa
    if request.method == 'POST':
        session.delete(categoryToDelete)
        session.commit()
        flash("Category Successfully Deleted! %s" % categoryToDelete)
        return redirect(url_for('showCategories', category_id=category_id))
    else:
        return render_template('deleteCategory.html',
                               category=categoryToDelete)


# Items

# This function shows all the items in a catagory.
@app.route('/catalog/category/<int:category_id>/')
@app.route('/catalog/category/<int:category_id>/inventory')
def showItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    creator = getUserInfo(category.user_id)
    items = session.query(StoreItem).filter_by(category_id=category_id).all()
    if 'username' not in login_session:
        return render_template('publicCatalogItems.html', items=items,
                               category=category, creator=creator)
    else:
        return render_template('items.html', items=items, category=category,
                               creator=creator)


# List of items for the public catalog.
@app.route('/catalog/public/<int:category_id>/')
@app.route('/catalog/category/public/<int:category_id>/inventory')
def showItemsPublic(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(StoreItem).filter_by(category_id=category_id).all()
    return render_template('publicCatalogItems.html', items=items,
                           category=category)


""" #This function returns a list of the item names.
@app.route('/catalog/<int:category_id>/')
@app.route('/catalog/category/<int:category_id>/itemlist') def
listNames(category_id): category =
session.query(Category).filter_by(id=category_id).one() items =
session.query(StoreItem).filter_by(category_id=category_id).all() return
render_template('viewItems.html', items=items, category=category) """

# This function allows the user to view a single item.


@app.route('/catalog/category/<int:category_id>/<int:item_id>/item')
def viewItem(category_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(StoreItem).filter_by(id=item_id).one()
    return render_template("viewItem.html", category=category, item=item)


@app.route('/catalog/public/category/<int:category_id>/<int:item_id>/item')
def viewItemPublic(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(StoreItem).filter_by(id=item_id).one()
    return render_template("viewItemPublic.html", category=category, item=item)


# Create a new store item.
@app.route('/catalog/category/<int:category_id>/inventory/new/',
           methods=['GET', 'POST'])
def newStoreItem(category_id):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(id=category_id).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized to add items this category. Please create your own category in order to add items.');}</script><body onload='myFunction()''>"  # noqa
    if request.method == 'POST':
        newItem = StoreItem(
            name=request.form['name'],
            author=request.form['author'],
            genre=request.form['genre'],
            price=request.form['price'],
            description=request.form['description'],
            category_id=category_id,
            user_id=category.user_id)

        session.add(newItem)
        session.commit()
        flash("New Category %s Item Successfuly Created!" % (newItem.name))

        return redirect(url_for('showItems', category_id=category_id))

    else:
        return render_template('newItem.html', category_id=category_id)


# Edit a store item.
@app.route('/catalog/edit/<int:category_id>/<int:inventory_id>/edit/',
           methods=['GET', 'POST'])
def editStoreItem(category_id, inventory_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedItem = session.query(StoreItem).filter_by(id=inventory_id).one()
    category = session.query(Category).filter_by(id=category_id).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert ('You are not authorized to edit items this category. Please create your own category in order to edit items.');}</script><body onload='myFunction()''>"  # noqa
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['author']:
            editedItem.author = request.form['author']
        if request.form['genre']:
            editedItem.genre = request.form['genre']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['description']:
            editedItem.description = request.form['description']

        session.add(editedItem)
        session.commit()
        flash("Item Successfully Edited!")
        return redirect(url_for('showItems', category_id=category_id))

    else:
        # catagories = session.query(Catagory).all()
        return render_template('editItem.html', category_id=category_id,
                               inventory_id=inventory_id,  item=editedItem)


# Delete a store item.
@app.route('/catalog/delete/<int:category_id>/<int:inventory_id>/delete/',
           methods=['GET', 'POST'])
def deleteStoreItem(category_id, inventory_id):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(id=category_id).one()
    itemToDelete = session.query(StoreItem).filter_by(id=inventory_id).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete items this category. Please create your own category in order to delete items.');}</script><body onload='myFunction()''>"  # noqa
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Item Successfuly Deleted!")
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('deleteItem.html', category_id=category_id,
                               item=itemToDelete)

# Starting the Flask Server


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='localhost', port=8000)
