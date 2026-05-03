import pandas as pd

bank_data={
            "job":["teacher","engineer","doctor","lawyer"],
            "Account Number":[1001,1002,1003,1004],
            "Name":["John", "Anna", "James", "Linda"],
            "Age":[28, 22, 35, 32],
            "City":["New York", "Paris", "London", "Berlin"],
            "Balance":[1000, 2000, 3000, 4000],
            }            
            

bank_df=pd.DataFrame(bank_data)
bnk=bank_df
#print(bnk)


class bank_account:
    def Account_all_info(self):
        user_input=int(input("Enter your account number: "))


        if user_input == bnk["Account Number"][0]:
            print("Account Number: ",bnk["Account Number"][0])
            print("Name: ",bnk["Name"][0])
            print("Age: ",bnk["Age"][0])
            print("City: ",bnk["City"][0])
            print("Balance: ",bnk["Balance"][0])
        elif user_input == bnk["Account Number"][1]:
            print("Account Number: ",bnk["Account Number"][1])
            print("Name: ",bnk["Name"][1])
            print("Age: ",bnk["Age"][1])
            print("City: ",bnk["City"][1])
            print("Balance: ",bnk["Balance"][1])
        elif user_input == bnk["Account Number"][2]:
            print("Account Number:",bnk["Account Number"][2])
            print("Name: ",bnk["Name"][2])
            print("Age: ",bnk["Age"][2])
            print("City: ",bnk["City"][2])
            print("Balance: ",bnk["Balance"][2])
        elif user_input == bnk["Account Number"][3]:
            print("Account Number:",bnk["Account Number"][3])
            print("Name: ",bnk["Name"][3])
            print("Age: ",bnk["Age"][3])
            print("City: ",bnk["City"][3])
            print("Balance: ",bnk["Balance"][3])
        else:
            print("Invalid account number")
class bank_balance:
    def balance_info(self):
        user_input=int(input("Enter your(balance)account number: "))
        if user_input == bnk["Account Number"][0]:
            print("Balance: ",bnk["Balance"][0])
        elif user_input == bnk["Account Number"][1]:
            print("Balance: ",bnk["Balance"][1])
        elif user_input == bnk["Account Number"][2]:
            print("Balance: ",bnk["Balance"][2])
        elif user_input == bnk["Account Number"][3]:
            print("Balance: ",bnk["Balance"][3])
        else:
            print("Invalid account number")
class bank_deposit:
    def deposit_info(self):
        user_input=int(input("Enter your(deposit) account number: "))
        if user_input == bnk["Account Number"][0]:
            print("Balance: ",bnk["Balance"][0])
            deposit_amount=int(input("Enter the deposit amount: "))
            bnk["Balance"][0]+=deposit_amount
            print("New Balance: ",bnk["Balance"][0])

        elif user_input == bnk["Account Number"][1]:
            print("Balance: ",bnk["Balance"][1])
            deposit_amount=int(input("Enter the deposit amount: "))
            bnk["Balance"][1]+=deposit_amount
            print("New Balance: ",bnk["Balance"][1])
        
        elif user_input == bnk["Account Number"][2]:
            print("Balance: ",bnk["Balance"][2])
            deposit_amount=int(input("Enter the deposit amount: "))
            bnk["Balance"][2]+=deposit_amount
            print("New Balance: ",bnk["Balance"][2])
        
        elif user_input == bnk["Account Number"][3]:
            print("Balance: ",bnk["Balance"][3])
            deposit_amount=int(input("Enter the deposit amount: "))
            bnk["Balance"][3]+=deposit_amount
            print("New Balance: ",bnk["Balance"][3])
        else:
            print("Invalid account number")
class bank_waithdraw:
    def withdraw_info(self):
        user_input=int(input("Enter your(withdraw) account number: "))
        if user_input == bnk["Account Number"][0]:
            print("Balance: ",bnk["Balance"][0])
            withdraw_amount=int(input("Enter the withdraw amount: "))
            bnk["Balance"][0]-=withdraw_amount
            print("New Balance: ",bnk["Balance"][0])
        elif user_input == bnk["Account Number"][1]:
            print("Balance: ",bnk["Balance"][1])
            withdraw_amount=int(input("Enter the withdraw amount: "))
            bnk["Balance"][1]-=withdraw_amount
            print("New Balance: ",bnk["Balance"][1])
        elif user_input == bnk["Account Number"][2]:
            print("balance: ",bnk["Balance"][2])
            withdraw_amount=int(input("Enter the withdraw amount: "))
            bnk["Balance"][2]-=withdraw_amount
            print("New Balance: ",bnk["Balance"][2])
        elif user_input == bnk["Account Number"][3]:
            print("balance: ",bnk["Balance"][3])
            withdraw_amount=int(input("Enter the withdraw amount: "))
            bnk["Balance"][3]-=withdraw_amount
            print("New Balance: ",bnk["Balance"][3])
        else:
            print("Invalid account number")


bank_accoun=bank_account()
bank_balane=bank_balance()
bank_deposi=bank_deposit()
bnk_withdaw=bank_waithdraw()

bank_accoun.Account_all_info()
bank_balane.balance_info()
bank_deposi.deposit_info()
bnk_withdaw.withdraw_info()

print("Thank you,dear customer")