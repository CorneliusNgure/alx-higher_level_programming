-- Lists the no. of records with the same score in 'second_table'
-- Records displayed in descending order

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
