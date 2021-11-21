# section09
# 파일 읽기, 쓰기
# 읽기모드 : r , 쓰기모드(기존파일삭제) : w , 추가모드(파일 생성 또는 추가) : a
# .. : 상대경로 , . : 절대경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

#파일읽기
#예제1
f = open('../resource/review.txt','r')
content = f.read()
print(content)
#print(dir(f))
#반드시 close 리소스 반환
f.close()

print('--------------------------------------')
print('--------------------------------------')

#예제2
#close 하여 반환하지 않아도 됨
with open('../resource/review.txt','r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('--------------------------------------')
print('--------------------------------------')

#예제3
with open('../resource/review.txt','r') as f:
    for c in f:
        print(c.strip())

print('--------------------------------------')
print('--------------------------------------')

#예제4
with open('../resource/review.txt','r') as f:
    content = f.read() #한번에 다 읽었음
    print(">",content)
    content = f.read() #내용없음 (다음에는 없음)
    print(">",content)

print('--------------------------------------')
print('--------------------------------------')

#예제5
with open('../resource/review.txt','r') as f:
    line = f.readline()
    #print(line)
    while line:
        print(line, end=' #### ')
        line = f.readline()

print()

#예제6
with open('../resource/review.txt','r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=' ****** ')

print()

#예제7
with open('../resource/score.txt','r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)

print('average : {:6.3}'.format(sum(score)/len(score)))

#파일 쓰기

#예제1 (쓰기)
with open('../resource/text1.txt','w') as f:
    f.write('Niceman!')

#예제2 (추가)
with open('../resource/text1.txt','a') as f:
    f.write('Niceman!')

#예제3
from random import randint

with open('../resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')

#예제4
#writelines : 리스트 -> 파일로 저장
with open('../resource/text3.txt','w') as f:
    list = ['Kim\n','Park\n','Cho\n']
    f.writelines(list)

#예제5
with open('../resource/text4.txt','w') as f:
    print('Test Contests1!', file=f)
    print('Test Contests2!', file=f)