-- Lists all records of 'second_table'
-- Rows will not be displayed without 'name' value
-- Records will be displaye in descending order

SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
