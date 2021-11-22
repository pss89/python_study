# 다양한 출력 포맷
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하고, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽정렬, 빈칸으로 _로 채움
print("{0:_<10}".format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000))
# 3자리마다 콤마 찍고, +- 부호 붙이기
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))
# 3자리마다 콤마를 찍고, 부호도 붙이고, 자릿수 확보
# 빈자리는 ^^
print("{0:^<+30,}".format(1000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자릿수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))