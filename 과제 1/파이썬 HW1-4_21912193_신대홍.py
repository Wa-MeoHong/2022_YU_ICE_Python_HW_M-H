# 파일명 : Drawing star
# #프로그램 목적 및 기능: 별의 선 길이를 입력받아 turtle그래픽으로 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 3월 5일)
# 최종 Update : Version 1.0.0, 2022년 3월 5일(신대홍)

import turtle as t #turtle 모듈을 약자 t로 사용

base = int(input("별의 선분 길이를 입력하시오. : "))
t.setup(1000,1000) # GUI load
t.shape("turtle")
t.width(3)
t.color("blue") #거북이모양, 선의 너비 3, 선색은 파랑
for i in range(5): #6
    t.forward(base)
    t.rt(144)
t.ht()