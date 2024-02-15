-- Displays the top 3 of the city's temp during July and August
-- ordered by city in descending order

SELECT city,
       AVG(value) AS average_temperature
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY average_temperature DESC
LIMIT 3;
