def weight(height, gender):
    height=float(height)
    if gender == 'male':
        pro_weight=height*height*22/10000
    else :
        pro_weight=height*height*21/10000
    return pro_weight

gender = input("are you male or female?")
height = input("how tall are you?(cm)")

pro_weight = round(weight(height,gender),2)
print("height {0} {1}'s proper weight is {2}".format(height,gender,pro_weight))