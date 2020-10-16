def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" .format(name,age,main_lang))


profile("taewoo, Kang", 27, "python")

profile(main_lang="python",name="taewoo, Kang", age=27)