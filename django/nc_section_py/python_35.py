# 예외처리
try:
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
    # num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    # num2 = int(input("두 번째 숫자를 입력하세요 : "))
    # print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다")
except ZeroDivisionError as err:
    print(err)
# except:
except Exception as err:
    print(err)
    # print("알 수 없는 에러가 발생하였습니다")