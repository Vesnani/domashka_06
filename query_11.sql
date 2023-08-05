-- 11 Середній бал, який певний викладач ставить певному студентові.
SELECT t.fullname, s.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id
JOIN students s ON s.id = g.student_id
WHERE t.id = 3 AND s.id = 12;