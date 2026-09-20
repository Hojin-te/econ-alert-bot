import sqlite3

def init_db():
    conn = sqlite3.connect("rates.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            currency TEXT NOT NULL,
            value REAL NOT NULL,
            UNIQUE(date, currency)
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("테이블 준비 완료")