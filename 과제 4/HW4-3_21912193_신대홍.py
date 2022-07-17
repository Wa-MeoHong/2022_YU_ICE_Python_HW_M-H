# 파일명 : Print time using Tuple
# 프로그램 목적 및 기능: 시, 분 초를 받는 튜플을 작성하고, 그 튜플을 묶은 리스트를
#           출력하고, 정렬한 후 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 3월 26일)
# 최종 Update : Version 1.0.0, 2022년 3월 26일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/26     v1.0.0       최초작성

L_time = [] #리스트 선언

for i in range(0, 10):                                  # 10번 반복
    (hour, minute, second) = tuple(map(int, \
    input("input hour, minute, second : ").split()))    # input된 문자열을 int형으로, tuple에 넣음
    L_time.append((hour, minute, second))               # 이렇게 만들어진 튜플을 L_time리스트에 넣음
    print("L_time = ", L_time)                          # 리스트 출력

print("After sorted L_time = \n", sorted(L_time))       # 최종 결과 리스트를 오름차순 정렬 후 출력
