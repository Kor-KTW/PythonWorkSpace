#set : can't overlap, no order
my_set = {1,2,3,3,3}
print(my_set)

alphabet={"a", "b", "c"}
betabet= set(["b", "c", "d"])

# intersection
print(alphabet & betabet)
print(alphabet.intersection(betabet))

# sum of set
print(alphabet|betabet)
print(alphabet.union(betabet))

#differnce of set
print(alphabet-betabet)
print(alphabet.difference(betabet))

#add set element
alphabet.add("f")
print(alphabet)

#remove set element
alphabet.remove("f")
print(alphabet)