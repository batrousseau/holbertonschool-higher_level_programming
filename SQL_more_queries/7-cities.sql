-- creates a database and the table cities, working with differents constraints for each field

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    state_id INTEGER NOT NULL,
    name VARCHAR(256) NOT NULL,

    CONSTRAINT fk_state_id
        FOREIGN KEY (state_id)
        REFERENCES states(id)
);