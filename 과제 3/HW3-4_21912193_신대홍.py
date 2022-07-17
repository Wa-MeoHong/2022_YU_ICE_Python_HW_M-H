# 파일명 : Print calender 
# 프로그램 목적 및 기능: 출력하고 싶은 년, 달을 입력하여 달력을 출력하게 하라.
# 프로그램 작성자 : 신대홍(2022년 3월 19일)
# 최종 Update : Version 1.0.0, 2022년 3월 19일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/19     v1.0.0       최초작성


monthday = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 월 날수 리스트
weekday = ["SUN", "MON", "TUE", "WEN", "TUR", "FRI", "SAT"] # 요일 출력위한 리스트
month_name = ["" , "January", "Febrary", "March", "April", "May", "June",
 "July", "August", "September", "October", "November", "December" ] 
 # 달의 영어이름 

days = 0
day = 1 # 반복할 때마다 계산된 날수 0일로 초기화, day는 1일 고정
days_string = list(input("input year, month : ").split()) #입력한 문자열을 리스트에 각각 맵핑
year, month= map(int, days_string) #리스트에 담긴 문자열을 정수로 변환해 각각의 변수에 맵핑

for i in range(1, year): # 지나간 년도에 따라 1년씩 추가
   if ((i % 4 == 0 and i % 100 != 0) or i % 400 == 0) : days += 366 # 윤년일시 366일 추가
   else: days += 365 #아니면 365일 추가

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) : monthday[2] = 29 #입력한 년이 윤년일시 2월을 29일로 설정
else : monthday[2] = 28 #아니면 28일로 초기화

for j in range(1, month) :
    days += monthday[j] #지나간 달만큼 달의 일수를 더함
days += day #남은 일수 더함

#달력 출력
print( "            {0:s} of Year {1:d}".format(month_name[month], year)) #몇년 몇월자
print("=============================================")
for k in range(0, 7):
    print("{0:>6}".format(weekday[k]), end = "") # 요일 출력
print()
print("---------------------------------------------")

for i in range(0, days%7):  print("{0:>6}".format(" "), end = "") # 시작일까지 공백 출력
for j in range(1, monthday[month]+1): #날 출력 시작
    if( days % 7 == 0) : print() #일요잃이면 한줄 엔터
    print("{0:>6}".format(j), end = "") # 날 입력
    days += 1 #days 갱신
print()
print("=============================================")
