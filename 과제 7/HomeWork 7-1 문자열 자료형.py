# 파일명 : HomeWork 7-1.py
# 프로그램 목적 및 기능: Person 클래스를 만들어 받은 리스트를 형식에 맞게 출력
# 프로그램 작성자 : 신대홍(2022년 4월 15일)
# 최종 Update : Version 1.0.0, 2022년 4월 15일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/15     v1.0.0       최초작성

from Classes import Person #클래스를 만들어서 따로 파일로 저장한 후, 불러옴

def printPersons(name, L_Person):
    print("{} : ".format(name))
    for p in L_Person:
        print("\t",p)
#------------------------------------------------------------------        
def main():
    L_Person = [
        Person("KIM J.S", 981111, 25),
        Person("JOO A.H", 950102, 28),
        Person("PARK D.Y", 970228, 26),
        Person("YOON J.H", 100312, 12),
        Person("JANG N.R", 950902, 28),
        Person("BAEK A.Y", 971211, 26),
        Person("JIN M.J", 991031, 24),
        Person("CHOI J.W", 830131, 39),
        Person("MOON T.E", 100000, 350),
        Person("Kim S.K", 980815, 25)
    ]
    #학생들 리스트 10명 
    printPersons("Persons", L_Person)

if __name__ == "__main__": #메인함수 출력
    main()