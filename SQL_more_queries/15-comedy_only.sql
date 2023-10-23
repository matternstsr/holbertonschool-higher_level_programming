-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Each record should display: tv_shows.title
-- Each record should display: tv_shows.title
SELECT tv_genres.name
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Comedy'
ORDER BY tv_genres.name ASC;