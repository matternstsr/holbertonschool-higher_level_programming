-- select the count from table of score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;