import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    UserName = Column(String(250), nullable=False)
    Password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    phone_number = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    inscriptionDate = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class Character(Base):
    __tablename__ = 'character'
    name= Column(String(250), primary_key=True)
    birth_date = Column(Integer)
    height = Column(Integer)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    favorite_list_id = Column(Integer, ForeignKey('favorite_list.id'))

class Planet(Base):
    __tablename__ = 'planet'
    name= Column(String(250), primary_key=True)
    population = Column(Integer)
    diameter = Column(Integer)
    climate= Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    favorite_list_id = Column(Integer, ForeignKey('favorite_list.id'))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    name= Column(String(250), primary_key=True)
    model = Column(String(250), nullable=False)
    max_speed = Column(String(250), nullable=False)
    passenger = Column(Integer)
    starships_class = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    favorite_list_id = Column(Integer, ForeignKey('favorite_list.id'))

class Favorite_list(Base):
    __tablename__ = 'favorite_list'
    name= Column(String(250), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
