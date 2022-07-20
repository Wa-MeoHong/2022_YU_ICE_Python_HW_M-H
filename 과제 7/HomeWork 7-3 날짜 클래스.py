# 파일명 : HomeWork 7-3
# 프로그램 목적 및 기능: 클래스 Date를 만들어 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 4월 16일)
# 최종 Update : Version 1.5.0, 2022년 4월 17일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/16     v1.0.0       최초작성
#     신대홍     2022/04/17     v1.0.1       주석문 일부 추가
#     신대홍     2022/04/17     v1.5.0       오류값은 출력안하도록 수정

from Classes import Date #클래스를 만들어서 따로 파일로 저장한 후, 불러옴
if __name__ == "__main__":
    dates = [
        Date(2000, 9, 15), Date(2020, 2, 29), Date(1998, 12, 3),
        Date(2002, 3, 5), Date(2020, 1, 30), Date(1836, 12, 21),
        Date(1945, 8, 15), Date(1122, 7, 31), Date(2022, 4, 16),
        Date(1998, 11, 21)
    ]
    
    print("dates before sorting : ") #정렬 전 날짜 출력
    for d in dates: #날짜 출력 
        if d.Year == -1 or d.Month == -1 or d.Day == -1:
            continue #날짜에 오류값이 있으면 출력 X
        print(d) 
    
    dates.sort() 
    print("\ndates after sorting : ") #정렬 후 날짜 출력
    for d in dates: #날짜 출력
        if d.Year == -1 or d.Month == -1 or d.Day == -1:
            continue #날짜에 오류값이 있으면 출력 X
        print(d)
