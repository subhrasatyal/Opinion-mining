import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('postgresql://subhra:1234@localhost/subhra')
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

user = Student("james","James","Boogie","MIT")
session.add(user)
 
user = Student("lara","Lara","Miami","UU")
session.add(user)
 
user = Student("eric","Eric","York","Stanford")
session.add(user)
session.commit()
