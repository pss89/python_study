# 탈출문자
print("백문이 불여일견\n백견이 불여일타")
print("저는 \"나도 코딩\" 입니다.")
print("\n-------------------------------------\n")
print("D:\\svc\\webapp\\python_django")
print("Red Apple\rPine") # PineApple
print("Redd\bApple") # RedApple
print("Red\tApple") # tab
print("\n-------------------------------------\n")
# 퀴즈
url = "http://naver.com"
url = url.replace("http://","") # http:// 공백으로 치환
url = url[:url.index(".")] # . 이 끝나는 부분만 자르기
ft = url[:3] # 앞 3글자만 추출
sl = len(url) # naver 의 글자수
st = url.count('e') # naver 의 e가 몇개인지
password = ft+str(sl)+str(st)+'!' # 패스워드 조합
print(password)