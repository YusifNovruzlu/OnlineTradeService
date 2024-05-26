from entities.login import Login
from entities.register import Register
from entities.entercard import Card 
if __name__ == "__main__":
    
    LOG = Login()
    REG = Register()


    while True:
        ans = input('''
1 --- Login
2 --- Register
Enter your choice: ''')

        if ans == "1":
            # username = input("Enter username: ")
            # password = input("Enter password: ")
            LOG.login()
            break

        if ans == "2":
            # name = input("Enter name: ")
            # surname = input("Enter surname: ")
            # username = input("Enter username: ")
            # password = input("Enter password: ")
            REG.register()
            break

        else:
            print("Invalid choice. Please enter 1 for Login or 2 for Register.")
