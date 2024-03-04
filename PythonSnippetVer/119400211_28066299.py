from cassandra.query import dict_factory
session = cluster.connect('mykeyspace')
session.row_factory = dict_factory
rows = session.execute("SELECT name, age FROM users LIMIT 1")
print rows[0]
{u'age': 42, u'name': u'Bob'}