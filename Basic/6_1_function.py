def open_account():
    print("new account is created")

def deposit(balance, money):
    print("Deposit is done. Balance is {0} dollar." .format(balance+money))
    return balance + money
def withdraw(balance, money):
    if balance >= money:
        print("withdraw is done, Balance is {0} dollar.".format(balance-money))
        return balance - money
process = int(input("which process do you want ?1\n 1.open account\n2.deposit\n3.withdraw\n4.done\n"))

balance = 0
while process != 4:
    if process == 1 :
        open_account()
        process = int(input("which process do you want ?1\n 1.open account\n2.deposit\n3.withdraw\n4.done\n"))

    elif process == 2 :
        money1 = int(input("how much do you want to deposit?"))
        balance = deposit(balance,money1)
        process = int(input("which process do you want ?1\n 1.open account\n2.deposit\n3.withdraw\n4.done\n"))

    else :
        money2 = int(input("how much do you want to withdraw?"))
        if balance >=money2:
            balance = withdraw(balance, money2)
        else :
            print("lack of balance")
        process = int(input("which process do you want ?1\n 1.open account\n2.deposit\n3.withdraw\n4.done\n"))


print("have a nice day.")
