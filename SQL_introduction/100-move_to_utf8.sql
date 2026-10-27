-- converts the database to UTF8

ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4;

ALTER TABLE first_table
CHARACTER SET utf8mb4;

ALTER TABLE first_table
MODIFY name
CHARACTER SET utf8mb4;