-- lists all records of a table in sorted order
SELECT score, name FROM second_table WHERE CHAR_LENGTH(name) > 0 ORDER BY score DESC;
