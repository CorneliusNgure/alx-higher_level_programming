-- Switch to the hbtn_0c_0 database and convert the table to UTF8
USE hbtn_0c_0;

-- Convert table and its field to UTF8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
