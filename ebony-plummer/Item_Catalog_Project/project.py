#Import Dependencies
from flask import Flask, render_template, request, redirect,jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Catagory, Base, BookItem, MusicItem, MovieItem

#Create app
app = Flask(__name__)

#Create Engine
engine = create_engine('sqlite:///storeitems.db')
Base.metadata.bind = engine

#Create a Session
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Create JSON API Endpoints
@app.route('catagory/<int:catagory_id>')

#Run the Server
if __name__ == '__main__':
	app.debug = True
	app.run(host=localhost, port=8000)