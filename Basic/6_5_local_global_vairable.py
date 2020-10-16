print("--------------------------------------")

#local variable
gun = 10
def checkpoint_local(soldiers):
    gun = 20
    gun = gun - soldiers
    print("[local(in function)] remain gun : {0}".format(gun))

print("global gun : {0}".format(gun))
checkpoint_local(2)
print("remain gun : {0}".format(gun))

print("--------------------------------------")
#global variable
gun = 10

def checkpoint_global(soldiers):
    global gun
    gun = gun - soldiers
    print("[local(in function)] remain gun : {0}".format(gun))

print("global gun : {0}".format(gun))
checkpoint_global(2)
print("remain gun : {0}".format(gun))

print("--------------------------------------")
#return
gun = 10

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print("[local(in function)] remain gun : {0}".format(gun))
    return gun
print("global gun : {0}".format(gun))
gun=checkpoint_return(gun,2)
print("remain gun : {0}".format(gun))
