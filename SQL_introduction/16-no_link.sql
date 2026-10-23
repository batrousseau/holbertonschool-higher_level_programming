-- list all recordsin descending order without name as null

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER by score DESC;
