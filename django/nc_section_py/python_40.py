# 패키지 : 여러개의 모듀을 모아놓은 것
# import travel.thailand
# # import travel.thailand.ThailandPackage
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__
from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 패키지, 모듈 위치 1
# import travel.thailand
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 패키지, 모듈 위치 2
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))