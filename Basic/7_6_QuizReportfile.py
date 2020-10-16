for i in range(1,51):
    weekly=str(i)
    name=weekly+"주차.txt"
    print(name)
    score_file = open(name, "w", encoding="utf8") #w< writing , utf8< 한글 사용시 깨짐 방지
    print(" - "+ weekly + " 주차 주간보고 - ", file=score_file)
    print("부서  : ", file=score_file)
    print("이름  : ", file=score_file)
    print("업무 요약 : ", file=score_file)
    score_file.close()
######################################################################################
######################################################################################
for i in range(1,51):
    with open("master\'s "+str(i)+"주차.txt","w", encoding="utf8") as report_file:
        report_file.write(" - {0} 주차 주간보고 - " .format(i))  
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
######################################################################################
######################################################################################