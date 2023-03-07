class Account():
    def __init__(self,name,balance):
        self.__balance = balance  
        self.name =name

    def check_balance(self):
        print(f"<{self.name.title()}: {self.__balance}>") 

    def reposit(self,other):
        self.__balance += other
        print(f"<{self.name.title()}: {self.__balance}>")

    def withdrawl(self,other):
        if self.__balance - other >1000:
           self.__balance -= other
           print(f"<{self.name.title()}: {self.__balance}>")
        else:
            print("you need at least 1000 in your account")

    def transaction(sender , reciever , amount):
        if sender.__balance >= amount and sender.__balance - amount > 1000:
            sender.__balance -= amount
            reciever.__balance += amount
            print("transaction completed")
            print(f"<{sender.name.title()}: {sender.__balance}>")
            print(f"<{reciever.name.title()}: {reciever.__balance}>")
        else :
            print("your balance is not enough") 



u1 =Account("amin",3000)
u2 =Account("ali",30000)

u1.check_balance()
u2.check_balance()
print("-"*20)
u1.reposit(5000)
print("-"*20)
Account.transaction(u1,u2,4000)






