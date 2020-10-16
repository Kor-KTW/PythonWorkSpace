key_gen = input("사이트 주소를 입력하세요.")
key_gen = key_gen.lower()
# index = key_gen.index("/")
# key_gen = key_gen[index+2:]
if key_gen.find("/") >= 0:
    key_gen = key_gen[key_gen.index("/")+2:]

# print(key_gen)
if key_gen.find("www.") == 0:
    key_gen = key_gen[key_gen.index("w")+4:]
#    print(key_gen)
if key_gen.find("www2.") == 0:
    key_gen = key_gen[key_gen.index("w")+5:]

if key_gen.find("www3.") == 0:
    key_gen = key_gen[key_gen.index("w")+5:]

if key_gen.find(".") >= 0:
    key_check = key_gen.index(".")
    #print(key_check)

#print(key_gen.find("/"))

if key_gen.find("/") >= 0:
    #print(key_gen)
    key_gen = key_gen[:key_gen.index("/")]



dot_lst = []
for_loop = key_gen
#print(for_loop)
while True:
    if for_loop.find(".") >= 0:
        dot_lst.append(for_loop.find("."))
        for_loop = for_loop[for_loop.find(".")+1:]
        #print(for_loop)

    else:
        break

#print(dot_lst)
n_of_element = len(dot_lst)
#print(n_of_element)

if n_of_element != 0:
    for i in range(0,n_of_element):
        if i > 0:
            dot_lst[i]+=dot_lst[i-1]

#print(dot_lst)
length_dot_list = len(dot_lst)

pw2 = []
pw3 = 1
if length_dot_list == 1:
    pw2 = key_gen[:3]
    pw3 = int(len(key_gen[:dot_lst[0]]))

elif length_dot_list == 2:
    if key_gen[dot_lst[0]:dot_lst[1]]=="co":
        pw2 = key_gen[:3]
        pw3 = int(len(key_gen[:dot_lst[0]]))
    else:
        pw2 = key_gen[dot_lst[0]+1:dot_lst[0]+4]
        pw3 = int(len(key_gen[dot_lst[0]+1:dot_lst[1]]))
elif length_dot_list ==3:
    pw2 = key_gen[dot_lst[0]+1:dot_lst[0]+4]
    pw3 = int(len(key_gen[dot_lst[0]+1:dot_lst[1]]))
else:
    pass

# dot으로 찾는것이 아닌 co, com, de, re 등등 조건 추가하면 확실하게 될 듯. 
pw3 = str(pw3)
#print(key_gen)
#print("생성된 비밀번호 : "+key_gen[:3]+str(len(key_gen))+str(key_gen.count("e"))+"!")

print("생성된 비밀번호 : "+pw2+str(pw3)+str(key_gen.count("e"))+"!")

# 문자열 인덱스 찾기부터 시작할 것    