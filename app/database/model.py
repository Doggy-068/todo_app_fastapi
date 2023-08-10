from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_complete = Column(Boolean)


class Continent(Base):
    __tablename__ = 'continents'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column()

    countries = relationship('Country', back_populates='continent')


class Country(Base):
    __tablename__ = 'countries'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column()
    continent_id: Mapped[int] = mapped_column(ForeignKey('continents.id'))

    continent = relationship('Continent', back_populates='countries')
    cities = relationship('City', back_populates='country')


class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column()
    country_id: Mapped[int] = mapped_column(ForeignKey('countries.id'))

    country = relationship('Country', back_populates='cities')
