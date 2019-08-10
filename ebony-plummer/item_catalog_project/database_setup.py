#Import SQLAlchemy Dependencies
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


#Created Catagory Class
class Catagory(Base):
    __tablename__ = 'catagory'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    @property
    def serialize(self):
        #Return object data in a easily serializeable format.
        return {
            'name': self.name,
            'id' : self.id,
        }


#StoreItem Class
class StoreItem(Base):
    __tablename__ = 'store_item'

    name = Column(String(150), nullable=False)
    id = Column(Integer, primary_key=True)
    author = Column(String(50), nullable=False)
    genre = Column(String(20))
    price = Column(String(10), nullable=False)
    description = Column(String(500))
    catagory_id = Column(Integer, ForeignKey('catagory.id'))
    catagory = relationship(Catagory)

    @property
    def serialize(self):
        #Return object data in a easily serializable format
        return {
            'name' : self.name,
            'id' : self.id,
            'author' : self.author,
            'genre' : self.genre,
            'price' : self.price,
            'description' : self.description,
        }


#Create the Database
engine = create_engine('sqlite:///storeitemsinventory.db')

Base.metadata.create_all(engine)


