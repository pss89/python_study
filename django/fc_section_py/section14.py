# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한글자 삭제)
print("Red\bApple")

# \t : 탭
print("Red\tApple")

url = 'http://naver.com'
my_str = url.replace('http://','')
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'

print("{0} 의 비밀번호는 {1} 입니다".format(url,password))

subway = ["유재석","조세호","박명수"]

print(subway.index("조세호"))

subway.insert(1,"정형돈")

print(subway)

subway.pop(2)

print(subway)

# 리스트 관련 함수
# sort() : 정렬, reverse() : 내용 반대로 , clear() : 모두 삭제