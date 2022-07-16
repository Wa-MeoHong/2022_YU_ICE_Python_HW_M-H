"""
 파일명 : Find area, perimeter of rectangle
 프로그램 목적 및 기능: 직사각형의 가로,세로를 입력받아 넓이, 둘레를 출력
 프로그램 작성자 : 신대홍(2022년 3월 12일)
 최종 Update : Version 1.0.0, 2022년 3월 12일(신대홍)
 =======================================================================
     수정자          날짜        버전        수정내용
 =======================================================================
     신대홍     2022/03/12     v1.0.0       최초작성
"""

x_str = input("width, length : ")
decimal_str = x_str.split(sep=' ')
width, length = map(int,decimal_str)
area = width * length
perimeter = 2 * (width + length)
print("Rectangle of width({}) and length({}) :\
 area ({}), perimeter ({})".format(width,length, area,perimeter))