#!/usr/bin/python3
"""This is DBStorage module"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class DBStorage:
    """
    This class manages storage of hbnb models
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Create the engine and session"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}:"
            f"{getenv('HBNB_MYSQL_PWD')}@"
            f"{getenv('HBNB_MYSQL_HOST')}/"
            f"{getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """ Retrives all objects in the current session
        """
        classes = [User, State, City, Amenity, Place, Review]
        new_dict = {}

        if cls is None:
            for obj in classes:
                for obj in self.__session.query(obj).all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
            return new_dict
        else:
            for obj in self.__session.query(cls).all():
                key = f"{cls.__name__}.{obj.id}"
                new_dict[key] = obj
            return new_dict

    def new(self, obj):
        """ Adds the given object to the
        current session.
        """
        self.__session.add(obj)

    def save(self):
        """"Saves the object to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the database schema and establishes a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
