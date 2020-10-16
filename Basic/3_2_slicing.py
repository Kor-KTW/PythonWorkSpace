Resident_registration_number = "940710-1933519"

print("성별 : " +Resident_registration_number[7])
print("생년 : 19" + Resident_registration_number[0:2]+"년") #0이상 2미만
print("월 : " + Resident_registration_number[2:4]+"월") 
print("일 : " + Resident_registration_number[4:6]+"일")

print("생년월일 : " + Resident_registration_number[:6]) #처음부터 6자리
print("주민등록번호 뒷자리 : " + Resident_registration_number[7:]) #7부터 끝까지