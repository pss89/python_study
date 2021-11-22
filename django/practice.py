def solution(seoul):
    find_num = seoul.index("Kim")

    answer = '김서방은 {0}에 있다'.format(find_num)
    return answer

list = ["Jane","Kim"]
print(solution(list))