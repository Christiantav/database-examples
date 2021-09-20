Original Tutorial Link
https://pymongo.readthedocs.io/en/stable/tutorial.html

1) Run a mongo container in the latest version of mongodb called "mongod" on port 27017
`docker run -d -p 27017:27017 --name mongod mongo:latest`

2) Create a venv in your folder with `pip3 -m venv env`

3) Start the virtual environment with `. env/bin/activate` on mac and that other command for windows, it might be `source ./env/bin/activate` idk

4) `pip install pymongo` in your virtual environment terminal

5) mongodb instances can support multiple databases. Let's access them with dict[key] format. (i.e. `db = client["db-name"]`)

6) Collections are loosely similar to tables on a db. Tables store rows formatted by columns, whereas collections store documents. Since this is nosql, we can format our data however we want without the constraint of columns. We can access them through the database from previous example with the same dict[key] format (i.e. `collection = db["test-collection"]`)

7) Data in mongo is stored in json style objects. We can use dictionaries here. The following would represent a user which falls in line with the types of structures we've been creating for our db_experiments.

import datetime
user = {
  "username": "user123",
  "first_name": "Jane",
  "last_name": "Doe",
  "phone": "123-456-7890",
  "birthday": "12/31/1999",
  "created_at": datetime.datetime.utcnow(),
}

8) Documents can contain Python types like datetime above, which will be automatically converted to the appropriate BSON types that mongodb will store it in.

9) Let's insert a single user document into our user collection using "insert_one()"
users = db["users"]
user_id = users.insert_one(user).inserted_id
user_id

10) A "special key" of "_id", is automatically added if the document object doesn’t already contain an "_id" key. The "_id" is much like a primary key and therefore must be unique in the collection of documents.

11) The "users" collection is automatically created by the server after the above command. Check that:
db.list_collection_names()

12) Let's query for a single document using "find_one()". This would be useful for finding a single document based on a unique attribute, or if you want to find the most recent insertion that satisfies the query.
print(users.find_one({"user": "user123"}))

13) SOMEONE ELSE DO THE REST OF THIS.