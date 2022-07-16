"""
 파일명 : Drawing circle
 프로그램 목적 및 기능: 원의 중심의 x,y좌표, 원의 반지름(radius)를 입력받아
                    turtle그래픽으로 출력하는 프로그램
 프로그램 작성자 : 신대홍(2022년 3월 12일)
 최종 Update : Version 1.0.0, 2022년 3월 12일(신대홍)
 =======================================================================
    수정자          날짜        버전        수정내용
 =======================================================================
     신대홍     2022/03/12     v1.0.0       최초작성
"""

import turtle as t  #turtle그래픽 불러오기 (이하 t로 불러온다.)
x_str = input("pos_x, pos_y : ")  # 중심좌표 입력
radius = int(input("radius = "))  # 반지름 입력
decimal_str = x_str.split(sep=' ')  
pos_x, pos_y = map(int, decimal_str)#중심좌표 입력받은걸 pos_x,pos_y에 넣음
print("Drawing a circle of radius ({}) at position({}, {})\n \
 at start_position({}, {})".format(radius, pos_x, pos_y, pos_x, pos_y-radius))
  # 출력문 

t.shape("turtle")   #화살표모양을 거북이로 설정
t.color("red")  #거북이의 색을 "red"로 설정
t.width(3)  #그리는 선분의 너비를 3으로 
t.up()  #선을 그리지 않는 상태(펜을 위로 든 상태)
t.goto(pos_x, pos_y)  #입력한 좌표로 이동, 후에 좌표를 출력
t.write(t.pos())
t.dot(5,"red")  #좌표 표시용으로 점을 하나 찍는다
t.color("blue")  #거북이 색을"blue"로 바꾼 후, radius만큼 아래로 이동
t.goto(pos_x, pos_y-radius)
t.write(t.position()) 
t.down()  #이제부터 펜을 아래로 놓아 그릴 준비 
t.circle(radius)  #원 그리기
t.mainloop()  #창이 꺼지지않게 하기 위함
t.bye() 