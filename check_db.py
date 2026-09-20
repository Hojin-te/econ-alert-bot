from db import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM rates ORDER BY rate_date")
for row in cursor.fetchall():
    print(row)
conn.close()