# 함수 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
        .format(name,age,main_lang))
    
profile("유재석",20,"Python")
profile("김태호",25,"Java")

# 같은학교, 같은학년, 같은반, 같은수업

def profile_v2(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
        .format(name,age,main_lang))
    
profile_v2("유재석")
profile_v2("김태호")

# 키워드 이용한 함수
def profile_v3(name, age, main_lang):
    print(name, age, main_lang)
    
profile_v3(name="유재석",age=20,main_lang="파이썬")
profile_v3(main_lang="자바",age=25,name="김태호")