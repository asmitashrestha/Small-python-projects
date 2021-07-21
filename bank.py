class bank:
    def __init__(self):
        self.balance=0
        print("Account is created")

    def deposit(self):
        amount=float(input("Enter the amount you want to depost:")) 
        self.balance =self.balance+amount
        print("Deposit is successful and the balance in the account is %f" %self.balance)

    def withdraw(self):
        amount=float(input("Enter the amount you want to withdrawn from your account:"))
        self.balance=self.balance-amount
        if self.balance>=amount:
            if amount>1000:               
               print("Withdrawn is successful and balance is %f"%self.balance)

            else:
              print("Insufficient balance in your account!!")

    def enquiry(self):
        print("Balance in the account is %f" %self.balance)            

ac=bank()
ac.deposit()
ac.withdraw()
ac.enquiry()

