#Import Dependencies
from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catagory, StoreItem

app = Flask(__name__)

engine = create_engine('sqlite:///storeitemsinventory.db')
Base.metadata.bind = engine

#Create a Session
DBSession = sessionmaker(bind=engine)
session = DBSession()

#JSON API Endpoints

@app.route('/')
@app.route('/catagory/JSON')
def catagoriesJSON():
	catagories = session.query(Catagory).all()
	return jsonify(catagories=[c.serialize for c in catagories])

@app.route('/catagory/storeItems/JSON')
def showStoreItemsJSON():
	storeItems = session.query(StoreItems).all()
	return jsonify(storeItems=[s.serialize for s in storeItems])

@app.route('catagory/<int:catagory_id>/items/JSON')
def showCatagoriesJSON()