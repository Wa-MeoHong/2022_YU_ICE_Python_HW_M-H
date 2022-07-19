# 파일명 : Homework5_3.py
# 프로그램 목적 및 기능: 파이썬 터틀 그래픽 기능을 사용하여 지정된 위치에
#    지정된 크기 (한 변의 길이)의 다각형을 그리는 drawPolygon() 함수를 구현하는
#    프로그램
# 프로그램 작성자 : 신대홍(2022년 4월 3일)
# 최종 Update : Version 1.0.0, 2022년 4월 3일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/03     v1.0.0       최초작성

import turtle as t  #turtle그래픽 불러오기 (이하 t로 불러온다.)
from math import * 

PI = 3.14159265358979
ROUND = 360

def DrawPolygon (x, y, numVer, length):
    t.shape("turtle")   #화살표모양을 거북이로 설정
    t.width(3)  #그리는 선분의 너비를 3으로 
    t.up()  #선을 그리지 않는 상태(펜을 위로 든 상태)
    t.goto(x, y)  #입력한 좌표로 이동, 후에 좌표를 출력
    t.write(t.pos())
    t.dot(5,"red")  #좌표 표시용으로 점을 하나 찍는다
    t.color("blue")  #거북이 색을"blue"로 바꾼 후
    j = (180 - (ROUND / numVer))/2 # 맨위 꼭지점으로 이동 후, 예시에 맞게 조정하기 위해
    # 내각의 절반을 구함
    radian = PI/180 * j # 라디안으로 변경
    height = (length/2)*tan(radian) #계산에 필요함
    hyp = sqrt(pow((length/2),2)+pow(height,2)) #중심위치에서 꼭짓점까지의 거리 구함
    if (numVer == 4 ): #만약 사각형일경우
        a = length/2 # 위에거 다무시하고, 길이의 절반만큼 x, y를 이동
        t.goto(x - a, y + a)
        t.lt(90 + (ROUND/ numVer)/2) # 이동후, 왼쪽위 45도를 바라본다.
    else:
        t.goto(x, y + hyp) # 나머지는 '중심 - 꼭지점까지 거리'(hyp)만큼  y좌표 이동후
        t.lt(90) #북쪽 바라보기
    t.lt(180 - j) #그후, 시작하기전 먼저 먼저 턴을 해줌
    t.down()  #이제부터 펜을 아래로 놓아 그릴 준비 

    for i in range(0,numVer):
        t.forward(length) #앞으로 가면서 그림
        t.write(t.position()) #위치 기록
        t.dot(5,"red")
        t.lt(ROUND / numVer) #외각만큼 턴함
    t.mainloop()  #창이 꺼지지않게 하기 위함


x_str = input("pos_x, pos_y, num_vertex and side_length : ") 
 # 중심좌표, 꼭지점 개수, 모서리 길이 입력
pos_x, pos_y, num_vet, length = map(int, x_str.split(sep=' '))
DrawPolygon(pos_x, pos_y, num_vet, length)
#중심좌표, 다각형 꼭짓점 개수, 모서리 길이 입력받은걸 각 변수에 집어넣는다에 넣음
