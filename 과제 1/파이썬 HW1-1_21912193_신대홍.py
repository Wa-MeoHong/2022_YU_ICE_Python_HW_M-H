# 파일명 : Find Perimeter and Area and circle
# #프로그램 목적 및 기능: 원의 반지름을 받아 넓이와 둘레를 구하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 3월 4일)
# 최종 Update : Version 1.0.0, 2022년 3월 4일(신대홍)


from math import * # math 모듈 불러오기

radius = int(input("반지름을 입력하시오 : ")) # 반지름(radius) 입력
area = pow(radius,2)*pi # 원 넓이 
perimeter = 2*radius*pi # 원 둘레

print("원의 넓이 :"+str(area)+" 원의 둘레 :"+str(perimeter)) # 출력

