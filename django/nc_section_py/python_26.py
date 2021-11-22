#pickle : 사용하는 데이터를 파일형태로 저장
import pickle
# 데이터를 pickle 파일로 저장
# profile_file = open("profile.pickle","wb",) # pickle 사용하려면 b를 붙여줘여함(binary)
# profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile에 있는 정보를 profile_file에 저장
# profile_file.close()

# 읽기
profile_file = open("profile.pickle","rb",) # pickle 사용하려면 b를 붙여줘여함(binary)
profile = pickle.load(profile_file) # 파일에 있는 정보를 profile에 저장
print(profile)
profile_file.close()