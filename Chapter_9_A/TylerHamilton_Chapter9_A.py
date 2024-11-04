class BankAcct:
    def __init__(self, name:str, acct_num:int, amount:float, interest_rate:float):
        self.name = name
        self.acct_num = acct_num
        self.amount = amount
        self.interest_rate = interest_rate
    
    def adjust_interest(self, new_interest_rate:float)->None:
        self.interest_rate = new_interest_rate
    
    def withdraw(self, withdraw_amount)->None:
        if withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
        else:
            print("Insufficient funds.")
    
    def deposit(self, deposit_amount)->None:
        self.amount += deposit_amount
    
    def get_balance(self)->float:
        return self.amount
    
    def calculate_interest_by_days(self, num_days)->float:
        return self.amount * ((1 + self.interest_rate / 365) ** num_days - 1)
    
    def __str__(self)->str:
        return f'Current Balance: ${self.amount:.2f} \nInterest Rate: {self.interest_rate:.2f}%'


def banking_test():
    account = BankAcct("Tyler Hamilton", 23113, 1000, .3)
    
    print('Initial Account Details:')
    print(account, '\n')
    
    print('After Depositing $50.05:')
    account.deposit(50.05)
    print('Current Balance:', account.get_balance(), '\n')
    
    print('After Withdrawing $100.04')
    account.withdraw(100.04)
    print('Current Balance:', account.get_balance(), '\n')
    
    print('After Adjusting Interest:')
    account.adjust_interest(.6)
    print(account, '\n')
    
    print('Calculating 30 days of accrued interest:')
    interest = account.calculate_interest_by_days(30)
    print(f'Interest for 30 days: ${interest:.2f}\n')
    
    print('Final Account Details:')
    print(account, '\n')

banking_test()