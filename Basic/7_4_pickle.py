#data -> file 
import pickle

profile_file = open("profile.pickle", "wb")#b=binary, encoding설정 필요x
profile = {"name":"g-park", "age":30, "hobby":["scoccer","golf","coding"]}
print(profile)
pickle.dump(profile,profile_file) #write profile data in profile_file 
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)#file data load
print(profile)
profile_file.close()
