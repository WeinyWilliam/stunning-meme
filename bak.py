class BankAccount:
    account_amount = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        BankAccount.account_amount += 1
    def account(self):
        return f"{self.name}: {self.balance}$"
    def deposit(self):
        deposit = int(input("you want to deposit: "))
        post_balance = self.balance + deposit
        self.balance = post_balance
        print(f"you deposited {deposit}, your balance is: {post_balance}")
        breakpoint
    def withdraw(self):
        withdraw = int(input("you want to withdraw: "))
        post_balance = self.balance - withdraw
        self.balance = post_balance
        while withdraw > self.balance:
            print("Your balance is insufficient")
            withdraw = int(input("you want to withdraw: "))
        print(f"you withdrawed {withdraw}, your balance is: {post_balance}")
        breakpoint
    @classmethod
    def count(cls):
        return f"Total number of accounts in this simulation: {cls.account_amount}"
account1 = BankAccount("NLac", 10000000000)
account2 = BankAccount("AQuan", 10000000000)
account3 = BankAccount("QHuy", 100000000)
def withdraw_deposit_menu(account):
    print(BankAccount.account(account))
    WD = int(input("Withdraw/Deposit (1/2/0): "))
    while WD != 0:
        if WD == 1: 
            account.withdraw()
            WD = int(input("Withdraw/Deposit (1/2/0): "))
        elif WD == 2:
            account.deposit()
            WD = int(input("Withdraw/Deposit (1/2/0): "))
        else:
            WD = int(input("Withdraw/Deposit (1/2/0): "))
    bank_menu()
def bank_menu():
    print(f"{BankAccount.count()}")
    print("press 1,2,3 to choose the account, press 0 to get out")
    user_input = int(input())
    if user_input == 0:
        print("Exiting the bank menu.")
        breakpoint
    while user_input != 0:
        if user_input == 1:
            withdraw_deposit_menu(account1)
            user_input = int(input())
        elif user_input == 2:
            withdraw_deposit_menu(account2)
            user_input = int(input())
        elif user_input == 3:
            withdraw_deposit_menu(account3)
            user_input = int(input())
bank_menu()
