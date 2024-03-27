#!/usr/bin/python3
""" State Module for HBNB project """
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'

    if models.storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    if models.storage_type != "db":
        @property
        def cities(self):
            """Getter for a list of city instances associated with the state"""
            from models.city import City
            cities = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
