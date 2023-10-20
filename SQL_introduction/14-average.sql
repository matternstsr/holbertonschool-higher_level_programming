-- select the avg from table of score
SELECT score, avg(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;