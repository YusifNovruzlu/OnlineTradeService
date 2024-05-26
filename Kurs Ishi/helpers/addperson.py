import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yusif2003!",
    database="onlinetrade"
)

# List of names, surnames, usernames, and passwords
names = [
    "Sahil", "Ali", "Aydin", "Murad", "Tural", "Nihad", "Rashad", "Javid", "Elnur", "Eldar",
    "Orkhan", "Kamran", "Ilkin", "Elchin", "Nariman", "Yashar", "Adil", "Ramin", "Anar", "Samir",
    "Kanan", "Rustam", "Farid", "Raul", "Toghrul", "Amil", "Zaur", "Elshan", "Araz", "Gurban",
    "Zakir", "Mehman", "Fikrat", "Emin", "Shahin", "Teymur", "Rauf", "Nazim", "Elmar", "Vugar",
    "Arif", "Yusif", "Asif", "Tahmasib", "Rovshan", "Aslan", "Etibar", "Gasim", "Jalal", "Ramiz"
]

surnames = [
    "Sahilov", "Aliyev", "Aydinov", "Muradov", "Turalov", "Nihadov", "Rashadov", "Javidov", "Elnurov", "Eldarov",
    "Orkhanov", "Kamranov", "Ilkinov", "Elchinov", "Narimanov", "Yasharov", "Adilov", "Raminov", "Anarov", "Samirov",
    "Kananov", "Rustamov", "Faridov", "Raulov", "Toghrulov", "Amilov", "Zaurov", "Elshanov", "Arazov", "Gurbanov",
    "Zakirov", "Mehmanov", "Fikratov", "Eminov", "Shahinov", "Teymurov", "Raufov", "Nazimov", "Elmarov", "Vugarov",
    "Arifov", "Yusifov", "Asifov", "Tahmasibov", "Rovshanov", "Aslanov", "Etibarov", "Gasimov", "Jalalov", "Ramizov"
]

usernames = [
    "sahill", "ali123", "aydin1", "murad_az", "turalbaku", "nihad007", "rashad85", "javid44", "elnur777", "eldar56",
    "orkhan90", "kamran33", "ilkin22", "elchin11", "nariman99", "yashar88", "adil66", "ramin77", "anar55", "samir123",
    "kananaz", "rustamq", "farid92", "raul87", "toghrul50", "amil31", "zaur1993", "elshan18", "araz78", "gurban01",
    "zakir26", "mehman61", "fikrat35", "emin10", "shahin29", "teymur14", "rauf06", "nazim47", "elmar04", "vugar11",
    "arif20", "yusif03", "asif68", "tahmasib97", "rovshan08", "aslan25", "etibar76", "gasim38", "jalal53", "ramiz66"
]

passwords = [
    "sah1l!", "al!123", "aydin1!", "mura@d", "tur#al", "niha$d", "rasha@d", "jav1d!", "elnur#1", "eld@ar",
    "orkhan!", "kam#ran", "ilkin12", "elch!n", "nar1man", "yash@r", "ad1l66", "ram1n77", "anar55#", "samir!23",
    "kanan@z", "rust@mq", "far1d92", "raul!87", "toghrul@", "amil31#", "zaur1993!", "elshan!8", "araz@78", "gurba@n",
    "zakir#26", "meh@man", "f1krat", "emi@n10", "sha#hin", "teymur!", "rauf!6", "nazim#7", "elmar04@", "vugar11!",
    "ari@f20", "yusif03#", "asi@f68", "tahm@97", "rovs@8n", "asl@n25", "etib@r76", "gas!m38", "jala@53", "ram!z66"
]

# Create a cursor object
cursor = conn.cursor()

# SQL query for inserting data into the users table
sql_users = "INSERT INTO users (name, surname, username, password) VALUES (%s, %s, %s, %s)"

# Combine names, surnames, usernames, and passwords into tuples and insert them into the database
data_users = list(zip(names, surnames, usernames, passwords))
for record in data_users:
    cursor.execute(sql_users, record)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("User data inserted successfully.")
