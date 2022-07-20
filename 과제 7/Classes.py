# 파일명 : Classes.py
# 프로그램 목적 및 기능: 만들어둔 클래스들을 불러오기 위한 파일
# 프로그램 작성자 : 신대홍(2022년 4월 15일)
# 최종 Update : Version 2.5.0, 2022년 4월 16일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/15     v1.0.0       최초작성(Class Person 추가)
#     신대홍     2022/04/15     v2.0.0       Class Date 추가
#     신대홍     2022/04/16     v2.1.0       Class Time 추가
#     신대홍     2022/04/16     v2.5.0       Class Matrix 추가, Data 클래스 버그 수정

class Person : #Person 클래스
    def __init__(self, Name, Births, Age) :
    #Name(이름), #Births(주민등록 앞자리), Age(나이)
        self.setName(Name)
        self.setBirths(Births) 
        self.setAge(Age)

    def setName(self, name): #이름을 분리
        self.Name = name 

    def setBirths(self, births): #생일을 분리
        self.Births = births

    def setAge(self, ag): #나이 확인 및 변수로 집어 넣어줌
        if (0 <= ag <= 100): #나이가 0부터 100살까지 범위
            self.Age = ag
        else :
            print("** Error in setting age (name:{}, age:{})".format(self.Name, ag))
            self.Age = -1
            #입력 오류로 -1을 출력 

    def __str__(self):
        return "Person({}, {}, {})".format(self.Name, self.Births, self.Age)
# ------------------------------------------------------------------------------
class Date: #날짜 클래스 
    def __init__(self, Year, Month, Day): # 초기값 설정
        self.setYear(Year)
        self.setMonth(Month) 
        self.setDay(Day)

    #값을 불러오기 위한 함수들 get~~
    def getYear(self): 
        return self.Year
    def getMonth(self):
        return self.Month
    def getDay(self):
        return self.Day

    # 변수에 값을 집어넣기 위한 함수들 set~
    def setYear(self, yr): #1년 이상만 (기원전, 0년 = Error(-1) )
        if (yr >= 1):
            self.Year = yr
        else: 
            print(" Error! Month({})".format(yr))
            self.Year = -1

    def setMonth(self, mn): #1월 ~ 12월 일때만 넣고 나머지는 Error(-1)
        if (mn >= 1 and mn <= 12):
            self.Month = mn
        else: 
            print(" Error! Month({})".format(mn))
            self.Month = -1

    def setDay(self, dy): #day는 경우의 수가 많기 때문에 따로 서술 ,오류값은 -1출력
        months = self.Month
        y = self.Year
        # month가 4월, 6월, 9월, 11월 일 경우( 일수가  30일까지)
        if (self.Month == 4 or self.Month == 6 or self.Month == 9 or self.Month == 11):
            if (dy >= 1 and dy <= 30):
                self.Day = dy
            else:
                print(" Error! Date = {}-{}-{}".format(y, months, dy))
                self.Day = -1
        # month가 2월일 경우( 일수가  28일까지, 윤년의 경우 29일)
        elif (self.Month == 2):
            if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
                if(dy >= 1 and dy <= 29): #윤년의 경우
                    self.Day = dy
                else:
                    print(" Error! Date = {}-{}-{}".format(y, months, dy))
                    self.Day = -1
            else:
                if(dy >= 1 and dy <= 28): #윤년이 아닐 경우
                    self.Day = dy
                else:
                    print(" Error! Date = {}-{}-{}".format(y, months, dy))
                    self.Day = -1

        else: #나머지 월(일수가 31일)
            if (dy >= 1 and dy <= 31):
                self.Day = dy
            else: 
                print(" Error! Date = {}-{}-{}".format(y, months, dy))
                self.Day = -1

    def __str__(self): #출력 방식
        return "(%4d-%2d-%2d)" %(self.getYear(),self.getMonth(), self.getDay())

    def __lt__(self, other): #정렬을 하기 위한 조건 
        if (self.Year, self.Month, self.Day) <\
             (other.Year, other.Month, other.Day): #년, 월, 일 전부 작다면 true
            return True
        else: #어느것이라도 작지 않다면? False
            return False
#---------------------------------------------------------------------------------
class Time: # Time 클래스
    def __init__(self, Hour, Minute, Second):
        self.setHour(Hour)
        self.setMinute(Minute) 
        self.setSecond(Second)

    def getHour(self): #값을 불러오기 위한 함수들 get~~
        return self.Hour
    def getMinute(self):
        return self.Minute
    def getSecond(self):
        return self.Second

    def setHour(self, Hour): # 변수에 값을 집어넣기 위한 함수들 set~
        if (Hour >= 0 and Hour <= 23): # 시 대입 (0시 ~23시(오후 11시))
            self.Hour = Hour
        else: 
            print("Error! Hour({})".format(Hour)) # 만약 24시가 넘거나 음수 값이면 -1
            self.Hour = -1

    def setMinute(self, Minute): # 분 대입 (0분 ~59분)
        if (Minute >= 0 and Minute <= 59):
            self.Minute = Minute
        else: 
            print("Error! Minute({})".format(Minute)) # 만약 59분 넘거나 음수 값이면 -1 
            self.Minute = -1

    def setSecond(self, Second): # 초 대입 (0초 ~59초)
        if (Second >= 0 and Second <= 59):
            self.Second = Second
        else: 
            print("Error! Second({})".format(Second)) # 만약 59초 넘거나 음수 값이면 -1 
            self.Second = -1

    def __str__(self): #출력 형식
        return "(%2d:%2d:%2d)" % (self.getHour(), self.getMinute(), self.getSecond())

    def __lt__(self, other):
        if (self.Hour, self.Minute, self.Second) <\
             (other.Hour, other.Minute, other.Second): #시, 분, 초 전부 작다면 true
            return True
        else: #어느것이라도 작지 않다면? False
            return False

#------------------------------------------------------------------------------------------
class Matrix: # 행렬 클래스
    def __init__(self, name, row, col, Lst_data): #초기값 설정
        self.name = name
        self.row = row # 열 번호 (행 개수)
        self.col = col # 행 번호 (열 개수)
        lst_row = [] # 한 행을 완성하기위한 리스트 
        self.rows = [] # 행렬을 완성하기위한 리스트 (완성된 Lst_row를 여기 넣음) 
        index = 0
        for i in range(0, self.row): # 끝까지 반복
            for j in range(0, self.col): # 한 행을 만들기
                lst_row.append(Lst_data[index])
                index += 1
            self.rows.append(lst_row) # 완성된 한 행에 집어 넣음
            lst_row = [] # 초기화 
    def __str__(self):
        # 출력할 문자열을 완성하는 함수 
        print(self.name, "=")
        s = "\n"
        for i in range(0, self.row):
            for j in range(0, self.col):
                s += "{:3d}".format(self.rows[i][j]) #문자열을 하나씩 추가
            s += "\n" #한 행이 끝나면 엔터추가
        return s

    def __add__(self, other): #행렬 덧셈
        lst_res = [] 
        for i in range(0, self.row):
            for j in range(0, self.col):
                r_ij= self.rows[i][j] + other.rows[i][j] # 행렬 덧셈 진행
                lst_res.append(r_ij) # 리스트에 추가
        return Matrix("R", self.row, self.col, lst_res) #리스트를 행렬로 교체

    def __sub__(self, other): # 행렬 뺄셈
        lst_res = []
        for i in range(0, self.row):
            for j in range(0, self.col):
                r_ij= self.rows[i][j] - other.rows[i][j] # 행렬 뺄셈 진행
                lst_res.append(r_ij)
        return Matrix("R", self.row, self.col, lst_res) # 리스트를 행렬로 교체
    
    def __mul__(self, other): # 행렬 곱셈
        C_row = self.row # 결과 행렬의 열 = 첫번째 행렬의 열
        C_col = other.col # 결과 행렬의 행 = 두번째 행렬의 행
        
        lst_res = []
        for i in range(0, C_row):
            for j in range(0, C_col):
                r_ij = 0
                for k in range(0, self.col):
                    r_ij += self.rows[i][k] * other.rows[k][j] # 행렬 곱셈 
                lst_res.append(r_ij)
        return Matrix("R", C_row, C_col, lst_res) # 리스트 → 행렬

    def setName(self, name):
        self.name = name