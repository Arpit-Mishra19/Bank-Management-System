
#-------- BANK SERVICES -------

from database import *
import datetime


class Bank:
    def __init__(self,username,account_number):
        self.__username = username
        self.__account_number = account_number
        self.createTransactionTable 

    def createTransactionTable(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction"
                 f"(timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER)")
        
    def balanceEnquiry(self):
        temp =db_query(f"SELECT balance,account_number FROM customers WHERE username = '{self.__username}';")
        print("--"*45)
        print(f"{self.__username} Your currently Balance is {temp[0][0]}")
        print("--"* 45)
        
    def CashDeposite(self,amount):
        temp =db_query(f"SELECT balance,account_number FROM customers WHERE username = '{self.__username}';")
        test = temp[0][0] +amount
        db_query(f"UPDATE customers SET balance = '{test}' WHERE username ='{self.__username}';")
        # self.balanceEnquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposite',"
                 f"'{amount}'"
                 f")")
        print("--"*45)
        print(f"{self.__username} Amount is Successfully Depositted into your Account '{self.__account_number}'")
        print("--"*45)

    def CashWithdraw(self,amount):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            test = temp[0][0] - amount
            db_query(
                f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}'; ")
            # self.balanceEnquiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Amount Withdraw',"
                     f"'{amount}'"
                     f")")
            print("--"*45)
            print(
                f"{self.__username} Amount is Sucessfully Withdraw from Your Account {self.__account_number}")
            print("--"*45)


    def fundtransfer(self, receive, amount):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            temp2 = db_query(
                f"SELECT balance FROM customers WHERE account_number = '{receive}';")
            if temp2 == []:
                print("Account Number Does not Exists")
            else:
                test1 = temp[0][0] - amount
                test2 = amount + temp2[0][0]
                db_query(
                    f"UPDATE customers SET balance = '{test1}' WHERE username = '{self.__username}'; ")
                db_query(
                    f"UPDATE customers SET balance = '{test2}' WHERE account_number = '{receive}'; ")
                receiver_username = db_query(
                    f"SELECT username FROM customers where account_number = '{receive}';")
                # self.balanceEnquiry()
                db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{self.__account_number}',"
                         f"'Fund Transfer From {self.__account_number}',"
                         f"'{amount}'"
                         f")")
                db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{self.__account_number}',"
                         f"'Fund Transfer to {receive} A/C',"
                         f"'{amount}'"
                         f")")
                print("--"*45)
                print(
                    f"{self.__username} Amount is Sucessfully Transaction from Your Account {self.__account_number}")
                print("45")
        
    
    
        
