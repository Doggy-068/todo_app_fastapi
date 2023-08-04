from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_complete = Column(Boolean)


class Continent(Base):
    __tablename__ = 'continents'

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)

    countries = relationship('Country', back_populates='continent')


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    continent_id = Column(Integer, ForeignKey('continents.id'))

    continent = relationship('Continent', back_populates='countries')
    cities = relationship('City', back_populates='country')


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    country_id = Column(Integer, ForeignKey('countries.id'))

    country = relationship('Country', back_populates='cities')
