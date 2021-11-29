CREATE DATABASE translation;
CREATE USER 'translator'@'localhost' IDENTIFIED BY 'translator#123';
GRANT ALL PRIVILEGES ON translation.* TO 'translator'@'localhost';
