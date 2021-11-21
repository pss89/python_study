# 리스트 []
subway = [10,20,30]
print(subway)
print("\n-------------------------------------\n")
subway = ["유재석","조세호","박명수"]
print(subway)
print(subway.index("조세호")) # 1
subway.append("하하") # 리스트 끝에 추가
print(subway)
subway.insert(1,"정형돈") # 리스트의 key 1에 추가돼고 다른값들은 뒤로 이동 (중간 삽입)
print(subway)
subway.pop() # 뒤에서부터 하나씩 제거 ( 하하 제거 )
print(subway)
print("\n-------------------------------------\n")
# 같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
print("\n-------------------------------------\n")
# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)
# 순서 뒤집기
print("\n-------------------------------------\n")
num_list.reverse()
print(num_list)
print("\n-------------------------------------\n")
#모두 지우기
num_list.clear()
print(num_list)
print("\n-------------------------------------\n")
#다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호",20,True]
print(mix_list)
num_list.extend(mix_list)
print(num_list)