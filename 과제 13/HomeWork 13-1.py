
# 파일명 : HomeWork 13-1.py
# 프로그램 목적 및 기능: 파이썬 터틀 그래픽을 이용하여 아날로그시계 만들기
# 프로그램 작성자 : 신대홍(2022년 6월 5일)
# 최종 Update : Version 1.0.0, 2022년 6월 5일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/06/05     v1.0.0       최초작성

import turtle
from turtle import * # 아날로그 시계를 표현하기 위한 함수
from datetime import datetime # 날짜 관련 라이브러리 함수

def jump(dis): # 점프 함수
    penup();    forward(dis);   pendown()
    # 펜을 들고 거리만큼 앞으로 이동 후, 다시 펜을 내려놓음

def rectangle(width, height): # 사각형 만드는 함수
    fd(width/2);    lt(90);     fd(height);     lt(90)
    fd(width);      lt(90);     fd(height);     lt(90)
    fd(width/2)

def make_hand_shape(name, width, height): # 시계 모양 만들기 함수
    reset()
    left(90); jump((-height)*0.15); right(90)
    begin_poly()
    rectangle(width, height*1.15)
    end_poly()
    clock_hand = get_poly()
    register_shape(name, clock_hand)

def clockface(radius): # 시계 페이스 만들기
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump((-radius)-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup(): # 초기 설정
    global sec_hand, min_hand, hour_hand, writer
    mode("logo") 
    make_hand_shape("sec_hand", 5, 150) # 초침 만들기
    make_hand_shape("min_hand", 10, 130) # 분침 만들기
    make_hand_shape("hour_hand", 15, 110) # 시침 만들기
    clockface(160)
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("black", "black")
    
    min_hand = Turtle()
    min_hand.shape("min_hand")
    min_hand.color("blue1", "blue1")

    sec_hand = Turtle()
    sec_hand.shape("sec_hand")
    sec_hand.color("red", "red")
    for hand in sec_hand, min_hand, hour_hand: # resize함
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()
    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.bk(85)

def getWeekDayString(t): # 요일을 반환해줌
    weekday_name = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday_name[t.weekday()]

def getDateString(date): # 날짜 반환
    month_name = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
        "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    yr = date.year
    mn = month_name[date.month-1]
    dy = date.day
    return "%s %d %d" % (mn, dy, yr)

def tick(): # 시계가 돌아가는 것을 표현함
    t = datetime.today()
    sec = t.second + t.microsecond*0.000001 # 시간을 표시 (초)
    minute = t.minute + sec/60.0    # 분
    hour = t.hour + minute/60.0     # 시
    try:  # 종료 되기 전
        tracer(False)
        writer.clear()
        writer.home()
        writer.pencolor("darkred")
        writer.forward(65)
        writer.write(getWeekDayString(t),
                align="center", font=("Courier", 14, "bold"))
        writer.back(150)
        writer.pencolor("brown")
        writer.write(getDateString(t),
                align="center", font=("Courier", 14, "bold"))
        writer.back(30)
        hhmmss = "(%2d : %2d : %2d)"%(hour, minute, sec)
        writer.pencolor("red")
        writer.write(hhmmss, align="center", font=("Tahoma", 14, "bold"))
        writer.forward(115)
        tracer(True)
        sec_hand.setheading(6*sec + 90) # or here
        min_hand.setheading(6*minute + 90)
        hour_hand.setheading(30*hour + 90)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass # 종료가 된 상태
def main(): # 메인 함수
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "Analog clock demo"

if __name__ == "__main__":
    mode("logo") # 로고 실행
    turtle.setup(500, 500) # 터틀그래픽 셋업
    turtle.title("My Analog Clock with Python")
    msg = main()
    mainloop()