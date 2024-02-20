-- Lists all shows in the hbtn_0d_tvshows database that have at least one genere linked
-- Sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
