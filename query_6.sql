-- 6 Знайти список студентів у певній групі.
SELECT s.fullname, gr.name
FROM students s
JOIN groups gr ON s.group_id = gr.id
WHERE gr.id = 5;