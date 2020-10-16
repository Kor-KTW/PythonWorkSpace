try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("error! value miss")

except ZeroDivisionError as err:
    print(err)

#except Exception as err:
#    print(err)
except:
    print("error unknown")


try:
    print("한 자리 숫자 전용 계산기다")
    num1 = int(input("첫번째 숫자는 무엇이냐"))
    num2 = int(input("두번째 숫자는 무엇이냐"))
    if num1 >=10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1,num2, int(num1/num2)))

except ValueError:
    print("wrong value. 한자리수만입력해라")
