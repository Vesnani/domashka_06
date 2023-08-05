-- 12 Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT s.fullname, g.grade, MAX(g.date_of) AS last_date, gr.name
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN students s ON s.id = g.student_id
JOIN groups gr ON gr.id = s.group_id
WHERE d.id = 7 AND gr.id = 4
GROUP BY s.id, g.discipline_id
HAVING g.date_of = MAX(g.date_of);