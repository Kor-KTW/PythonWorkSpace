#1,2,3,4 -> 101,102,103,104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#for using str
students_name_length = ["ironman", "torr", "groot"]
students_name_length = [len(i) for i in students_name_length]
print(students_name_length)
students_name = ["ironman", "torr", "groot"]
students_name = [i.upper() for i in students_name]
print(students_name)