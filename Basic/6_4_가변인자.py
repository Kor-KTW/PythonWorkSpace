#def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#    print("name : {0}\tage : {1}\t".format(name, age), end=" ")#end="" < print가 끝날때 줄바꿈을 하지 않게 한다.
#    print(lang1, lang2, lang3, lang4, lang5)

#profile("taewoo, Kang", 27, "python", "java", "C", "C++", "C#")
#profile("taewoo, Kang", 27, "kotlin", "swift", "","",""

def profile(name, age, *lang):
    print("name : {0}\tage : {1}\t".format(name, age), end=" ")#end="" < print가 끝날때 줄바꿈을 하지 않게 한다.
    print(lang, end=" ")
    print()

profile("taewoo, Kang", 27, "python", "java", "C", "C++", "C#")
profile("taewoo, Kang", 27, "kotlin", "swift")

