# 퀴즈
def std_weight(height,gender):
    result = ''
    if gender == "남자":
        result = round(height * height * 22,2)
    elif gender == "여자":
        result = round(height * height * 21,2)
    
    text_result = "키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(round(height*100),result)
    print(text_result)

std_weight(1.75,"남자")
std_weight(1.65,"여자")