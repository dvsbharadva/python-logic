class Bankaccount:
    def __init__(self, accNumber, name, balance) -> None:
        self.accNumber = accNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount
        print(f"Account has been credit of ${amount} ")
        print(f"Current account balance is: ${self.balance}\n")
        return self.balance

    def Withdraw(self, amount):
        self.balance -= amount
        print(f"${amount} has been debited.")
        print(f"Current account balance is: ${self.balance} \n" )
        return self.balance

    def BalanceInquiry(self):
        print("-=-=-=-= BALANCE INQUIRY =-=-=-")
        print(f"Account name: {self.name}")
        print(f"Account no: {self.accNumber}")
        print(f"Account Balance: ${self.balance}", "\n")

user = Bankaccount("Divyesh", 78965565, 300000)
user.BalanceInquiry()
user.Deposit(4200)
user.Deposit(4800)
user.Deposit(4600)
user.BalanceInquiry()
user.Withdraw(1200)