import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yusif2003!",
    database="onlinetrade"
)

# Create a cursor object
cursor = conn.cursor()

# List of currency names and their values
currencies = [
    ('GBP', '2.3'),
    ('CAD', '1.35'),
    ('AUD', '1.3'),
    ('CHF', '1.85'),
    ('CNY', '0.26'),
    ('RUB', '0.02'),
    ('INR', '0.022'),
    ('SGD', '1.25'),
    ('HKD', '0.22'),
    ('NZD', '1.2'),
    ('MXN', '0.085'),
    ('ZAR', '0.11'),
    ('BRL', '0.33'),
    ('KRW', '0.0015'),
    ('TRY', '0.19'),
    ('SEK', '0.17'),
    ('NOK', '0.16'),
    ('DKK', '0.27'),
    ('PLN', '0.45'),
    ('THB', '0.05'),
    ('MYR', '0.4'),
    ('PHP', '0.034')
]

# SQL query for inserting data into the currency table
sql_currency = "INSERT INTO currency (nameofcurr, value) VALUES (%s, %s)"

# Insert the currency data
for currency in currencies:
    cursor.execute(sql_currency, currency)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Currency data inserted successfully.")
