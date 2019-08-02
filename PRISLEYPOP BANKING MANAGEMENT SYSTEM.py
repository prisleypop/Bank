
import os
import random
class Account :
    
    account_details = {}
    account_balance = {}
    def __init__(self):
        self.intro()
        self.createAccount()
        self.showAccount()    
    
    def createAccount(self):
        '''function for account creation'''
        #self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter new account holder name : ")
        self.type = input("Enter type of account [C/S] to be created: ").isupper()
        self.deposit = int(input("Enter The Initial amount: "))
        self.acc_Number = random.randint(10000,99999)
        self.account_details[self.name] = self.acc_Number
        self.account_balance[self.name] = self.deposit
        print("\n\n\nAccount Created")

    
    def showAccount(self):
        '''prints account details'''
        for self.accountname,self.accountnumber in self.account_details.items():
            print(self.accountname , self.accountnumber)
    
        
    def depositAmount(self,acc_no,amount):
        '''for deposit'''
        for acc_no in self.account_details.keys():
            self.deposit += amount
            print("DEPOSIT SUCCESSFUL")
    
    def withdrawAmount(self,acc_no,amount):
        '''to withdraw money'''
        for acc_no in self.account_details.values():
            self.deposit -= amount
            print("WITHDRAWAL SUCCESSFUL")
    
    def getAccountNo(self):
        return self.acc_no
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self,acc_no):
        for acc_no in self.account_details.values():
            return self.deposit
    

    def intro(self):
        print("\t\t\t********************************************")
        print("\t\t\tWELCOME TO PRISLEYPOP BANK MANAGEMENT SYSTEM")
        print("\t\t\t********************************************")
        input()


#start of the program
if __name__ =='__main__':
    bank = Account()
    ch = 0
    while ch != 8:
        print("\tMAIN MENU")
        print("\t1. MODIFY YOUR ACCOUNT")
        print("\t2. DEPOSIT AMOUNT")
        print("\t3. WITHDRAW AMOUNT")
        print("\t4. BALANCE ENQUIRY")
        print("\t5. ALL ACCOUNT HOLDER LIST")
        print("\t6. CLOSE AN ACCOUNT")
        print("\t8. EXIT")
        print("\tSelect Your Option (1-8) ")
        ch = int(input("Enter your choice : "))
        if ch == 1:
            bank.createAccount()
        elif ch == 2:
            acc_num = int(input("Enter The account No. : "))
            amount = int(input("Enter the amount to be deposited: "))
            bank.depositAmount(acc_num,amount)
        elif ch == 3:
            acc_num = int(input("Enter The account No. : "))
            amount = int(input("Enter the amount to be withdrawn"))
            bank.withdrawAmount(acc_num,amount)
        elif ch == 4:
            acc_num = int(input("\tEnter The account No. : "))
            bank.getDeposit()
        elif ch == 5:
            bank.showAccount()
        elif ch == 6:
            num =int(input("\tEnter The account No. : "))
            deleteAccount(num)
        elif ch == 7:
            num = int(input("\tEnter The account No. : "))
            modifyAccount(num)
        elif ch == 8:
            print("\tThanks for using bank managemnt system")
            break
        else :
            print("Invalid choice")
        
        
    


    
    
    
    
    
    
    
    
    
    
