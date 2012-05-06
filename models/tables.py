# -*- coding: utf-8 -*-


from models import metadata
import models as m
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from werkzeug.datastructures import CallbackDict
from flask import json

user              = Table("user", metadata, autoload=True)
loginlog          = Table("loginlog", metadata, autoload=True)
image             = Table("loginlog", metadata, autoload=True)
activity          = Table("activity", metadata, autoload=True)
discuss           = Table("discuss", metadata, autoload=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(metadata=metadata)
Base.query = m.session.query_property()
    
class User(Base):
    __table__ = user  
          
    @property
    def votingnum(self):
        return 1
            
    
class Loginlog(Base):
    __table__ = loginlog
    
class Image(Base):
    __table__ = image

class Activity(Base):
    __table__ = activity
    
class Discuss(Base):
    __table__ = discuss