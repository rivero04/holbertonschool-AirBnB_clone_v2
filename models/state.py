#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Representation of state """
    if storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    if storage_type != "db":
        @property
        def cities(self):
            """Getter for a list of city instances associated with the state"""
            from models.city import City
            cities = []
            all_cities = storage_type.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
