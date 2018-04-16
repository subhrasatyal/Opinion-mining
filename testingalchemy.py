from sqlalchemy import create_engine, MetaData, Table, Column, Integer
from sqlalchemy.orm import mapper
from sqlalchemy.sql.expression import func, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.automap import automap_base

engine = create_engine('mysql://subhra:anything@localhost:5432/yelp_db')
engine.echo = True
Base = declarative_base()
#Base = automap_base()
connection = engine.connect()
metadata = MetaData(engine)
review = Table('review', metadata, autoload_with=engine)

metadata.reflect(engine, only=['review']

#Table('review', metadata,
 #              Column('id', Integer, primary_key=True),
  #              Column('user_id', ForeignKey('user.id'))
   #         )


Base = automap_base(metadata=metadata)
Base.prepare()

class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)

def loadSession():
    mapper(reviews, review)
    
    session = Session(engine)
    session.commit()

def main():
    print("20 reviews by date")
    s = review.select().order_by(func.rand()).limit(20)
    row = rs.fetchall()
    print 'id:', row[0]
    print 'text:', row['text']
    print 'date:', row.date
    for row in rs:
        print row.id, 'has written the review', row.text, 'on date', row.date
  
if __name__== "__main__":
    session = loadSession()
    rs = s.execute()
   # rs = session.query(reviews).all()
    main()

