# creating a table
use movie_db_1;

# creates a table
# not null makes it to where we have to fill in the name on the table
# create table actors (name VARCHAR(50) not null);
# create table movies (title varchar(200) not null, year integer null) engine = InnoDB;

# read
# if you know the order of the colums
# insert into movies values ('Avatar', 2009);
# if you do not know the order of the columns
# insert into movies (title, year) values ('Avatar', 2009);
# insert more than one at a time
# note that the everything must follow the same order as the first set of ordres 
# insert into movies (title, year) values ('Avatar', 2009), ('Avatar 2', null);
# import using set
# insert into movies set title = 'Back to the Future', year = 1985;

# updatng
# update movies set year = 2015 where title = 'Avatar 2';
# update movies set year = 2016, title = 'Avatar Reloaded' where title = 'Avatar 2';

# delete
# dont do this one as it will delete everyhting from the table
# delete from movies;
delete from movies where title = 'Avatar Reloaded' and year = 2016