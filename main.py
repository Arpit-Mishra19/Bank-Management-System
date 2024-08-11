



print("--"*40)
print("                     Welcome to Bank Management System                        ")
print("--"*40)

from register import *
from bank import *
status = False

while True:

    print("""
1. SignUP
2. SignIn

""")
    try:
        register = int(input("Enter any number = "))
        
        if register == 1 or register == 2:
            if register ==1:
                SignUp()
                n= input("Do you want to continue this loop Y/N ??")
                if n =="Y" or n=="y":
                    continue
                else:
                    exit()
            if register ==2:
                user = SignIn()
                status = True
                break
        else:
            print("Enter a Valid Input")

    except ValueError:
        print("Invalid Input !!")
        print("Try again !!")



user = SignIn()
account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")


while status:
    print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")   

    print("""
1. Balance Enquiry
2. Cash Deposite
3. Cash Withdraw
4. Fund Transfer
5. Exit 
""")
    try:
        facility = int(input("Enter any number = "))
        
        if facility >= 1 or facility <= 4:

            if facility ==1:
                bobj = Bank (user,account_number[0][0])
                bobj.balanceEnquiry()
        
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.CashDeposite(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            
            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.CashWithdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number"))
                        amount = int(input("Enter Money to Transfer"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.FundTransfer(receive, amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue

            elif facility == 5:
                print("Thanks For Using Banking Services")
                exit()


        else:
            print("Please Enter Valid Input From Options")
            continue

    except ValueError:
        print("Invalid Input Try Again with Numbers")
        continue

