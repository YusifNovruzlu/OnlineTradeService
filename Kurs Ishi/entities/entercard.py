import mysql.connector

class Card:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "Yusif2003!"
        self.database = "onlinetrade"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to MySQL database")
        except mysql.connector.Error as error:
            print("Error connecting to MySQL database:", error)

    def enter_card(self):
        if not self.connection:
            self.connect()
        
        cardnum = input("Enter card number: ")
        expiration = input("Enter expiration date (YYYY-MM): ")
        cvc = input("Enter CVC: ")

        query = "SELECT cardnum, money FROM cards WHERE cardnum = %s AND expiration = %s AND cvc = %s"
        self.cursor.execute(query, (cardnum, expiration, cvc))
        result = self.cursor.fetchone()

        if result:
            print("Card number:", result[0])
            print("Money:", result[1])
        else:
            print("Card not found or details incorrect.")

        self.close_connection()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")

# Example usage:
# card_system = Card()
# card_system.enter_card()
