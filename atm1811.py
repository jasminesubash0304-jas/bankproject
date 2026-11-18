balance=5000
def check_balance():
    print("current balance =",balance)
def check_deposit():
    global balance
    d=int(input("enter the amount:"))
    balance=balance+d
    print("current balance after deposit=", balance)
def check_withdrawal():
    global balance
    w=int(input("enter the amount:"))
    balance=balance-w
    print("current balance after withdrawal=", balance)
pin=int(input("enter the pin:"))
if pin==9596:
    
    
    
else:
    print("pin is not valid")