-- Lists all records with score >= 10
-- in the 'second_table' in descendng order

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
