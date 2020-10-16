#while
Customer = "torr"
index = 5 
while index >=1 :
    print("{0}, coffee is ready. sir {1} times left" .format(Customer, index))
    index -=1
    if index ==0:
        print("coffee is excuted")


#infinite loop
index2 = 1
"""
while True:
    print("{0}, coffe is ready. {1} times called" .format(Customer,index2))
    index2 +=1
"""
Customer = "torr"
person = "unknown"

while person != Customer :
    print("{0}, coffee is ready sir" .format(Customer))
    person = input("what's your name? ")
print("here is your coffee {0}, have a nice day".format(Customer))



