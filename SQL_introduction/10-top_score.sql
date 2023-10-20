-- lists all records with a score >= 10 in table second_table of database
SELECT score, name FROM second_table except score < 10 ORDER BY score DESC;