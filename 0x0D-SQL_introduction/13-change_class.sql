-- removes all records with a score with less or equal 5 of a table
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
