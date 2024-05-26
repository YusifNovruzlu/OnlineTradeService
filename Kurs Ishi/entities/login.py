import mysql.connector
from entities.entercard import Card  # Importing the Card class from entercard.py

class Login:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "Yusif2003!"
        self.database = "onlinetrade"
        self.connection = None
        self.cursor = None
        self.transaction_history = []

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

    def login(self):
        self.connect()
        
        username = input("Enter username: ")
        password = input("Enter password: ")

        query = """
            SELECT users.id, users.name, users.surname, cards.money, balance.AZN, balance.USD, balance.EUR, balance.BTC, balance.JPY, balance.XAU, balance.TSLA, balance.ETH 
            FROM users 
            INNER JOIN balance ON users.id = balance.id 
            INNER JOIN cards ON users.id = cards.id 
            WHERE users.username = %s AND users.password = %s
        """
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchone()

        if result:
            user_id = result[0]
            print("\nLogin successful.")
            while True:
                print("\n--- Account Options ---")
                print("1. Account Details")
                print("2. Buy or Sell")
                print("3. History")
                print("4. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    print("\nName:", result[1])
                    print("Surname:", result[2])
                    print("\nBalances:")
                    print("AZN:", result[4])
                    print("USD:", result[5])
                    print("EUR:", result[6])
                    print("BTC:", result[7])
                    print("JPY:", result[8])
                    print("XAU:", result[9])
                    print("TSLA:", result[10])
                    print("ETH:", result[11])
                elif choice == "2":
                    print("\n--- Buy or Sell ---")
                    print("1. Buy")
                    print("2. Sell")
                    print("3. Back")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == "1":

                        # Buy operation
                        print("\n--- Buy Options ---")
                        print("1. AZN (1.0)")
                        print("2. USD (1.7)")
                        print("3. EUR (2.0)")
                        print("4. BTC (5000)")
                        print("5. JPY (0.015)")
                        print("6. XAU (1800)")
                        print("7. TSLA (600)")
                        print("8. ETH (4000)")
                        currency_choice = int(input("Choose the currency to buy (1-8): "))
                        amount = float(input("Enter the amount you want to buy: "))
                        print("You want to buy", amount, "of the selected currency.")
                        currency_columns = ["AZN", "USD", "EUR", "BTC", "JPY", "XAU", "TSLA", "ETH"]
                        currency_rate = [1.0, 1.7, 2.0, 5000, 0.015, 1800, 600, 4000]
                        currency = currency_columns[currency_choice - 1]
                        rate = currency_rate[currency_choice - 1]
                        total_cost = amount * rate

                        card_money = float(result[3])  # Convert the money column to float

                        if card_money >= total_cost:
                            self.cursor.fetchall()  # Fetch all remaining results to clear the result set
                            # Update cards table
                            update_cards_query = "UPDATE cards SET money = money - %s WHERE id = %s"
                            self.cursor.execute(update_cards_query, (total_cost, user_id))
                            # Update balance table
                            update_balance_query = f"UPDATE balance SET {currency} = {currency} + %s WHERE id = %s"
                            self.cursor.execute(update_balance_query, (amount, user_id))
                            self.connection.commit()
                            print("Transaction successful. You bought", amount, currency, "for", total_cost, "from your card.")
                            self.transaction_history.append(f"Bought {amount} {currency} for {total_cost}")
                        else:
                            print("Insufficient funds.")
                    elif sub_choice == "2":
                        # Sell operation
                        print("\n--- Sell Options ---")
                        print("1. AZN")
                        print("2. USD")
                        print("3. EUR")
                        print("4. BTC")
                        print("5. JPY")
                        print("6. XAU")
                        print("7. TSLA")
                        print("8. ETH")
                        currency_choice = int(input("Choose the currency to sell (1-8): "))
                        amount = float(input("Enter the amount you want to sell: "))
                        print("You want to sell", amount, "of the selected currency.")
                        currency_columns = ["AZN", "USD", "EUR", "BTC", "JPY", "XAU", "TSLA", "ETH"]
                        currency_rate = [1.0, 1.7, 2.0, 5000, 0.015, 1800, 600, 4000]
                        currency = currency_columns[currency_choice - 1]
                        rate = currency_rate[currency_choice - 1]
                        total_gained = amount * rate

                        card_money = float(result[3])  # Convert the money column to float

                        if card_money >= amount:
                            self.cursor.fetchall()  # Fetch all remaining results to clear the result set
                            # Update cards table
                            update_cards_query = "UPDATE cards SET money = money + %s WHERE id = %s"
                            self.cursor.execute(update_cards_query, (total_gained, user_id))
                            # Update balance table
                            update_balance_query = f"UPDATE balance SET {currency} = {currency} - %s WHERE id = %s"
                            self.cursor.execute(update_balance_query, (amount, user_id))
                            self.connection.commit()
                            print("Transaction successful. You sold", amount, currency, "for", total_gained, "to your card.")
                            self.transaction_history.append(f"Sold {amount} {currency} for {total_gained}")
                        else:
                            print("Insufficient funds.")
                    elif sub_choice == "3":
                        continue
                    else:
                        print("Invalid choice.")
                elif choice == "3":
                    print("\n--- Transaction History ---")
                    for transaction in self.transaction_history:
                        print(transaction)
                elif choice == "4":
                    break
                else:
                    print("Invalid choice.")
        else:
            print("Invalid username or password.")

        self.close_connection()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")

# Example usage:
# login_system = Login()
# login_system.login()
