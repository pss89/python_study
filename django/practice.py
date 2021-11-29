def solution(a, b):
    if a > b:
        start = b
        end = a+1
    else:
        start = a
        end = b+1

    answer = 0
    
    for i in range(start,end):
        answer += i

    return answer

a = 5
b = 3
print(solution(a,b))