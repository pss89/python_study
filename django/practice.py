def solution(s):
    if s.isdigit() == True and (len(s) == 4 or len(s) == 6):
        answer = True
    else:
        answer = False
    return answer

s = 'a234'
print(solution(s))