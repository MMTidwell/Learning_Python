use movie_db_1;

# RENAME TABLE
# rename table movies to movie_table, actors to actor_ables;

# DELETE TABLE
# drop deletes table to where it no longer exists
# drop table reviews; 		# fails due to no table called reivews
drop table if exists reviews; 			# throws warning since there is no reviews table
# truncate removes all the data from the table w/o perminitly deleting the data
# truncate table movie_table;			# this will delete the whole table
truncate actor_table;


# ALTERING COLUMNS
# alter table movie_table add column genre varchar(100);
# alter table actor_table add (pob varchar(100), dob date);
# alter table actor_table change column pob place_of_bearth varchar(100);
# alter table actor_table change column dob date_of_birth date;
 alter table actor_table change year year_released year;

# REMOVE COLUMNS
# alter table actor_table drop date_of_birth;
