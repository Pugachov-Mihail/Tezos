from sqlalchemy import Integer, Column, Text,\
    create_engine, select, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker


metadata = MetaData()
engine = create_engine("sqlite:///sqlite3.db")

user = Table('user', metadata,
             Column('id',Integer(), primary_key=True),
             Column('data', Text(),nullable=True)
             )

metadata.create_all(engine)


def read(table):
    conn = engine.connect()
    sel = select([table])
    re = conn.execute(sel)
    data = re.fetchone()
    print(data['data'])
    return str(data['data'])

def write(data):
    conn = engine.connect()
    conn.execute(data)
