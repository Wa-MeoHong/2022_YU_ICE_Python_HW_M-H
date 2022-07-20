# 파일명 : HomeWork 8-2.py
# 프로그램 목적 및 기능: 10명의 학생들의 성적 데이터를 파일로부터 입력받고
#           성적 합, 평균을 계산하고 출력과 파일출력, 과목별 평균도 게산 및 출력
#           하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 4월 30일)
# 최종 Update : Version 1.0.0, 2022년 4월 30일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/30     v1.0.0       최초작성

def Print_Stu(Stu): #출력 함수
    print("====================================================")
    print("{0:>5} : {1:>6} {2:>6} {3:>6} {4:>6} {5:>7} {6:>7}"\
        .format("Name", "Kor", "Eng", "Math", "Sci", "Sum", "Avg"))
    print("----------------------------------------------------")
    #기본 정보 출력
    for i in range(0, len(Stu)): #Students 리스트의 개수만큼 반복
        print("{0:>5} : {1:>6d} {2:>6d} {3:>6d} {4:>6d} {5:>7d} {6:>7.2f} "\
        .format(Stu[i][0], Stu[i][1], Stu[i][2], Stu[i][3], Stu[i][4], Stu[i][5], Stu[i][6]))
    #요소들을 출력
    print("====================================================")
    print()
#
def Calculate_Stu(Stu): #학생들의 점수 합계, 평균 계산
    for i in range(0, len(Stu)):
        Sum = Stu[i][1] + Stu[i][2] + Stu[i][3] + Stu[i][4]
        #Sum = 국어 + 영어 + 수학 + 과학
        Stu[i].append(int(Sum)) # 정수형으로 학생들 리스트요소에 집어넣어줌
        Avg = Sum / 4 #평균 계산
        Stu[i].append(float(Avg)) #실수형으로 집어넣음
#
def Calculate_Curri(Stu): #과목당 평균 계산
    Sum_Kor = Sum_Eng = Sum_Math = Sum_Sci = 0
    #합계들 초기값 설정
    for i in range(0, len(Stu)): #각 과목 합계들 계산
        Sum_Kor += Stu[i][1]
        Sum_Eng += Stu[i][2]
        Sum_Math += Stu[i][3]
        Sum_Sci += Stu[i][4]

    Avg_Cur = dict(Kor_avg = float(Sum_Kor/len(Stu)), Eng_avg = float(Sum_Eng/len(Stu)),\
        Math_avg = float(Sum_Math/len(Stu)), Sci_avg = float(Sum_Sci/len(Stu)))
    #평균을 게산해서, 딕셔너리 형태로 만들어서 Avg_Cur을 만듦
    print("Average score of each class : ")
    for Avgkey, AvgVal in Avg_Cur.items(): #Avg_Cur을 출력, 키와 아이템 따로따로 출력함
        print("{0:<8} = {1:>5.2f}".format(Avgkey, AvgVal))
    print()
#
def FilePrint_Stu(Stu): #파일 출력 함수
    Output = "output.txt"
    fout = open(Output, 'w') # 출력용 파일 오픈

    fout.write("{0:>5} : {1:>6}, {2:>6}, {3:>6}, {4:>6}, {5:>7}, {6:>7}\n"\
        .format("Name", "Kor", "Eng", "Math", "Sci", "Sum", "Avg"))
    fout.write("----------------------------------------------------\n")
    for i in range(0, len(Stu)):
        fout.write("{0:>5} : {1:>6d}, {2:>6d}, {3:>6d}, {4:>6d}, {5:>7d}, {6:>7.2f} \n"\
        .format(Stu[i][0], Stu[i][1], Stu[i][2], Stu[i][3], Stu[i][4], Stu[i][5], Stu[i][6]))
    #Print_Stu와 거의 같으나 print가 fout.write로 바뀜(C에선 fprintf와 비슷함)
    fout.close() #파일 닫기

def main(): #메인 함수
    DataFile = "student_records.txt" #파일 이름
    fin = open(DataFile, 'r')
    Students = []

    for line in fin.readlines(): #파일을 한 줄 읽어서 읽은 줄이 없을 때까지 진행
        Name, Kor, Eng, Math, Sci = line.split() #읽은 line을 공백칸을 기준으로 split하여 변수들에 담아준다.
        temp = [Name, int(Kor), int(Eng), int(Math), int(Sci)] #나눈 변수들을 이용해 하나의 리스트로 만듦
        Students.append(temp) #그 리스트를 contryLst에 담아준다.

    for i in range(0, len(Students)):
        print(Students[i])
    print()

    Calculate_Stu(Students) # 학생들 성적 평균 계산
    Print_Stu(Students) #출력
    Calculate_Curri(Students) #과목 평균 계산 및 출력
    FilePrint_Stu(Students) #학생 리스트 파일 출력
    fin.close() # 입력용 파일 닫기

if __name__ == "__main__":
    main() #메인함수 실행
