# 파일명 : Drawing isosceles triangle
# #프로그램 목적 및 기능: 이등변삼각형의 밑변, 높이를 입력받아 turtle그래픽으로 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 3월 5일)
# 최종 Update : Version 1.0.0, 2022년 3월 5일(신대홍)

import turtle as t
from math import *
base = int(input("이등변삼각형의 밑변을 입력하시오. : "))
height = int(input("이등변삼각형의 높이를 입력하시오. : "))
hyp = sqrt(pow((int(base)*0.5),2)+pow(int(height),2)) #빗변 구하기
B_degree = asin(height/hyp) * 180 / pi #밑변꼭지점의 각, 라디안 → 도로 변환
H_degree = 180 - (2 * B_degree) # 윗꼭지점의 각
t.setup(1000,1000) # turtle GUI 불러오기
t.shape("turtle") 
t.width(3)
t.color("blue") 
t.forward(base)
t.lt(180-B_degree) #left turn 약자
t.forward(hyp)
t.lt(180-H_degree)
t.forward(hyp)
t.ht() #hide turtle 약자, 거북이 숨기기