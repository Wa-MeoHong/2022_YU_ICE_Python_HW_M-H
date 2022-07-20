# 파일명 : HomeWork 7-4
# 프로그램 목적 및 기능: 클래스 Time를 만들어 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 4월 16일)
# 최종 Update : Version 1.5.0, 2022년 4월 17일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/16     v1.0.0       최초작성
#     신대홍     2022/04/17     v1.5.0       만약 오류값이 있으면 출력 X 추가

from Classes import Time #클래스를 만들어서 따로 파일로 저장한 후, 불러옴
if __name__ == "__main__" : 
    times = [
        Time(23,59,59), Time(9, 0, 5), Time(12, 32, 5), Time(13, 43, 55),
        Time(0, 0, 0), Time(15,59,59), Time(15,55,2), Time(19,00,00),
        Time(12,59,60), Time(6,60,0)
    ]
    print("times before sorting : ") #정렬전 출력
    for t in times:
        if t.Hour == -1 or t.Minute == -1 or t.Second == -1:
            continue
            #만약 오류값이 있는 시간이라면 출력 X
        print(t)
    times.sort() #정렬

    print("\nimes after sorting : ") #정렬후 출력
    for t in times:
        if t.Hour == -1 or t.Minute == -1 or t.Second == -1:
            continue
            #만약 오류값이 있는 시간이라면 출력 X
        print(t)