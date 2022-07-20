# 파일명 : HomeWork 9-3~4_Classes.py
# 프로그램 목적 및 기능: 만들어둔 클래스를 저장하는 파일
#
# 프로그램 작성자 : 신대홍(2022년 5월 1일)
# 최종 Update : Version 1.0.0, 2022년 5월 1일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/01     v1.0.0       최초작성'


import json
from datetime import datetime

class CustomEncoder(json.JSONEncoder): #jsonEncoder 클래스
    def default(self, o):
        if isinstance(o, datetime):
            return {'__datetime__':o.replace(microsecond=0).isoformat()}
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}
#------------------------------------------------------------------------
class Matrix: # 행렬 클래스
    def __init__(self, name, row, col, Lst_data): #초기값 설정
        self.name = name
        self.row = row # 열 번호 (행 개수)
        self.col = col # 행 번호 (열 개수)
        lst_row = [] # 한 행을 완성하기위한 리스트 
        self.rows = [] # 행렬을 완성하기위한 리스트 (완성된 Lst_row를 여기 넣음) 
        index = 0
        for i in range(0, self.row): # 끝까지 반복
            for j in range(0, self.col): # 한 행을 만들기
                lst_row.append(Lst_data[index])
                index += 1
            self.rows.append(lst_row) # 완성된 한 행에 집어 넣음
            lst_row = [] # 초기화 
    def __str__(self):
        # 출력할 문자열을 완성하는 함수 
        print(self.name, "=")
        s = ""
        for i in range(0, self.row):
            for j in range(0, self.col):
                s += " {:>6.2f}".format(self.rows[i][j]) #문자열을 하나씩 추가
            s += "\n" #한 행이 끝나면 엔터추가
        return s

    def __add__(self, other): #행렬 덧셈
        lst_res = [] 
        for i in range(0, self.row):
            for j in range(0, self.col):
                r_ij= self.rows[i][j] + other.rows[i][j] # 행렬 덧셈 진행
                lst_res.append(r_ij) # 리스트에 추가
        return Matrix("R", self.row, self.col, lst_res) #리스트를 행렬로 교체

    def __sub__(self, other): # 행렬 뺄셈
        lst_res = []
        for i in range(0, self.row):
            for j in range(0, self.col):
                r_ij= self.rows[i][j] - other.rows[i][j] # 행렬 뺄셈 진행
                lst_res.append(r_ij)
        return Matrix("R", self.row, self.col, lst_res) # 리스트를 행렬로 교체
    
    def __mul__(self, other): # 행렬 곱셈
        C_row = self.row # 결과 행렬의 열 = 첫번째 행렬의 열
        C_col = other.col # 결과 행렬의 행 = 두번째 행렬의 행
        
        lst_res = []
        for i in range(0, C_row):
            for j in range(0, C_col):
                r_ij = 0
                for k in range(0, self.col):
                    r_ij += self.rows[i][k] * other.rows[k][j] # 행렬 곱셈 
                lst_res.append(r_ij)
        return Matrix("R", C_row, C_col, lst_res) # 리스트 → 행렬

    def setName(self, name):
        self.name = name