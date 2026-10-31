from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://sample:password@127.0.0.1:3306/sample_db")
with engine.connect() as conn:
    result = conn.execute(text("SELECT DATABASE(), VERSION()"))
    print(result.one())
    conn.execute(
        text("""
        CREATE TABLE IF NOT EXISTS `book` (
            book_id INT PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(32) NOT NULL,
            isbn VARCHAR(16) NOT NULL,
            create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_book_title (title)
        )
    """)
    )
    conn.execute(
        text("""
                CREATE TABLE IF NOT EXISTS `order` (
                    order_id INT PRIMARY KEY AUTO_INCREMENT,
                    book_id INT,
                    CONSTRAINT fk_order_user
                        FOREIGN KEY (book_id) REFERENCES book (book_id)
                )
            """)
    )
    conn.execute(
        text("""
                INSERT INTO `book` (title, isbn)
                    VALUES
                        ('book1', '1234'),
                        ('book2', '1235');
       
                 """)
    )
    conn.execute(
        text("""
                    INSERT INTO `order` (book_id)
                        VALUES
                            (17), (18);
                """)
    )
    conn.commit()
    result = conn.execute(text("SELECT * FROM book"))
    print(result.all())
    result = conn.execute(text("SELECT * FROM `order`"))
    print(result.all())
