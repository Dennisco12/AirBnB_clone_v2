#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os

all_classes = {
        'State': State, 'City': City, 'User': User,
        'Place': Place, 'Review': Review, 'Amenity': Amenity}


class DBStorage:
    """This class manages db storage of hbnb models using SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the SQLAlchemy engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        # drop tables if enviroment in test mode
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects by class or just everything"""
        obj_dict = {}

        if cls:
            for row in self.__session.query(cls).all():
                obj_dict.update({'{}.{}'.format(type(cls).__name__,
                                row.id,): row})
        else:
            for key, val in all_classes.items():
                for row in self.__session.query(val):
                    obj_dict.update({'{}.{}'.format(type(row).__name__,
                                    row.id,): row})
        return obj_dict

    def new(self, obj):
        """ add a new element in the table """
        self.__session.add(obj)

    def save(self):
        """ save changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete an element in the table """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload configuration """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ closes sqlalchemy session """
        self.__session.close()
