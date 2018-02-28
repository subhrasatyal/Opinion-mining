from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('postgresql://subhra:1234@localhost/subhra')
connection = engine.connect()

Base = declarative_base()
class Student(Base):
    def __init__(self, username, firstname, lastname, university):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.university = university	
    
    __tablename__ = "student"
 
    id = Column(Integer, primary_key=True) # true is for auto inc
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    university = Column(String)

Base.metadata.create_all(engine)
