import psycopg2
import os
from dotenv import load_dotenv
import datetime
load_dotenv()


conn = psycopg2.connect(
    host=os.getenv('host'),
    database=os.getenv('database'),
    user=os.getenv('user')
)

cur = conn.cursor()
hello = 'hello_test'
now = datetime.datetime.now()

try:
    cur.execute("INSERT INTO test_bet VALUES (%s,%s,%s);",(hello,"bye5",now))
    conn.commit()
    print('success')
except (Exception, psycopg2.DatabaseError) as error:
    print(error)


cur.close()
conn.close()