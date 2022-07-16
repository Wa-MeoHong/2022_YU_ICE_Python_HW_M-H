"""
 파일명 : Print operation
 프로그램 목적 및 기능: 2개의 정수를 입력받고, a+b, a-b, a*b, a/b, a//b, a%b의 값을
		출력하는 프로그램
 프로그램 작성자 : 신대홍(2022년 3월 12일)
 최종 Update : Version 1.0.0, 2022년 3월 12일(신대홍)
 =======================================================================
    수정자          날짜        버전        수정내용
 =======================================================================
     신대홍     2022/03/12     v1.0.0       최초작성
"""
integer_str = input("input a and b : ") # 두 개의 수를 받기위한 문자열
decimal_str = integer_str.split(sep=' ') # 문자열안의 공백으로 문자열 나누기
a, b = map(int, decimal_str) # 나뉘어진 문자열(숫자)을 각각에 매핑

print("a({0:3d}) +  b({1:3d}) = {2:}" .format(a,b,a+b))
print("a({0:3d}) -  b({1:3d}) = {2:}" .format(a,b,a-b))
print("a({0:3d}) *  b({1:3d}) = {2:}" .format(a,b,a*b))
print("a({0:3d}) /  b({1:3d}) = {2:f}" .format(a,b,a/b))
print("a({0:3d}) // b({1:3d}) = {2:f}" .format(a,b,a//b))
print("a({0:3d}) %  b({1:3d}) = {2:f}" .format(a,b,a%b))
# 출력