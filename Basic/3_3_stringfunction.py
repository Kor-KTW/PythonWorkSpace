python = "Python Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))


# index, find 모두 처음 해당 문자가 나오는 위치를 찾아주고, 또한 ", +int"를 이용하면 int 이후에 나오는 첫 문자를 찾아줌. 없는 경우엔 -1로 표시 
# 문자열의 경우 존재여부만 0,-1로 표현함
 
index = python.index("n")
print(index)
print("---test---")
print(python.index("o"))
print("---over---")
index = python.index("n",index+1)
print(index)
strindex = python.index("Python")
print(strindex)
print(python.find("n"))
print(python.find("Python")) 
print(python.find("Java"))
print("---test---")
print(python.find("o",12))
print("---over---")
#print(python.index("Java")) >> .index if not exist  >> traceback

print(python.count("n"))