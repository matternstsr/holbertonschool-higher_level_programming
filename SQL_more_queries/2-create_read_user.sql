-- Check if the database exists, and if not, create it
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user exists, and if not, create the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to the user on the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';