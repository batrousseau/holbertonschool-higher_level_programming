-- create unique_id_table

CREATE TABLE IF NOT EXISTS unique_id(
    id INTEGER UNIQUE DEFAULT 1 ,
    name VARCHAR(256)
);