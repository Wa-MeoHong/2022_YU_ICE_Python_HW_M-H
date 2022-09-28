# 파일명 : MyList.py
# 프로그램 목적 및 기능: 큰 난수 발생,출력, 셔플 모듈용 파일
# 프로그램 작성자 : 신대홍(2022년 4월 9일)
# 최종 Update : Version 1.0.0, 2022년 4월 9일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/09     v1.0.0       최초작성

from random import *
#========================================================================
def genBigRandList(L, SIZE): # 랜덤한 난수 발생 함수
    i = 0
    while i < SIZE:
        rand = randint(0,SIZE-1) #0~SIZE까지 범위 내에서 랜덤하게 정수 하나 생성
        if rand in L: #이미 한번 발생되었던 난수라면 다시 발생
            continue
        L.append(rand)
        i += 1
#========================================================================
def printListSample(L, SIZE, per_line, sample_line): #난수 리스트 출력 
    if (SIZE <= 50):  #사이즈가 50개 미만이라면 이것만 출력
        sample_line = SIZE // per_line

    #기본출력 
    for k in range(0, sample_line): 
        for j in range(0, per_line):
            print("%8d" %L[k*10+j], end = "")
        print()

    #추가출력
    if (SIZE >= 50):
        count = SIZE - (sample_line * per_line)
        print("\t . . . . . .")
        for k in range(0, sample_line) : 
            for j in range(0, per_line):
                print("%8d" %(L[count+k*10+j]), end = "")
            print()
#========================================================================
def suffleList(L,SIZE): #난수들의 순서를 섞어주는 함수(random.suffle 사용 X)
    i = 0
    while i < SIZE:

        s1 = randint(0,SIZE-1)
        s2 = randint(0,SIZE-1)

        temp = L[s1]
        L[s1] = L[s2]
        L[s2] = temp
        i += 1
