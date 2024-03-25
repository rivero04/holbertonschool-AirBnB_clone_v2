#!/usr/bin/python3
""" DBStorage Module for HBNB project """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base


class DBStorage:
    """ Interact with the database """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the engine and session """
        user = os.getenv('HBNB_MYSQL_USER', 'hbnb_dev')
        pwd = os.getenv('HBNB_MYSQL_PWD', 'hbnb_dev_db')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB', 'hbnb_dev')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = session_factory()

    def all(self, cls=None):
        """ Query on current db session """
        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        
        classes = {'City': City, 'State': State,
                     'User': User, 'Place': Place,
                     'Review': Review, 'Amenity': Amenity}
        
        objects = {}
        
        session = self.__session
        if cls is None:
            for name_class in classes:
                data = session.query(classes[name_class]).all()
                for obj in data:
                    objects["{}.{}".format(obj.__class__.__name__,
                                           obj.id)] = obj
        else:
            if isinstance(cls, str):
                cls = classes[cls]
            data = self.__session.query(cls).all()
            for obj in data:
                objects["{}".format(obj.id)] = obj
        return objects

    def new(self, obj):
        """ Add an object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes to the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete an object from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and create the current database session """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = session_factory()
