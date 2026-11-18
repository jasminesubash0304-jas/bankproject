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
    
    
    while True:
        choice=int(input("enter the number:"))
        if choice==1:
            check_balance()
        elif choice==2:
            check_deposit()
        elif choice==3:
            check_withdrawal()
        elif choice==4:
            break
        else:
            ("invalid")
        
else:
    print("pin is not valid")