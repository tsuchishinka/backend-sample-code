from pathlib import Path

from sqlalchemy import create_engine, text

sql = Path("create_book_order.sql").read_text(encoding="utf-8")

engine = create_engine("mysql+pymysql://sample:password@127.0.0.1:3306/sample_db")
with engine.begin() as conn:
    conn.execute(text(sql))
