-- Create database named udemy-clone, IF NOT EXISTS
CREATE DATABASE IF NOT EXISTS udemy_clone;

-- Create a table named course, with fields:
-- id: auto_increment, int, primary key
-- name - varchar(255)
-- description - varchar(255)
-- image_url - varchar(255)
-- price - int
-- rating - int
CREATE TABLE IF NOT EXISTS Courses (
    ID int NOT NULL AUTO_INCREMENT,
    Name varchar(255) NOT NULL,
    Description varchar(255),
    Image_url varchar(255),
    Price int NOT NULL,
    Rating int,
    PRIMARY KEY (ID)
);
