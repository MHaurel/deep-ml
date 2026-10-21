SELECT c.category_name AS category_name, EXTRACT(MONTH FROM s.searched_at) AS month, COUNT(*) AS search_count
FROM searches s
JOIN categories c ON s.category_id = c.category_id
WHERE EXTRACT(YEAR FROM s.searched_at) = 2023
GROUP BY EXTRACT(MONTH FROM s.searched_at), c.category_name
ORDER BY month ASC, category_name ASC;