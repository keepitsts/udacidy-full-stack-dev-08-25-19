# Import SQLAlchemy Dependencies

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


# Creates the User class for the user table.
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

# Creates the Category class for the category table.


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Return object data in a easily serializeable format.
        return {
            'name': self.name,
            'id': self.id,
        }


# Creates the StoreItem class for the store_item table.

# StoreItem Class
class StoreItem(Base):
    __tablename__ = 'store_item'

    name = Column(String(150), nullable=False)
    id = Column(Integer, primary_key=True)
    author = Column(String(50), nullable=False)
    genre = Column(String(20))
    price = Column(String(10), nullable=False)
    description = Column(String(500))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Return object data in a easily serializable format
        return {
            'name': self.name,
            'id': self.id,
            'author': self.author,
            'genre': self.genre,
            'price': self.price,
            'description': self.description,
        }


# Creates a database
# engine = create_engine('sqlite:///storeitemsinventory.db')

# Creates a database with users.
engine = create_engine('sqlite:///storeitemsinventorywithusers.db')


Base.metadata.create_all(engine)
