# 파일명 : what time is it
# 프로그램 목적 및 기능: 시, 분, 초를 입력해서 지난 자정과의 시간차와 
#                      다음 자정과의 시간차를 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 3월 19일)
# 최종 Update : Version 1.0.0, 2022년 3월 19일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/19     v1.0.0       최초작성

Next_midnight = 24 * 3600 #다음날 자정
while(1):
    time = 0
    hour, minute, second = map(int,input("input hour min sec : \
(음수입력시 종료) ").split())
    if (hour < 0 or minute < 0 or second < 0):
        break
    print("Input time : (%02d:%02d:%02d)" %(hour, minute, second))
    time = hour * 3600 + minute * 60 + second
    print( "Elapsed second from last midnight = %d" %(time))
    print( "Elapsed second from last midnight = %d" %(Next_midnight - time))
