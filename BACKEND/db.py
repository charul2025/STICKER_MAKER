import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables

# Connect to your postgres database
conn = psycopg2.connect(
   os.getenv("DB_URL")
)

# Create a cursor object
cur = conn.cursor()

# Execute a query
cur.execute("SELECT version();")

# Fetch and print result
print(cur.fetchone())

# Close the cursor and connection
cur.close()
conn.close()
