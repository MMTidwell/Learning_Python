# INDEXING - improves preformence when reading/serching for info from a specific column
#	Kind of like a index in a book

#	Finding a specific user, took 0.000 sec due to only 3 useres in the list
#SELECT * FROM users WHERE last_name = 'Chalkley';
#	Shoews us how it is searching for the info
#EXPLAIN SELECT * FROM users WHERE last_name = 'Chalkley';

#	Creates an index
#CREATE INDEX last_name_idx ON users(last_name);
#SELECT * FROM users WHERE last_name = 'Chalkley';
#	Used index to search for cirteria 
#EXPLAIN SELECT * FROM users WHERE last_name = 'Chalkley';

# 	Add a new user to the db
#INSERT INTO users (username, email, first_name, last_name)
#VALUES ('Henry', 'henry@email.com', 'Henry', 'Chalkley');

#EXPLAIN SELECT * FROM users WHERE last_name = 'Chalkley';
#EXPLAIN SELECT * FROM users WHERE first_name = 'Andrew' AND last_name = 'Chalkley';


#					Setting up multiple users for your db
#	Permisions for db - Write, Read, Modify Schema
# 	Useres that we are going to create:
#		user1 = read
#		user2 = read and write
#		user3 = modify schema

#	Steps
#		Home
#		Under MySQL connections click on box named local in the upper right corner of box
#		Connection name = 'Admin for remote db'
#		Hostname = '192.168.1033' (an ip address) 
#		Root = Admin
#		Enter password
#		Test connection
#		Close

#	In the admin conncection you will specify the username, permissions, and password

