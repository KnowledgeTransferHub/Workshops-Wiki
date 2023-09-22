CREATE TABLE users (
    id serial PRIMARY KEY,
    username VARCHAR (80) UNIQUE NOT NULL,
    password VARCHAR (80) NOT NULL
);
