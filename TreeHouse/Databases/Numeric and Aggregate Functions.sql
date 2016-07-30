#	Allows us to view the first time in the movies table
#SELECT * FROM movies LIMIT 1;

#	Allows us to view all movie_id's that are 1 in the reviews table
#SELECT * FROM reviews WHERE movie_id = 1;

#	How many review there are 
#	The permamiters after count dont really matter as it will still count
#SELECT COUNT(*) FROM reviews WHERE movie_id = 1;
#SELECT COUNT(id) AS reivew_count FROM reviews WHERE movie_id = 1;

#	Minimum fucntion
#SELECT MIN(score) AS min_score FROM reviews WHERE movie_id = 1;

#	Maximum function
#SELECT MIN(score) AS min_score, MAX(score) AS max_score FROM reviews WHERE movie_id = 1;

#	Sum function
#SELECT MIN(score) AS min_score, MAX(score) AS max_score, SUM(score) AS sum_score
#FROM reviews WHERE movie_id = 1;

#	Average function
#	Long way:
#SELECT MIN(score) AS min, MAX(score) AS max, SUM(score) / COUNT(score) AS sum
#FROM reviews WHERE movie_id = 1;
#	Short way:
#SELECT MIN(score) AS min, MAX(score) AS max, AVG(score) as avg
#FROM reviews WHERE movie_id = 1;
#	Even shorter way:
#SELECT AVG(score) FROM reviews WHERE movie_id = 1;
#	Average all scores for all movies:
#SELECT AVG(score) FROM reviews;

#	Group movies together by movie_id (this will not return null items since we pulled inner join)
#SELECT title, MIN(score) AS min,
#MAX(score) AS max,
#AVG(score) AS avg
#FROM movies JOIN reviews
#ON movies.id = reviews.movie_id
#GROUP BY movie_id;

#	Group movies together by movie_id including null)
#SELECT title, min(score) AS min,
#MAX(score) AS max,
#AVG(score) AS avg
#FROM movies LEFT OUTER JOIN reviews
#ON movies.id = reviews.movie_id
#GROUP BY movie_id;

#	If null function - this will give a 0 avg for a null value. A lot of places can not work with null values
#SELECT title, MIN(score) AS MIN,
#MAX(score) AS max,
#IFNULL(AVG(score), 0) AS avg
#FROM movies LEFT OUTER JOIN reviews
#ON movies.id = reviews.movie_id
#GROUP BY movie_id;

#	Having - creates a filter for avg
#SELECT title, MIN(score) AS MIN,
#MAX(score) AS max,
#IFNULL(AVG(score), 0) AS average
#FROM movies LEFT OUTER JOIN reviews
#ON movies.id = reviews.movie_id
#GROUP BY movie_id HAVING average > 3;

#	String Function
#	Shows id, username, email, first and last names
#SELECT * FROM users;
#SELECT first_name, last_name, email FROM users;

#	Lower function (works the same way as .lower() in python)
#SELECT first_name, last_name, LOWER(email) FROM users;

#	Upper Case Function (works like .upper() in python)
#select first_name, upper(last_name), lower(email) from users;

# 	Finding the length of user name and calling up emails matching the shorter username length
#select first_name, upper(last_name), lower(email), length (username) 
#as username_length 
#from users;

# 	Just like above but using HAVING
#select first_name, upper(last_name), lower(email), length (username) 
#as username_length 
#from users having username_length < 19;

#	Join 2 or more strings together (this will also take away the ' ' if not added)
#select concat(first_name, ' ', upper(last_name)), lower(email), length (username) 
#as username_length 
#from users having username_length < 19;

#	Substring Method - shows only what you allow it to show
#select concat(first_name, ' ', upper(last_name)) as full_name, 
#concat(substring(lower(email), 1, 10), '...') as partial_email,
#length (username) 
#as username_length 
#from users having username_length < 19;
