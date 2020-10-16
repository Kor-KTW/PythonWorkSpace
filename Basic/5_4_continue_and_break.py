absent = [2, 5, 39]
no_book = [7]
for student in range(1, 41) : # 1~40
    if student in absent:
        print("{0}, oh he is not here? than next" .format(student))
        continue
    elif student in no_book:
        print("{0}, read the book please" .format(student)) 
        print("you {0} don't bring your book? everybody study on your own. you follow me" .format(student))
        break
    print("{0}, read the book please" .format(student)) 


    
