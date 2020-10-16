# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" .format(name,age,main_lang))


# profile("taewoo, Kang", 27, "python")
# profile("jinheui,Jung", 27, "python")

# if age is all same
def profile(name, age=27, main_lang="python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" .format(name,age,main_lang))


profile("taewoo, Kang")