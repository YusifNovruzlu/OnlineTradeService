import mysql.connector
import re

class Register:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "Yusif2003!"
        self.database = "onlinetrade"

    def register(self):
        def is_valid_name(name):
            return re.match("^[A-Za-z]+$", name) is not None

        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()

            while True:
                name = input("Enter your name: ")
                if not is_valid_name(name):
                    print("Invalid name. Please enter a name with alphabetic characters only.")
                    continue
                break

            while True:
                surname = input("Enter your surname: ")
                if not is_valid_name(surname):
                    print("Invalid surname. Please enter a surname with alphabetic characters only.")
                    continue
                break

            username = input("Enter a username: ")
            password = input("Enter a password: ")

            query = "INSERT INTO users (name, surname, username, password) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (name, surname, username, password))
            self.connection.commit()
            print("Registration successful.")

        except mysql.connector.Error as error:
            print("Error registering user:", error)

        finally:
            if self.connection:
                self.connection.close()
                print("Connection closed.")

# Example usage:
# register_system = Register()
# register_system.register()
