from sqlalchemy import create_engine, MetaData, Table, select, text, distinct
from sqlalchemy import inspect

engine = create_engine('sqlite:///census.sqlite')

inspector = inspect(engine)
table_names = inspector.get_table_names()

metadata = MetaData()
census = Table('census', metadata, autoload_with=engine)

connection = engine.connect()

stmt = select(distinct(census.c.state))
results = connection.execute(stmt).fetchall()
print(results)

stmt = text('SELECT SUM(pop2000), SUM(pop2008), state FROM census '
            'WHERE state IN("Alaska", "New York") '
            'GROUP BY state ')
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()
print(results)

stmt = text('SELECT SUM(pop2008), state, sex FROM census '
            'WHERE state = "New York" '
            'GROUP BY state, sex ')
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()

print(results)

