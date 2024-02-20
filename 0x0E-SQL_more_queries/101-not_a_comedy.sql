-- Lists all shows without the genre Comedy

SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN (
    SELECT tsg.show_id
    FROM tv_show_genres tsg
    JOIN tv_genres tg ON tsg.genre_id = tg.id
    WHERE tg.name = 'Comedy'
)
ORDER BY ts.title ASC;
