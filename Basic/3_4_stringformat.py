# print("a"+"b")
# print("a","b")

# Method 1 %d, %s, %c

print("I am %d years old." % 20) 
print("I like %s." % "파이썬")
print("Apple start with letter %c." %"A")

#%s
print("I am %s years old." % 20) 

print("I like %s and %s." % ("Blue", "Red")) 

# Method 2 using format 

print("I am {} years old".format(20))
print("I like {} and {}." .format("Blue", "Red"))
print("I like {0} and {1}." .format("Blue", "Red"))
print("I like {1} and {0}." .format("Blue", "Red"))

# Method 3  using function in format 

print("I am {age} years old, and I like {color}".format(age = 20, color="Red"))
print("I am {age} years old, and I like {color}".format(color="Red", age = 20))

# Method 4 (v3.6 ~ ) using f 
age = 20
color = "Red"

print(f"I am {age} years old, and I like {color}")