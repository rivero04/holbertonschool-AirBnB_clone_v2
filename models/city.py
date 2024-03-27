#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.state import State
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
    """Representation of city """
    if models.storage_type == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        state_id = ""
        name = ""
