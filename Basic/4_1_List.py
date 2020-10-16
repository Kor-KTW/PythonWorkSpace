#list[]

#Subway

# Subway1 = 10
# Subway2 = 20
# Subway3 = 30

subway=[10, 20, 30]

print(subway)

taxi = ["유재석", "조세호", "박명수"]
print(taxi)
print(taxi.index("조세호"))

#Append, Insert : add
taxi.append("하하")
print(taxi)

taxi.insert(1, "정형돈")
print(taxi)


#pop : remove from back
print(taxi.pop())
print(taxi)

print(taxi.pop())
print(taxi)

print(taxi.pop())
print(taxi)

#Quantitiy of value
taxi.append("유재석")

print(taxi.count("유재석"))

#sorting
num_list = [5, 4, 3, 2, 1]
num_list.sort()
print(num_list)

#reverse
num_list.reverse()
print(num_list)

#clear the list
num_list.clear()    
print(num_list)

#list can use various mixed data types
mix_str = ["조세호", "유재석", 20, True]
print(mix_str)

#extend
num_for_extend = [5, 4, 3, 2, 1]
num_for_extend.extend(mix_str)
print(num_for_extend)