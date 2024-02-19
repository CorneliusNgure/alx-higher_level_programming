-- Retrieves the ID and name of cities along with the corrsponding state names
SELECT cities.id AS id, cities.name AS name, states.name AS state_name FROM cities
-- Joins the cities table with the states table on the state_id column
JOIN states ON cities.state_id = states.id
-- Sorts the results by city ID in ascending order.
ORDER BY cities.id ASC;
