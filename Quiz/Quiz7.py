import os
for i in range(1,51):
    bogo_file = open(str(i)+"주차.txt", "w", encoding="utf8") 
    print("- {0} 주차 주간 보고 -".format(i), file=bogo_file)
    print("부서 : ", file=bogo_file)
    print("이름 : ", file=bogo_file)
    print("업무 요약 : ", file=bogo_file)
    bogo_file.close()
    print(str(i)+"주차.txt가 생성되었습니다.")

a  = input("삭제하시겠습니까? yes/no")
if a =="yes":
    for i in range(1,51):
        os.remove(str(i)+"주차.txt") 
        print(str(i)+"주차.txt가 삭제되었습니다.")

