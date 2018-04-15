from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql.expression import func, select

engine = create_engine('mysql://subhra:anything@localhost:5432/yelp_db')
engine.echo = True
connection = engine.connect()
metadata = MetaData(engine)
review = Table('review', metadata, autoload_with=engine)

class review(object):
    pass
def loadSession():
mapper(reviews, review)

Session = sessionmaker(bind=engine)
session = Session()
return session

def main():
  print("20 reviews by date")
s = review.select().order_by(func.rand()).limit(20)
rs = s.execute()
row = rs.fetchall()
print 'id:', row[0]
print 'text:', row['text']
print 'date:', row.date
for row in rs:
    print row.id, 'has written the review', row.text, 'on date', row.date
  
if __name__== "__main__":
    session = loadSession()
    rs = session.query(reviews).all()
    main()

