class Bank_balance():
    Account_Number = 123
    Balance = 0

    def __init__(self,Balance,Account_Number) :
        self.Balance = Balance
        self.Account_Number = Account_Number

    def Debit(self,deb = None):
        deb = int(input("Enter Amount to Debit : "))
        self.Balance-=deb
        print("The Account is deboted by : ", deb)
        print("The Balance is :",self.Balance)
        
    def Credit(self,cred = None):
        cred = int(input("Enter Amount to Credit : "))
        self.Balance += cred
        print("The Account is Credited by : ", cred)
        print("The Balance is :",self.Balance)


    def show_Balance(self) :
        print("Your Final Balance is : ",self.Balance)



Balance = int(input("Enter Account Balance : " ))
Account_Number = int(input("Enter Account Number :"))

a1 = Bank_balance(Balance ,Account_Number )
a1.Debit()
a1.Credit()
a1.show_Balance()


    
