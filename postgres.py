import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


conn = psycopg2.connect(
    host=os.getenv('host'),
    database=os.getenv('database'),
    user=os.getenv('user')
)

cur = conn.cursor()


cur.execute('SELECT * FROM test_bet')

rows = cur.fetchall()
print(rows)

cur.close()
conn.close()