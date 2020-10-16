score_file = open("score.txt", "w", encoding="utf8") #w< writing , utf8< 한글 사용시 깨짐 방지
print("math : 0", file=score_file)
print("eng  : 150", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") #a < appending(추가), utf8< 한글 사용시 깨짐 방지
score_file.write("science : 80")
score_file.write("\ncoding : 100") #> .write를 이용한 경우 자동줄바꿈이 안됌.
score_file.close()


print("\n{0:-<30}".format("-"))

score_file = open("score.txt", "r", encoding="utf8") #r < reading
#print(score_file.read()) # read all line, move curso to the end 
print(score_file.readline(), end="") # read by line,  move cursor to next line 
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()


print("\n{0:-<30}".format("-"))

#using while loop
score_file = open("score.txt", "r", encoding="utf8") 
while True:
    line = score_file.readline()
    if not line :
        break
    print(line, end="")
score_file.close()


print("\n{0:-<30}".format("-"))

#using for
score_file = open("score.txt", "r", encoding="utf8") 
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()