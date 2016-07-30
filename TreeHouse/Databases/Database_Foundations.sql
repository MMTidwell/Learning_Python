SELECT movies.title, movies.year FROM movies;
SELECT * FROM movies;
SELECT movies.year, movies.title FROM movies;
SELECT year, title FROM movies;
SELECT title, year FROM movies;
SELECT title FROM movies;

# note the single = when searching specifics in the rows
SELECT * FROM movies WHERE year = 1999;
SELECT * FROM movies WHERE year != 1999;
SELECT * FROM movies WHERE year > 1999;
SELECT * FROM movies WHERE year >= 1999;
SELECT * FROM movies WHERE year < 1999;
SELECT * FROM movies WHERE year <= 1999;

# Can use both ' or "
SELECT * FROM movies WHERE year = 1999 AND title = 'The Matrix';
SELECT * FROM movies WHERE year = 1998 OR year = 2000;
SELECT * FROM movies WHERE year BETWEEN 1998 AND 2000;
SELECT * FROM movies WHERE title LIKE '%godfather';
SELECT * FROM movies WHERE title LIKE '%godfather%';

select * from movies order by year;
select * from movies order by year desc;
select * from movies order by year asc;
select * from movies order by year asc, title desc;

select * from movies limit 10;
select * from movies limit 10 offset 1;
select * from movies limit 10 offset 0;
select * from movies limit 10 offset 10;
select * from movies limit 10 offset 250;
# this is the same as above, just shorter syntax
select * from movies limit 20, 10;

select * from movies where year is null;
select * from movies order by year;
select * from movies where year is not null order by year;


