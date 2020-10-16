import pickle

#with 안에선 close 필요 없음
#with with pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) 
#with open("study.txt", "w", encoding="utf8") as study_file:
#   study_file.write("study python now")

#with with normal txt
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
