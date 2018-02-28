import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('postgresql://subhra:1234@localhost/subhra')
connection = engine.connect()
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create objects  
for student in session.query(Student).order_by(Student.id):
    print student.firstname, student.lastname
