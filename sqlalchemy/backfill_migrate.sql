INSERT INTO book (title, isbn, create_at) 
SELECT map.new_title, src.isbn, src.create_at 
FROM (
    SELECT 'book1' AS old_title, 'book3' AS new_title
    UNION ALL SELECT 'book2', 'book4'
)  AS map
JOIN book AS src ON src.title = map.old_title
