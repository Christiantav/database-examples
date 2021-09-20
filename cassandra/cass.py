from cassandra.cluster import Cluster


cluster = Cluster(['0.0.0.0'],port=9042)
session = cluster.connect('mykeyspace',wait_for_all_pools=True)
session.execute('USE mykeyspace')

username = input("Please enter a username: ")
name = input("Please enter a name: ")
age = input("Please enter an age: ")

session.execute(f"insert into users (username, name, age) values  (1, {username}, {name}, {age});")

rows = session.execute('SELECT * FROM users')
for row in rows:
    print(row.age,row.name,row.username)
