-- 7 Знайти оцінки студентів в окремій групі з певного предмета.
SELECT d.name, gr.name, s.fullname, g.grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
JOIN groups gr ON gr.id = s.group_id
WHERE d.id = 6 AND gr.id = 2;