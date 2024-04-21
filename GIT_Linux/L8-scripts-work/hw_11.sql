-- 1. Подключитесь к базе данных Students (которая находится на удаленном сервере). 
USE Students;

-- 2. Найдите самого старшего студента
SELECT name, MAX(age) AS max_age
FROM Students;

SELECT
name,
age
FROM Students
ORDER BY age DESC
LIMIT 1;

-- 3. Найдите самого старшего преподавателя
SELECT name, MAX(age) AS max_age
FROM Teachers;

SELECT
name,
age
FROM Teachers
ORDER BY age DESC
LIMIT 1;

-- 4. Выведите список преподавателей с количеством компетенций у каждого
-- SELECT * FROM Teachers;
-- SELECT * FROM Teachers2Competencies;
-- SELECT * FROM Competencies;


SELECT Teachers.name AS Teacher, COUNT(Teachers2Competencies.competencies_id) AS Competences_count
FROM Teachers
LEFT JOIN Teachers2Competencies
ON Teachers.id = Teachers2Competencies.teacher_id
GROUP BY Teachers.id;


-- 5. Выведите список курсов с количеством студентов в каждом
SELECT Courses.title, COUNT(Students2Courses.student_id) AS Count_Of_Students
FROM Courses
LEFT JOIN Students2Courses
ON Courses.id = Students2Courses.course_id
GROUP BY Courses.id;

-- 6. Выведите список студентов, с количеством курсов, посещаемых каждым студентом. 
SELECT Students.name, COUNT(Students2Courses.course_id) AS Courses_Count
FROM Students
LEFT JOIN Students2Courses ON Students.id = Students2Courses.student_id
GROUP BY Students.id, Students.name;

