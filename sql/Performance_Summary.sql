CREATE TABLE performance_summary (
    student_id INT,
    name VARCHAR(100),
    average_marks FLOAT,
    attendance_percentage FLOAT,
    performance VARCHAR(50)
);

ALTER TABLE performance_summary
DROP COLUMN name;

SELECT *
FROM performance_summary;
