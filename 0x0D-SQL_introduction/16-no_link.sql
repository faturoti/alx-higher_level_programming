-- This would select all names except those that have name to be null
-- and prints them
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
