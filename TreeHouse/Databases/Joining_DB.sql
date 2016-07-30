#USE treehouse_movie_db;

#	Creates table 
#CREATE TABLE genres (id INTEGER, name VARCHAR(30));
#CREATE TABLE genres (id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(30) NOT NULL UNIQUE KEY);

#	Insert
#INSERT INTO genres (name) values('Sci Fi');
#INSERT INTO genres (name) values('Musical');
#INSERT INTO genres (name) values('Action');

#	View
#SELECT * FROM genres;

#	Alter Table
#ALTER TABLE movie ADD COLUMN id INTEGER AUTO_INCREMENT PRIMARY KEY FIRST;
#ALTER TABLE movie 
#ADD COLUMN genere_id INTEGER NULL,
#ADD CONTRAINT foreign KEY (genre_id) REFRENCES (genre_id);


#	Join
#SELECT * FROM movies JOIN genres ON movies.genre_id = genres.id;
#	Inner Join - joins sections in common with both groups
#SELECT * FROM movies INNER JOIN genres ON movies.genre_id = genres.id;
#	Outer Left Join - views items in left table and the inner join
#SELECT * FROM movies LEFT OUTER JOIN genres ON movies.genre_id = genres.id;
#	Outer Right Join - views litems in right table and the inner join
#SELECT * FROM movies RIGHT OUTER JOIN genres ON movies.genre_id = genres.id;

#	Altering
# 	Bring back name and genre name from the tables
# 	This will change the name that we see in the results for the column, but will not change schemas
#SELECT movies.title AS movie_title, genres.name AS genres_name 
#FROM movies LEFT OUTER JOIN genres 
#ON movies.genre_id = genres.id;
#	With Conditions - alysis can not be called on. Must use their original name
#SELECT movies.title AS movie_title, genres.name AS genere_name
#FROM movies LEFT OUTER JOIN genres
#ON movies.genre_id = genres.id
#WHERE name IS NOT NULL;


















