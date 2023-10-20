-- Check if the database exists, and if not, create it, name not null
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256) CHECK (name IS NOT NULL);