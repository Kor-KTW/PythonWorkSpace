a = input("당신의 성별은 무엇입니까? 1.남성, 2.여성")
b = input("당신의 키는 몇 cm입니까?")
def std_weight(gender,height):    
    if gender == "1.남성" or "1" or "1." or "male":
        return float(height)*float(height)*22/10000
    else:
        return float(height)*float(height)*21/10000


if a == "1.남성" or "1" or "1." or "male":
    print("키 {0} 남성의 표준 체중은 {1}입니다.".format(b,round(std_weight(a,b),2)))