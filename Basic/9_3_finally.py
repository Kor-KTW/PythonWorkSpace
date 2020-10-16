class Bignumerror(Exception):

    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    print("한 자리 숫자 전용 계산기다")
    num1 = int(input("첫번째 숫자는 무엇이냐"))
    num2 = int(input("두번째 숫자는 무엇이냐"))
    if num1 >=10 or num2 >= 10:
        raise Bignumerror("입력한값은 {0}, {1}이니라".format(num1,num2))
    print("{0} / {1} = {2}".format(num1,num2, int(num1/num2)))

except ValueError:
    print("wrong value. 이상한거말고한자리수만입력해라")
except Bignumerror as err:
    print("wrong value. 큰수말고한자리수만입력하거라")
    print(err)

finally:#error가 있건 없건 무조건 실행되는 구문(traceback 포함)
    print("계산기를 종료할테니 들어가보거라")