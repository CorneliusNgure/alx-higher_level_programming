-- Displays the avg temperature by city ordered by
-- temperature(descending)

SELECT city,
    AVG(temperature_fahrenheit) AS average_temperature_fahrenheit
FROM (
    SELECT city,
        CASE
            WHEN (MIN(value) >= -459.67 AND MAX(value) <= 212) THEN AVG(value)  -- Fahrenheit, directly take the average
            ELSE AVG((value * 9 / 5) + 32)  -- Convert Celsius to Fahrenheit and then take the average
        END AS temperature_fahrenheit
    FROM temperatures
    GROUP BY city
) AS city_temperatures
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
