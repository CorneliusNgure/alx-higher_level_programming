-- Retrieves the ID and name of cities along with the corrsponding state names
SELECT cities.id AS c_id, cities.name AS c_name, states.name AS s
FROM cities
-- Joins the cities table with the states table on the state_id column
JOIN states ON cities.state_id = states.id
-- Sorts the results by city ID in ascending order.
ORDER BY cities.id ASC;
