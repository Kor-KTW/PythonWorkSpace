#Site_Name= "http://naver.com"
Site_Name="https://dirams.re.kr"
print("Site Name Check :", Site_Name)

#find parts

F_P_I=Site_Name.find("/")+2
S_P_I=Site_Name.find(".")

forpw=Site_Name[F_P_I:S_P_I]
#print(forpw)
newpw=forpw[:3]+str(len(forpw))+str(forpw.count('e'))+"!"
# forprin1=str(forpw)
# forprin2=str(newpw)
print(f"새로 생성된 {Site_Name}의 비밀번호는 {newpw}입니다")

