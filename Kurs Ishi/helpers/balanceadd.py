import mysql.connector
import random

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yusif2003!",
    database="onlinetrade"
)

# Create a cursor object
cursor = conn.cursor()

# Generate 50 random values for each currency
azn = [random.uniform(100, 100000) for _ in range(100)]
usd = [random.uniform(100, 100000) for _ in range(100)]
eur = [random.uniform(100, 100000) for _ in range(100)]
btc = [random.uniform(0.001, 2) for _ in range(100)]
jpy = [random.uniform(1000, 10000000) for _ in range(100)]
xau = [random.uniform(0.1, 100) for _ in range(100)]
tsla = [random.uniform(1, 1000) for _ in range(100)]
eth = [random.uniform(0.01, 10) for _ in range(100)]

# SQL query for inserting data into the balance table
sql_balance = "INSERT INTO balance (AZN, USD, EUR, BTC, JPY, XAU, TSLA, ETH) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

# Combine all currency lists into tuples and insert them into the database
data_balance = list(zip(azn, usd, eur, btc, jpy, xau, tsla, eth))
for record in data_balance:
    cursor.execute(sql_balance, record)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Balance data inserted successfully.")
