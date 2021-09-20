Tutorial Link:
https://towardsdatascience.com/getting-started-with-apache-cassandra-and-python-81e00ccf17c9
https://www.tutorialspoint.com/python_data_persistence/python_data_persistence_cassandra_driver.htm

CQL Docs:
https://cassandra.apache.org/doc/latest/cql/

Setup Commands

1) created two folders to store data. we will have two nodes in our db so i created node1 and node2

2) `docker pull cassandra`

3) Get your current working directory with `pwd`. Copy the path. You'll need to paste it in the next couple commands.

4) docker run --name cas1 -p 9042:9042 -v /[CURRENT_PATH_HERE]/node1:/var/lib/cassandra/data -e CASSANDRA_CLUSTER_NAME=MyCluster -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra:latest

5) `docker exec -it cas1 nodetool status` to look into the status of this new node.

6) Check out cassandra docs and look into the details about the status of this datacenter. Snitches and statuses (i.e. UN vs UJ) to understand how nodes communicate with one another.

7) docker run --name cas2 -v /[CURRENT_PATH_HERE]/node2:/var/lib/cassandra/data -e CASSANDRA_SEEDS="$(docker inspect --format='{{ .NetworkSettings.IPAddress }}' cas1)" -e CASSANDRA_CLUSTER_NAME=MyCluster -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra:latest

8) `docker exec -it cas1 nodetool status` to check out the status of this new node connecting to the other node.

9) Create a docker compose file. Copy paste the contents of this docker-compose file into your own file of the same name. Make sure to update the volume with your current path from the previous steps.

10) Run the `docker-compose up -d` to run in detached mode.

11) Create a virtual environment. Do this with `python3 -m venv env` or similar command. Activate it with `. env/bin/activate` or similar (windows is slightly different but i forget). Run pip3 install cassandra-driver.

12) Copy paste the contents of the `cass.py` file into your own file.

CQL Commands

0) docker exec -it cas2 cqlsh

1)
USE mykeyspace;

2)
CREATE TABLE cities (
 id int,
 name text,
 country text,
 PRIMARY KEY(id)
);

3)
CREATE TABLE users (
 username text,
 name text,
 age int,
 PRIMARY KEY(username)
);

4)
INSERT INTO cities(id,name,country) VALUES (1,'Karachi','Pakistan');
INSERT INTO cities(id,name,country) VALUES (2,'Lahore','Pakistan');
INSERT INTO cities(id,name,country) VALUES (3,'Dubai','UAE');
INSERT INTO cities(id,name,country) VALUES (4,'Berlin','Germany');

5)
INSERT INTO users(username,name,age) VALUES ('aali24','Ali Amin',34);
INSERT INTO users(username,name,age) VALUES ('jack01','Jack David',23);
INSERT INTO users(username,name,age) VALUES ('ninopk','Nina Rehman',34);

6)
CREATE TABLE users_by_cities (
 username text,
 name text,
 city text,
 age int,
 PRIMARY KEY(city,age)
);

7)
INSERT INTO users_by_cities(username,name,city,age) VALUES ('aali24','Ali Amin','Karachi',34);
INSERT INTO users_by_cities(username,name,city, age) VALUES ('jack01','Jack David','Berlin',23);
INSERT INTO users_by_cities(username,name,city, age) VALUES ('ninopk','Nina Rehman','Lahore',34);

Running it

1) python3 cass.py