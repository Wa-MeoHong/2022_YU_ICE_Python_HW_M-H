"""
 파일명 : Find circle Area,circumference
 프로그램 목적 및 기능: 원의 반지름을 입력받아 넓이,원주를 출력
 프로그램 작성자 : 신대홍(2022년 3월 12일)
 최종 Update : Version 1.0.0, 2022년 3월 12일(신대홍)
 =======================================================================
     수정자          날짜        버전        수정내용
 =======================================================================
     신대홍     2022/03/12     v1.0.0       최초작성
"""
from math import *
radius = int(input("radius = "))
area = pi * radius**2
circumference = 2 * radius * pi
print("Circle of radius ({}) : arae ({}),\
 cicurmference ({})" .format(radius, area, circumference))