# 파일명 : HomeWork 7-2
# 프로그램 목적 및 기능: Person을 상속받는 클래스 Student를 만들어 사용해보자
# 프로그램 작성자 : 신대홍(2022년 4월 15일)
# 최종 Update : Version 1.0.0, 2022년 4월 15일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/15     v1.0.0       최초작성

from Classes import Person #클래스를 만들어서 따로 파일로 저장한 후, 불러옴

class Student(Person): #Person의 클래스를 상속받은 class Student 
    def __init__(self, Name, Births, Age, St_id, Major, GPA):
        #St_id(학번), Major(전공), GPA(학점)
        Person.__init__(self, Name, Births, Age) #Person 클래스의 초기값 식을 그대로 가져와서 사용
        self.setSt_id(St_id) #나머지는 새로 지정
        self.setMajor(Major)
        self.setGPA(GPA)

    def setSt_id(self, st_id): #학번 저장
        self.St_id = st_id
    def setMajor(self, Major): #전공 저장, 전공이 ??면 None으로 출력하게 함
        if ( Major == "??"):
            print("** Error in setting Major (name:{}, major:{})".format(self.Name, Major))
            self.Major = "None"
        else:
            self.Major = Major
    def setGPA(self, GPA): #학점 출력
        self.GPA = GPA
    def __str__(self): #출력 형식 
        return "Students({}, {}, {}, {}, {}, {})"\
            .format(self.Name, self.Births, self.Age, self.St_id, self.Major, self.GPA)
#--------------------------------------------------------------------------------
def printStd(L_student): #리스트 출력
    for s in range(len(L_student)):
        print(L_student[s])
#
def compareStd(st1, st2, key): #key를 통해 학생 1과 학생 2를 비교
    if key == "st_id": 
        if st1.St_id < st2.St_id: #학번을 비교
            return True
        else:
            return False
    elif key == "GPA": # 학점을 비교
        if st1.GPA < st2.GPA:
            return True
        else:
            return False
    elif key == "name": # 이름을 비교
        if st1.Name < st2.Name:
            return True
        else:
            return False
#
def sortStd(L_student, key): # 학생 리스트 정렬 
    for i in range(0, len(L_student)):
        min_idx = i
        for j in range(i+1, len(L_student)):
            if compareStd(L_student[j], L_student[min_idx], key):
                min_idx = j
        if min_idx != i:
            L_student[i], L_student[min_idx] = L_student[min_idx], L_student[i]
#
def main(): #메인 함수
    students = [
        Student("KIM", 980203, 25, 13234, "EE", 4.1),
        Student("JOO", 971123, 26, 11021, "ME", 4.2),
        Student("PARK", 990930, 24, 12544, "CE", 3.7),
        Student("SHIN", 991023, 24, 12234, "ICE", 4.3),
        Student("MOON", 961112, 28, 15231, "ICE", 3.9),
        Student("MIN", 100000, 25, 12515, "??", 3.6),
        Student("AN", 991022, 24, 12114, "CE", 3.4),
        Student("CHOI", 971212, 26, 13412, "EE", 3.2),
        Student("BEAK", 990901, 24, 12151, "EE", 3.8),
        Student("CHOO", 980401, 25, 14312, "ICE", 3.8),
    ]
    print("Students before sorting : ") #정렬 전 학생 정보 출력
    printStd(students)
    #
    sortStd(students,"name")
    print("\nstudents after sorting by name : ")
        #이름을 기준으로 오름차순 정렬 후 출력
    printStd(students)
    #
    sortStd(students,"st_id")
    print("\nstudents after sorting by st_id : ")
        #학번을 기준으로 오름차순 정렬 후 출력
    printStd(students)
    #
    sortStd(students,"GPA")
    print("\nstudents after sorting by GPA : ")
        #성적을 기준으로 오름차순 정렬 후 출력
    printStd(students)
#
if __name__ == "__main__":
    main()
