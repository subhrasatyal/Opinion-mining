from sqlalchemy import *
from sqlalchemy import create_engine
engine = create_engine('mysql://subhra:anything@localhost:5432/yelp_db')
engine.echo = False
connection = engine.connect()
metadata = MetaData(engine)
review = Table('review', metadata, autoload=True)
s = review.select()
rs = s.execute()
row = rs.fetchone()
print 'id:', row[0]
print 'text:', row['text']
print 'date:', row.date
for row in rs:
    print row.id, 'has written the review', row.text, 'on date', row.date



