#use treehouse_movie_db

#user1 - read only
#	.* - is a wild card for all the tables in the db
#	@'%' - means that the specified user can use it where they are at, if you would like them 
#		to have limited access to it from location then you will need to spedify that in the ''. 
#grant select
#on treehouse_movie_db.*
#to user1@'%'
#identified by '123';

# 	Flush privileges - must do this, otherwise you wont be able to connect
#flush privileges;



#user2 - CRUD
#grant select, insert, update, delete
#on treehouse_movie_db.*
#to user2@'%'
#identified by '123';

#flush privileges;



#user3 - DDL
#grant alter, create, drop
#on treehouse_movie_db.*
#to user3@'%'
#identified by '123';

#flush privileges;