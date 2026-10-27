-- group the city and orders them by their averaging temperature

SELECT city, AVG(value) AS avg_temp
FROM hbtn_0c_0.temperatures
GROUP BY city
ORDER BY avg_temp DESC;