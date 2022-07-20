# 파일명 : HomeWork 9-1.py 
# 프로그램 목적 및 기능: 터틀 그래픽 기반 다각형 그리기
#           다각형을 그리기 위한 외접원의 radius(반지름), 꼭지점수, 중심좌표(x, y),
#           색깔을 정의한 후, 이 다각형 튜플을 리스트에 추가한 후, 터틀 객체 그래픽으로 표현
# 프로그램 작성자 : 신대홍(2022년 5월 8일)
# 최종 Update : Version 1.0.0, 2022년 5월 8일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/12     v1.0.0       최초작성

import turtle as t  # turtle그래픽 불러오기 (이하 t로 불러온다.)
from math import * # 삼각함수 계산에 필요

PI = 3.14159265358979 # 라디안 값을 구하기 위한 파이값 설정
ROUND = 360 # 360도를 ROUND라고 따로 정의

def DrawPolygons (tuple_poly): # 도형 그리기 함수
    radius, num_Ver, x, y, Col = tuple_poly # 튜플의 요소를 변수로 나누어줌
    t.speed(10)
    t.width(3)  #그리는 선분의 너비를 3으로 
    t.color("black")
    t.up(); t.goto(x, y); t.write(t.pos()); t.dot(10,"red")
    # 펜을 위로 든 상태로 그릴 좌표로 이동한 후, 위치를 찍는다.
    t.color(Col)
    if (num_Ver == "Circle"): #만약 num_Ver가 원이라면
        t.forward(radius)
        t.lt(90)
        t.down()
        t.circle(radius) #원을 그린다.
        t.up()
    else:
        Ver_angle = (ROUND / num_Ver)
        # 외접원에 접하는 꼭짓점에서 그 다음 꼭짓점까지, 중심점과 각각 이었을 때의 그 각도
        j = 180 - ((180 - Ver_angle)/2) # 꼭지점에서 처음에 도형을 그리기전, 화살표를 돌릴 각도
        # 외접원의 반지름 2개와 변 1개로 이루어진 삼각형에서 변을 구하기 위해
        # 중심점에서 수직으로 변에 내려와서 직각삼각형에서 한 각도.
        radian = (PI/180) * (Ver_angle/2) # sin함수를 쓰기 위해 sin을 사용하기 위해 radian으로 고침
        length = radius * sin(radian) * 2 # 변의 길이 구함
        t.forward(radius) # 그림그리기 위해 꼭지점으로 이동
        t.rt(j)
        t.down() # 펜을 놓아 이제 그릴 준비
        for i in range(0, num_Ver):
            t.forward(length)
            t.rt(Ver_angle)
        t.up() #다 그렸기 때문에 펜을 듬
        t.home() #초기위치로 복귀

def main():
    L_polygons = [ (50, 3, -225, 100, "red"), (50, 4, -75, 100, "blue"),\
    (50, 5, 75, 100, "green"), (50, 6, 225, 100, "magenta"),\
    (50, 7, -225, -100, "brown"), (50, 8, -75, -100, "gold"),\
    (50, 9, 75, -100, "black"), (50, "Circle", 225, -100, "purple") ]
    # 도형 리스트 초기값

    t.setup(700, 500) # 터틀그래픽창 표시
    t.title("Drawing Polygons with turtle.circle")
    t.mode("logo") # 터틀 모드 설정 (logo : 화살표 초기 방향이 북쪽을 바라봄)

    for i in range(0, len(L_polygons)): # 도형 그리기
        DrawPolygons(L_polygons[i])
    
if(__name__ == "__main__"): # 메인함수 실행
    main()
    t.mainloop()
