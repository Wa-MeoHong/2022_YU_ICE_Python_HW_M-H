# 파일명 : Calculate days from Jan01AD01 
# 프로그램 목적 및 기능: 년, 월, 일을 입력받고, 서기1년1월1일부터 며칠이 지났는지
#                   계산을 거친 후, 지난날과 그날의 요일을 출력하는 프로그램
#                   AD01/01/01은 월요일이다.
# 프로그램 작성자 : 신대홍(2022년 3월 19일)
# 최종 Update : Version 1.0.0, 2022년 3월 19일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/19     v1.0.0       최초작성


monthday = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 월 날수 리스트
weekday = ["SUN", "MON", "TUE", "WEN", "TUR", "FRI", "SAT"] # 요일 출력위한 리스트

while (1): # 무한반복(0 0 0 입력할 때 까지)
    days = 0 # 반복할 때마다 계산된 날수 0일로 초기화
    days_string = list(input("input year, month, day : ").split()) #입력한 문자열을 리스트에 각각 맵핑
    year, month, day = map(int, days_string) #리스트에 담긴 문자열을 정수로 변환해 각각의 변수에 맵핑
    if year == 0 and month == 0 and day == 0 : # 0 0 0 입력시 반복문 끝
        break
    print("Input yr_mn_dy_strings : ", days_string) # 입력한 날 출력

    for i in range(1, year): # 지나간 년도에 따라 1년씩 추가
        if ((i % 4 == 0 and i % 100 != 0) or i % 400 == 0): days += 366 # 윤년일시 366일 추가
        else: days += 365 #아니면 365일 추가

    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0): monthday[2] = 29 #입력한 년이 윤년일시 2월을 29일로 설정
    else : monthday[2] = 28 #아니면 28일로 초기화

    for j in range(1, month):
        days += monthday[j] #지나간 달만큼 달의 일수를 더함
    days += day #남은 일수 더함
    print("Day (year({0:}), month({1:}), day({2:})) : weekday({3:s}), elapsed {4:d} days from Jan01AD01".format(year, month, day, weekday[days % 7], days-1))
    # 출력, 요일은 days를 그대로 쓰고, 지나간날은 days에서 1일 뺌
