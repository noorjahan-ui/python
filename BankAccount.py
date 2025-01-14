class BankAccount:
    def __init__(self,account_no,name,account_type,balance=0):
        self.account_no=account_no
        self.name=name
        self.account_type=account_type
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount}deposited successfully.New balance:{self.balance}")
        else:
            print("deposit amount must be positive")
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"insufficient balance.Available balance:{self.balance}")
        elif amount<=0:
            print("withdrawal amount must be positive")
        else:
            self.balance-=amount
            print(f"{amount}withdraw successfully.new balance:{self.balance}")
    def display_details(self):
        print("\n Account Details")
        print(f"Account Number:{self.account_no}")
        print(f"Account Holder:{self.name }")
        print(f"Account Type:{self.account_type}")
        print(f"Balance:{self.balance}")
print("welcome to Bank A/c management system")
account_no=input("enter a/c no:")
name=input("enter a/c holder's name:")
account_type=input("enter a/c type(savings/current):")
balance=int(input("enter initial balance :"))
account=BankAccount(account_no,name,account_type,balance)

print("\n1 Display Account details")
account.display_details()
print("\n 2.Deposit Money")
deposit_amount=float(input("enter amount to deposit:"))
account.deposit(deposit_amount)

print("\n 3.Withdraw Money")
withdraw_am=float(input("enter amount to withdraw:"))
account.withdraw(withdraw_am)

print("\n 4.Display updated account details")
account.display_details()