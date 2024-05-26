import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yusif2003!",
    database="onlinetrade"
)

# List of card numbers, expiration dates, CVCs, and balances
cardnum = [
    "1234567812345678", "2345678923456789", "3456789034567890", "4567890145678901", "5678901256789012",
    "6789012367890123", "7890123478901234", "8901234589012345", "9012345690123456", "0123456701234567",
    "1234567812345679", "2345678923456788", "3456789034567899", "4567890145678908", "5678901256789019",
    "6789012367890128", "7890123478901239", "8901234589012348", "9012345690123459", "0123456701234568",
    "1234567812345677", "2345678923456787", "3456789034567898", "4567890145678907", "5678901256789018",
    "6789012367890127", "7890123478901238", "8901234589012347", "9012345690123458", "0123456701234566",
    "1234567812345676", "2345678923456786", "3456789034567897", "4567890145678906", "5678901256789017",
    "6789012367890126", "7890123478901237", "8901234589012346", "9012345690123457", "0123456701234565",
    "1234567812345675", "2345678923456785", "3456789034567896", "4567890145678905", "5678901256789016",
    "6789012367890125", "7890123478901236", "8901234589012344", "9012345690123454", "0123456701234564",    "1234567812345678", "2345678923456789", "3456789034567890", "4567890145678901", "5678901256789012",
    "6789012367890123", "7890123478901234", "8901234589012345", "9012345690123456", "0123456701234567",
    "1234567812345679", "2345678923456788", "3456789034567899", "4567890145678908", "5678901256789019",
    "6789012367890128", "7890123478901239", "8901234589012348", "9012345690123459", "0123456701234568",
    "1234567812345677", "2345678923456787", "3456789034567898", "4567890145678907", "5678901256789018",
    "6789012367890127", "7890123478901238", "8901234589012347", "9012345690123458", "0123456701234566",
    "1234567812345676", "2345678923456786", "3456789034567897", "4567890145678906", "5678901256789017",
    "6789012367890126", "7890123478901237", "8901234589012346", "9012345690123457", "0123456701234565",
    "1234567812345675", "2345678923456785", "3456789034567896", "4567890145678905", "5678901256789016",
    "6789012367890125", "7890123478901236", "8901234589012344", "9012345690123454", "0123456701234564"
]

expiration = [
    "12/25", "11/24", "10/23", "09/22", "08/21", "07/20", "06/19", "05/18", "04/17", "03/16",
    "02/15", "01/14", "12/13", "11/12", "10/11", "09/10", "08/09", "07/08", "06/07", "05/06",
    "04/05", "03/04", "02/03", "01/02", "12/01", "11/00", "10/99", "09/98", "08/97", "07/96",
    "06/95", "05/94", "04/93", "03/92", "02/91", "01/90", "12/89", "11/88", "10/87", "09/86",
    "08/85", "07/84", "06/83", "05/82", "04/81", "03/80", "02/79", "01/78", "12/77", "11/76", "12/25", "11/24", "10/23", "09/22", "08/21", "07/20", "06/19", "05/18", "04/17", "03/16",
    "02/15", "01/14", "12/13", "11/12", "10/11", "09/10", "08/09", "07/08", "06/07", "05/06",
    "04/05", "03/04", "02/03", "01/02", "12/01", "11/00", "10/99", "09/98", "08/97", "07/96",
    "06/95", "05/94", "04/93", "03/92", "02/91", "01/90", "12/89", "11/88", "10/87", "09/86",
    "08/85", "07/84", "06/83", "05/82", "04/81", "03/80", "02/79", "01/78", "12/77", "11/76"
]

cvc = [
    "123", "234", "345", "456", "567", "678", "789", "890", "901", "012",
    "321", "432", "543", "654", "765", "876", "987", "098", "109", "210",
    "132", "243", "354", "465", "576", "687", "798", "809", "920", "031",
    "213", "324", "435", "546", "657", "768", "879", "980", "091", "102",
    "312", "423", "534", "645", "756", "867", "978", "089", "190", "201",    "123", "234", "345", "456", "567", "678", "789", "890", "901", "012",
    "321", "432", "543", "654", "765", "876", "987", "098", "109", "210",
    "132", "243", "354", "465", "576", "687", "798", "809", "920", "031",
    "213", "324", "435", "546", "657", "768", "879", "980", "091", "102",
    "312", "423", "534", "645", "756", "867", "978", "089", "190", "201"
]

balanc = [
    1000.00, 2000.50, 3000.75, 4000.00, 5000.25, 6000.50, 7000.75, 8000.00, 9000.25, 10000.50,
    11000.75, 12000.00, 13000.25, 14000.50, 15000.75, 16000.00, 17000.25, 18000.50, 19000.75, 20000.00,
    21000.25, 22000.50, 23000.75, 24000.00, 25000.25, 26000.50, 27000.75, 28000.00, 29000.25, 30000.50,
    31000.75, 32000.00, 33000.25, 34000.50, 35000.75, 36000.00, 37000.25, 38000.50, 39000.75, 40000.00,
    41000.25, 42000.50, 43000.75, 44000.00, 45000.25, 46000.50, 47000.75, 48000.00, 49000.25, 50000.50,    1000.00, 2000.50, 3000.75, 4000.00, 5000.25, 6000.50, 7000.75, 8000.00, 9000.25, 10000.50,
    11000.75, 12000.00, 13000.25, 14000.50, 15000.75, 16000.00, 17000.25, 18000.50, 19000.75, 20000.00,
    21000.25, 22000.50, 23000.75, 24000.00, 25000.25, 26000.50, 27000.75, 28000.00, 29000.25, 30000.50,
    31000.75, 32000.00, 33000.25, 34000.50, 35000.75, 36000.00, 37000.25, 38000.50, 39000.75, 40000.00,
    41000.25, 42000.50, 43000.75, 44000.00, 45000.25, 46000.50, 47000.75, 48000.00, 49000.25, 50000.50
]

# Create a cursor object
cursor = conn.cursor()

# SQL query for inserting data into the users table
sql_users = "INSERT INTO cards (cardnum, expiration, cvc, money) VALUES (%s, %s, %s, %s)"

# Combine card numbers, expiration dates, CVCs, and balances into tuples and insert them into the database
data_users = list(zip(cardnum, expiration, cvc, balanc))
for record in data_users:
    cursor.execute(sql_users, record)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Card data inserted successfully.")
