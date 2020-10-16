#sep -> 기존의 " "로 나뉘어지던 print 대상들의 구분을 sep = "" 안의 표현대로 구분함
#end -> print의 마지막이 기존에는 \n으로 줄바꿈되나
print("python", "java", "javascript", sep=" vs ", end="?")
print("which would be more fun?")


import sys
print("python", "java", file=sys.stdout)#표준출력 standard output, log 처리를 할 때 구분하기 위함.
print("python", "java", file=sys.stderr)#표준에러 standard error

#exam result
scores = {"math":0, "eng":50, "coding":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(12), sep=":")#ljust, rjust >정렬

# bank waiting number 
# 001, 002, 003, 
for num in range(1,21):
    print("number : " + str(num))
    
    if len(str(num)) == 1:
        num = "00"+str(num)
    if len(str(num)) == 2:
        num = "0"+str(num)
    print("number : " + str(num))
    print("number : " + str(num).zfill(3)) #zfill -> 남은 공간은 zero로 채움


answer = input("input any value")
#answer = 10
print("input type is "+str(type(answer))+".") #input으로 값을 가져오는 경우 자료형이 str으로 저장됨

