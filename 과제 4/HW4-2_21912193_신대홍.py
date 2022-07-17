# 파일명 : Print Date using Tuple
# 프로그램 목적 및 기능: 연,월, 일을 받는 튜플을 작성하고, 그 튜플을 묶은 리스트를
#           출력하고, 정렬한 후 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 3월 26일)
# 최종 Update : Version 1.0.1, 2022년 3월 30일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/26     v1.0.0       최초작성
#     신대홍     2022/03/30     v1.0.1       정렬전 리스트 출력

L_date = []                                         # 리스트 선언

for i in range(0, 10):                              # 10번 반복
    (year, month, day) = tuple(map(int, \
    input("input year, month, day : ").split()))    # input된 문자열을 int형으로, tuple에 넣음
    L_date.append((year, month, day))               # 이렇게 만들어진 튜플을 L_date리스트에 넣음
    print("L_date = ", L_date)                      # 리스트 출력
    
print("L_date = \n", L_date)                        # 정렬전 리스트 출력
print("After sorted L_date = \n", sorted(L_date))   # 최종 결과 리스트를 정렬 후 출력