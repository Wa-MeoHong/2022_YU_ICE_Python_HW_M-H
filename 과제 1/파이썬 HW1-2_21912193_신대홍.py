# 파일명 : Drawing rectangle
# #프로그램 목적 및 기능: 직사각형의 가로, 세로를 입력받아 turtle그래픽으로 출력
# 프로그램 작성자 : 신대홍(2022년 3월 4일)
# 최종 Update : Version 1.0.0, 2022년 3월 4일(신대홍)

import turtle as t

width = int(input("직사각형의 가로를 입력하시오. : ")) #직사각형 가로 입력
height = int(input("직사각형의 세로를 입력하시오. : ")) #직사각형 세로 입력
t.setup(800,800)  #turtle GUI 불러옴
t.shape("turtle") #거북이 모양
t.width(3)  #선이 잘 보이도록 선의 너비를 3으로 설정
t.color("red") #이또한 잘 보이도록 색을 빨간색으로 줌
for i in range(2):  #반복문 
    t.forward(width)
    t.lt(90)
    t.forward(height)
    t.lt(90)