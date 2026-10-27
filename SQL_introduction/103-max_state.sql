-- display de max temperature for each state

SELECT state, MAX(VALUE) AS max_temp
FROM temperatures
GROUP by state
ORDER BY state ASC;
