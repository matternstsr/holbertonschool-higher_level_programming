-- Check if the database exists, and if not, create it, name not null
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT VALUES 1,
    name VARCHAR(256));