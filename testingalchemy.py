from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql.expression import func, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql://subhra:anything@localhost:5432/yelp_db?charset=utf8')
engine.echo = True
Base = declarative_base()
connection = engine.connect()
metadata = MetaData(engine)
review = Table('review', metadata, autoload_with=engine)

metadata.reflect(engine, only=['review'])


class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    business_id = Column(Integer, nullable=False)
    user_id = Column(String(20), nullable=False)
    stars = Column(Integer, nullable=True)
    date = Column(String(20), nullable=True)
    text = Column(String, nullable=True)
    useful = Column(Integer, nullable=True)
    funny = Column(Integer, nullable=True)
    cool = Column(Integer, nullable=True)
    
    def __init__(self, text='Warm ambience'):
        self.text = text

def loadSession():
    # create session
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()


def Main():
    def __init__(self):
        pass
    def run(self):
        s = review.select().order_by(func.rand()).limit(20)
        row = rs.fetchall()
        rs = s.execute()
        print 'id:', row[0]
        print 'text:', row['text']
        print 'date:', row.date
        for row in rs:
           print row.id, 'has written the review', row.text, 'on date', row.date
  
if __name__== '__main__':
    session = loadSession()
    
   # rs = session.query(reviews).all()
    Main()
    connection.close()

