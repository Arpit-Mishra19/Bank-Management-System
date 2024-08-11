


# USER REGISTRATION SIGN IN AND SIGN UP


from database import *
import random
from customer import *
from bank import Bank


def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("Username Already Exists")
        SignUp()
    else:
        print("Username is Available Please Proceed")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        city = input("Enter Your City: ")
        while True:
            account_number = int(random.randint(10000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("--"*45)
                print("                   Your Account Number",account_number)
                print("--"*45)
                break
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.createTransactionTable()


def SignIn():
    username = input("Enter username = ")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        while True:
            passward = input(f"Welcome {username.capitalize()} Enter your passward = ")
            temp = db_query(f"SELECT password FROM customers WHERE username = '{username}';")
            # print(temp[0][0])
            if temp[0][0] == passward:
                print("             Sign In Successfully ....")
                return username

            else:
                print("Wrong Password Try Again ....")
                continue
    else:
        print("UserName is incorrect")
        print("Please Enter a valid username .....")
        SignIn()


