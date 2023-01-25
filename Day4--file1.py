class Bank:
    name=" "
    account_number=" "
    branch=" "
    def __init__(self,name,account_number,branch):
         self.name=name
         self.account_number=account_number
         self.branch=branch
s1=Bank("Varsha",1234,"Kakinada")
print(s1.name)
print(s1.account_number)
print(s1.branch)

