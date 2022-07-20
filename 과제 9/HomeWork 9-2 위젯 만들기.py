# 파일명 : HomeWork 9-2.py 
# 프로그램 목적 및 기능: tkinter 기반 거리 변환기 구현
#          거리를 나타내는 km, mile의 양방향 변환 계산기 구현
# 프로그램 작성자 : 신대홍(2022년 5월 8일)
# 최종 Update : Version 1.0.0, 2022년 5월 8일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/12     v1.0.0       최초작성

from tkinter import * # tkinter 라이브러리 호출

class KmMile: # 클래스 생성
    def __init__(self, master): # 초기 화면 설정
        frame = Frame(master) #컨테이너 위젯, 윈도우 창을 생성 함
        frame.pack() # 위젯을 압축배치함 (위젯의 크기에 맞게 윈도우창을 조절)
        
        self.km_var = DoubleVar() # 실수형을 입력할 변수를 만듦
        Entry(frame, textvariable=self.km_var).grid(row=0,column=0) 
        # 입력칸 생성, text를 입력하면 km_var에 실수형으로 담긴다.
        Label(frame, text='Km').grid(row=0,column=1) # 라벨 생성 (입력 칸 바로 옆에 생성)
        self.mile_var = DoubleVar() # 마일 입력을 위한 실수형 입력 변수 생성
        Entry(frame, textvariable=self.mile_var).grid(row=0,column=2) #km와 똑같이 입력 칸 생성
        Label(frame, text='Mile').grid(row=0,column=3) # 라벨 Mile 생성
        button1 = Button(frame, text='Km -> Mile', command= self.KmtoMile)
         #아래칸에 버튼1번 생성 (Km -> Mile 기능 수행)
        button1.grid(row=1, column=0) # 버튼1 위치 
        button2 = Button(frame, text='Mile -> Km', command= self.MiletoKm)
         # 버튼 2 생성 (Mile -> Km 기능 수행)
        button2.grid(row=1, column=2) # 버튼2 위치

    def KmtoMile(self): # Km -> Mile 수행하는 함수, 1 mile = 1.60924 km
        Km = self.km_var.get()
        Mile = Km / 1.60934 # 킬로미터를 마일로 변환
        self.mile_var.set(round(Mile, 3)) # 유효숫자 3자리로 표현
    
    def MiletoKm(self): # Mile -> Km 수행하는 함수, 1 mile = 1.60924 km
        Mile = self.mile_var.get()
        Km = Mile * 1.60934  # 마일을 킬로미터로 변환
        self.km_var.set(round(Km, 3)) # 유효숫자 3자리로 표현

def main():
    window = Tk() # 윈도우 창 생성
    window.wm_title('Km <-> Mile Converter') # 창 타이틀 설정
    app = KmMile(window) # 창 출력
    window.mainloop() # 꺼지지 않게 함

if __name__ == "__main__": #메인함수 출력
    main()
