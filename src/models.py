import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    userID = Column(Integer, primary_key=True)
    userName = Column(String(20), unique=True, nullable=False)
    favoriteID = Column(Integer, ForeignKey('favorite.favoriteID'))
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)
    favorite = relationship('Favorite', back_populates = 'user', uselist = False )

class Favorite(Base):
    __tablename__ = 'favorite'
    favoriteID = Column(Integer, unique =True)
    id = Column(Integer, primary_key=True)
    planetsID = Column(String(20), unique=True, nullable=False)
    speciesID = Column(String(20), unique=True, nullable=False)
    vehiclesID = Column(String(20), unique=True, nullable=False)
    userID = Column(Integer, ForeignKey('user.userID'))
    user = relationship('User', back_populates="favorite")

class People(Base):
    __tablename__ = 'people'
    peopleID = Column(Integer, unique = True, primary_key=True, nullable = False)
    uid = Column(Integer, unique = True, nullable = False)
    speciesName = Column(String, unique = True, nullable = False)
    description = Column(String, unique = True, nullable = False)
    planetID = Column(Integer, unique = True, nullable = False)
    height = Column(Integer, unique = True, nullable = False)
    mass = Column(Integer, unique = True, nullable = False)
    hair_color = Column(String, unique = True, nullable = False)
    skin_color = Column(String, unique = True, nullable = False)
    eye_color = Column(String, unique = True, nullable = False)
    birth_year = Column(String, unique = True, nullable = False)
    gender = Column(String, unique = True, nullable = False)
    created = Column(String, unique = True, nullable = False)
    edited = Column(String, unique = True, nullable = False)
    url = Column(String, unique = True, nullable = False)
    favoriteID = Column(Integer, ForeignKey('favorite.favoriteID'))
    favorite = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    planetID = Column(Integer, unique = True, primary_key=True, nullable = False)
    uid = Column(Integer, unique = True, nullable = False)
    planetName = Column(Integer, unique = True, nullable = False)
    description = Column(String, unique = True, nullable = False)
    diameter = Column(Integer, unique = True, nullable = False)
    rotation_period = Column(Integer, unique = True, nullable = False)
    orbital_period = Column(Integer, unique = True, nullable = False)
    gravity = Column(Integer, unique = True, nullable = False)
    population = Column(Integer, unique = True, nullable = False)
    climate = Column(Integer, unique = True, nullable = False)
    terrain = Column(Integer, unique = True, nullable = False)
    surface_water = Column(Integer, unique = True, nullable = False)
    created = Column(String, unique = True, nullable = False)
    edited = Column(String, unique = True, nullable = False)
    url = Column(String, unique = True, nullable = False)
    favoriteID = Column(Integer, ForeignKey('favorite.favoriteID'))

class Starships(Base):
    __tablename__ = 'starships'
    shipID = Column(Integer, unique = True, primary_key=True, nullable = False)
    shipName = Column(String, unique = True, nullable = False)
    description = Column(String, unique = True, nullable = False)
    model = Column(String, unique = True, nullable = False)
    starship_class = Column(String, unique = True, nullable = False)
    manufacturer = Column(String, unique = True, nullable = False)
    cost_in_credits = Column(Integer, unique = True, nullable = False)
    length = Column(Integer, unique = True, nullable = False)
    crew = Column(Integer, unique = True, nullable = False)
    passengers = Column(Integer, unique = True, nullable = False)
    max_atmosphering_speed = Column(Integer, unique = True, nullable = False)
    hyperdrive_rating = Column(Integer, unique = True, nullable = False)
    MGLT = Column(Integer, unique = True, nullable = False)
    cargo_capacity = Column(Integer, unique = True, nullable = False)
    consumables = Column(String, unique = True, nullable = False)
    pilots = Column(String, unique = True, nullable = False)
    created = Column(Integer, unique = True, nullable = False)
    edited = Column(String, unique = True, nullable = False)
    favoriteID = Column(Integer, ForeignKey('favorite.favoriteID'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')