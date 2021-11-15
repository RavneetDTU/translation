CREATE DATABASE translation;
CREATE USER 'translator'@'localhost' IDENTIFIED BY 'translator@124#N';
GRANT ALL PRIVILEGES ON translation.* TO 'translator'@'localhost';
