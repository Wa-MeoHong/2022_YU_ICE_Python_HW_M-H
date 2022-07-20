# 파일명 : HomeWork 8-1.py
# 프로그램 목적 및 기능: 파일로부터 국가의 정보(이름, 수도, 인구수, 면적)을 입력받아
#               출력한 후, 인구수 기준으로 내림차순으로 정렬 후 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 4월 30일)
# 최종 Update : Version 1.0.0, 2022년 4월 30일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/30     v1.0.0       최초작성

def printLst(coL): #출력 양식 함수
    print("===========================================================================")
    print(" No : {0:<20s} {1:<15s} {2:>15s} {3:>15s}"\
        .format("Name", "Capital", "Num_people", "Area[km²]")) # 이름, 수도, 인구수, 면적을 형식에 맞게 출력
    print("---------------------------------------------------------------------------")

    for i in range(0, len(coL)):
        print(" {0:>2d} : {1:<20} {2:<15} {3:>15d} {4:>15d}"\
            .format(i, coL[i][0], coL[i][1], coL[i][2], coL[i][3]))
    #format형은 str(문자열)만을 출력하기에 정수들을 전부 문자형으로 형변환하고 출력,
    #자리수를 지정해주어 출력 크기를 지정해준다.
    print("===========================================================================")
    print()
#
def main():
    dataFile = "demography.txt" #파일 이름
    fin = open(dataFile, 'r') #읽기상태로 열기
    contryLst = [] #읽은 자료를 담아주는 리스트 contryLst

    for line in fin.readlines(): #파일을 한 줄 읽어서 읽은 줄이 없을 때까지 진행
        Name, Capital, Nuw_people, Area = line.split() #읽은 line을 공백칸을 기준으로 split하여 변수들에 담아준다.
        temp = [Name, Capital, int(Nuw_people), int(Area)] #나눈 변수들을 이용해 하나의 리스트로 만듦
        contryLst.append(temp) #그 리스트를 contryLst에 담아준다.

    print("Input List of Contry: ")
    printLst(contryLst) #출력
    Sorted_contries = sorted(contryLst, key = lambda x : x[2], reverse = True)
    #정렬, sorted(정렬할 리스트, 기준값(리스트내의 요소 중 사용할 기준) : 작은 리스트의 3번째값(인구수), 내림차순)
    print("List of Contries sorted bt demography(number of people): ")
    printLst(Sorted_contries) #출력
    fin.close() #파일 닫기

if __name__ == "__main__":
    main()