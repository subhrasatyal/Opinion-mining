import sqlalchemy
def connect(user, password, db, host='localhost', port=5432):
#ret a connection obj and metadata obj
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    meta = sqlalchemy.MetaData(blind=con, reflect=True)

    return con, meta
    #con, meta = connect('zomato', 'zomatoreviews', 'reviews')
    
    Engine(postgresql://zomato:***@localhost:5432/reviews)
    
    MetaData(bind=Engine(postgresql://zomato:***@localhost:5432/reviews))
from sqlalchemy import Table, Column, Integer, String, MetaData
name = Table('name', meta,
    Column('name', String),
    Column('review', String),
    Column('rating', Integer, primary_key=True)
)

meta.create_all(con)


    
