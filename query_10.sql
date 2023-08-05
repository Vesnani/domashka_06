-- 10 Список курсів, які певному студенту читає певний викладач.
SELECT DISTINCT t.fullname, d.name, s.fullname
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN students s ON s.id = g.student_id
JOIN teachers t ON t.id = d.teacher_id
WHERE s.id = 45 AND t.id = 4;