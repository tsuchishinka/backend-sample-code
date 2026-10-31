CREATE TABLE IF NOT EXISTS `book` (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(32) NOT NULL,
    isbn VARCHAR(16) NOT NULL,
    create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_book_title (title)
);

CREATE TABLE IF NOT EXISTS `order` (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    CONSTRAINT fk_order_user
        FOREIGN KEY (book_id) REFERENCES book (book_id)
);

INSERT INTO `book` (title, isbn)
    VALUES
        ('book1', '1234'),
        ('book2', '1235');

INSERT INTO `order` (book_id)
    VALUES
        (1), (2);