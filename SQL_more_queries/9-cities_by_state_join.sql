-- lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement

USE hbtn_0d_usa;

SELECT city.id, city.name, state.name
FROM cities AS city
JOIN states as state ON city.state_id = state.id
ORDER BY city.id ASC;