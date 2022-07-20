# 파일명 : HomeWork 9-1.py 
# 프로그램 목적 및 기능: 터틀 그래픽 기반 다각형 그리기
#           다각형을 그리기 위한 외접원의 radius(반지름), 꼭지점수, 중심좌표(x, y),
#           색깔을 정의한 후, 이 다각형 튜플을 리스트에 추가한 후, 터틀 객체 그래픽으로 표현
# 프로그램 작성자 : 신대홍(2022년 5월 8일)
# 최종 Update : Version 1.0.0, 2022년 5월 8일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/08     v1.0.0       최초작성
#     신대홍     2022/05/08     v1.1.0       도형 그리기 코드 최적화

import turtle as t  # turtle그래픽 불러오기 (이하 t로 불러온다.)

def DrawPolygons (tuple_poly): # 도형 그리기 함수
    radius, num_Ver, x, y, Col = tuple_poly # 튜플의 요소를 변수로 나누어줌
    t.speed(0); t.width(3)  #그리는 속도는 최고속도, 그리는 선분의 너비를 3으로 
    t.up(); t.goto(x, y); t.write(t.pos()); t.dot(10,"red")
    # 펜을 위로 든 상태로 그릴 좌표로 이동한 후, 위치를 찍는다.
    t.color(Col); t.forward(radius); t.lt(90); t.down()
    # 색깔을 정한 후, 초기위치에서 좌표를 이동 후, 위치를 잡고 펜을 내린다.
    
    if (num_Ver == "Circle"): #만약 num_Ver가 원이라면
        t.circle(radius) #원을 그린다.
    else:
        t.circle(radius, steps = num_Ver) #도형을 그린다.
    t.up()
    t.home() #초기위치로 복귀

def main():
    radius = 50 # 외접원 반지름 정의
    L_polygons = [ (radius, 3, -225, 100, "red"), (radius, 4, -75, 100, "blue"),\
    (radius, 5, 75, 100, "green"), (radius, 6, 225, 100, "magenta"),\
    (radius, 7, -225, -100, "brown"), (radius, 8, -75, -100, "gold"),\
    (radius, 9, 75, -100, "black"), (radius, "Circle", 225, -100, "purple") ]
    # 도형 리스트 초기값

    t.setup(700, 500) # 터틀그래픽창 표시
    t.title("Drawing Polygons with turtle.circle")
    t.mode("logo") # 터틀 모드 설정 (logo : 화살표 초기 방향이 북쪽을 바라봄)

    for i in range(0, len(L_polygons)): # 도형 그리기
        DrawPolygons(L_polygons[i])
    
if(__name__ == "__main__"): # 메인함수 실행
    main()
    t.mainloop()