﻿# Bank-Management-System

## Overview
The Bank Management System is a Python application designed to manage various banking operations. Using Object-Oriented Programming (OOP) principles and SQL (SQLite), this system allows for efficient management of customer profiles, bank accounts, and financial transactions.

## Features
1. SignUp
2. SignIn
3. Balance Enquiry
4. Cash Deposite
5. Cash Withdraw
6. Fund Transfer
7. Status

## Database Integration:
Use SQLite for database operations and persistent storage.

## Getting Started

### Prerequisites
* Python 3.x
* SQLite (included with Python’s standard library)

## Example Usage
Here’s how to use the core functionalities of the system:

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

This is the sample code of Balance Enquiry in Bank Management System


## Acknowledgements
* Python documentation for programming practices.
* SQLite documentation for database operations.
* Open-source libraries used for development.


## Contact
For any questions or support, please contact  aarpit6388@gmail.com
