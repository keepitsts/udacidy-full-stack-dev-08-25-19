#Import Dependencies
from flask import Flask, render_template, request, redirect,jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Catagory, Base, StoreItem
from flask import session as login_session
import random
import string

#Create app
app = Flask(__name__)


#Client ID
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Bookstore Application"


#Create Engine
engine = create_engine('sqlite:///storeitems.db')
Base.metadata.bind = engine

#Create a Session
DBSession = sessionmaker(bind=engine)
session = DBSession()


#Create Google Sign in
@app.route('/login')
def showLogin():
	state = ''.join(random.choice(string.ascii_uppercase + string.digits)\
					for x in xrange(32))
	login_session['state'] = state
	return render_template('login.html', STATE=state)



#Create JSON API Endpoints
@app.route('/catagory/<int:catagory_id>/inventory/JSON')
def itemInventoryJSON(catagory_id):
	catagory = session.query(Catagory).filter_by(id=catagory_id).one()
    items = session.query(StoreItem).filter_by(catagory_id=catagory_id).all()
    return jsonify(StoreItems=[i.serialize for i in items])

@app.route('/catagory/<int:catagory_id>/inventory/<int:item_id>/JSON')
def storeItemJSON(catagory_id, item_id):
	store_Item = session.query(StoreItem).filter_by(id=item_id).one()
	return jsonify(store_Item=store_Item.serialize)

@app('/catagory/JSON')
def restaurantJSON():
	catagories = session.query(Catagory).all()
	return jsonify(catagories=[r.serialize for i in catagories])

#Google Sign In


#Run the Server
if __name__ == '__main__':
	app.debug = True
	app.run(host=localhost, port=8000)