# 파일 입출력
# 파일 생성 및 작성
# score_file = open("score.txt","w",encoding="utf8") # 한글 깨짐 방지
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
# print("\n-------------------------------------\n")
# 추가하기
# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 80")
# score_file.close()
# print("\n-------------------------------------\n")
# 파일 읽기 (모두 읽기)
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()
# print("\n-------------------------------------\n")
# # 한줄씩 읽기
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end="") # 한줄씩 읽고 커서는 다음줄로 이동
# score_file.close()
# print("\n-------------------------------------\n")
# 몇줄일지 모를 때 읽기
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line: # 값이 없을 때는 break
#         break
#     print(line,end='')
# score_file.close()
# print("\n-------------------------------------\n")
# 리스트 형태로 보여주기
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line,end="")
score_file.close()