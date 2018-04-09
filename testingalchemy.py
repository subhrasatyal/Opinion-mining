
from sqlalchemy import create_engine, MetaData, Table
engine = create_engine('mysql://subhra:anything@localhost:5432/yelp_db')
engine.echo = False
connection = engine.connect()
metadata = MetaData(engine)
review = Table('review', metadata, autoload_with=engine)
s = review.select().order_by(func.rand()).limit(20)
rs = s.execute()
row = rs.fetchone()
print 'id:', row[0]
print 'text:', row['text']
print 'date:', row.date
for row in rs:
    print row.id, 'has written the review', row.text, 'on date', row.date
def main():
  print("2o reviews by date")
  
if __name__== "__main__":
  main()

print("Reviews")


