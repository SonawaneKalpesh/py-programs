class Bank:
    def __init__(self):
        self.name = "user"
        self.balance = 0
        self.account_number = 0

    def set_details(self,name, balance,account_number):
        self.name = name
        self.balance = balance
        self.account_number=account_number

    def get_details(self):
        return self.name,self.balance,self.account_number

obj = Bank()
print("Initial balance:", obj.get_details())

obj.set_details("kalpesh Sonawane",1000,10101)
print("Updated balance:", obj.get_details())