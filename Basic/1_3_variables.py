# 애완동물을 소개해주세요
animal = "강아지"
name = "폼폼이"
age = 1
hobby = "산책"
is_adult = age >= 3

print ("우리집 강아지의 이름은 폼폼이에요")
print ("폼폼이는 1살이며, 산책을 아주 좋아해요")
print ("폼폼이는 어른일까요? False")

print ("우리집 " + animal + "의 이름은 " + name + "에요")
print (name+"는"+str(age)+" 살이며, " +hobby+"을 아주 좋아해요")
print (name,"는",age," 살이며, ",hobby,"을 아주 좋아해요")
# +가아닌 ,를 이용할 경우 자동으로 띄워짐
print (name+"는 어른일까요? "+ str(is_adult))