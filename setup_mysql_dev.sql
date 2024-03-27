-- Creating a database hbnb_dev_db and a user hbnb_dev with specific privileges.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
ALTER USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
