
# 파일명 : for문을 이용한 곱셈표 출력 프로그램
# 프로그램 목적 및 기능: for문을 이용해서 1단부터 12단 *12 값까지 곱셈표를 출력한다.
# 프로그램 작성자 : 신대홍(2022년 3월 19일)
# 최종 Update : Version 1.0.0, 2022년 3월 19일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/19     v1.0.0       최초작성

multiplicate = 12
multiplication = 12
for i in range(1, multiplicate + 1):
    for j in range(1, multiplication + 1):
        print("%2d * %2d = %4d," %(i , j,i*j), end = " ")
    print()