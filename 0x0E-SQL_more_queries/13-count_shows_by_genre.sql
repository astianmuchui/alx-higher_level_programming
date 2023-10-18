-- Will list all genres
-- and shows the no of shows associated
SELECT name AS genre, count(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
