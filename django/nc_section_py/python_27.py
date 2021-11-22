# with
# import pickle

# 파일을 열어서 profile_file 에 저장
# pickle load를에 profile_file 변수를 삽입
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt","w",encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf-8") as study_file:
    print(study_file.read())