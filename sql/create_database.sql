CREATE DATABASE student_pipeline;

USE student_pipeline;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    school VARCHAR(10),
    sex VARCHAR(5),
    age INT,
    address VARCHAR(10),
    famsize VARCHAR(10),
    Pstatus VARCHAR(10),
    Medu INT,
    Fedu INT,
    Mjob VARCHAR(50),
    Fjob VARCHAR(50)
);

CREATE TABLE scores (
    score_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    G1 INT,
    G2 INT,
    G3 INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
     absences INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

SELECT * FROM students;
SELECT * FROM scores;
SELECT * FROM attendance;

drop table scores;
drop table attendance;
drop table students;