from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Boolean
from sqlalchemy.ext.automap import automap_base

engine = create_engine('mysql://subhra:anything@localhost:5432/yelp_db?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
#creating a user model
class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    business_id = Column(Integer, nullable=False)
    user_id = Column(String(20), nullable=False)
    stars = Column(Integer, nullable=True)
    date = Column(String(20), nullable=True)
    text = Column(String(70), nullable=True)
    useful = Column(Integer, nullable=True)
    funny = Column(Integer, nullable=True)
    cool = Column(Integer, nullable=True)
#create the table
Base.metadata.create_all(engine)
#inserting data
rr_review = Review(review_id='123456') #123456 is a an id I am adding
#adding to session
session.add(rr_review)
session.commit()
print(rr_review.review_id)
#querying
review = session.query(Review).all()
print(review)
#particular attribute
print(session.query(Review.review_id.first())



                                         

