-- This helps to list the score and name
-- The orders them from highest to lowest
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
