cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

#if element did not defined at the number you used, 
#[] makes trace back and .get() return None 

#print(cabinet[5])
print(cabinet.get(5))
#if the number you used is not defined, than str after "," would be returned
print(cabinet.get(5, "사용 가능"))

cabinet2 = {"A-3":"유재석", "B-100":"김태호"}

print(cabinet2["A-3"])
print(cabinet2["B-100"])

#Add and update define
print(cabinet2)
cabinet2["C-20"] = "조세호"
cabinet2["A-3"] = "김종국"

print(cabinet2)

#remove define
del cabinet2["A-3"]
print(cabinet2)

#print keys
print(cabinet2.keys())

#print values
print(cabinet2.values())

#print all
print(cabinet2.items())

#clear
cabinet2.clear()
print(cabinet2)
