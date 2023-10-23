-- Import the database dump from hbtn_0d_tvshows to your 
-- MySQL server: download (same as 11-genre_id_all_shows.sql)
-- Write a script that lists all shows contained in 
-- hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement

SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_shows.title - tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;