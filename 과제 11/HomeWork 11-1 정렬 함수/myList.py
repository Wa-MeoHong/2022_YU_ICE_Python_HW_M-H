# 파일명 : myList.py
# 프로그램 목적 및 기능: 정수형 랜덤 리스트 생성, 난수를 출력하는 함수를 담은 파일
# 프로그램 작성자 : 신대홍(2022년 5월 22일)

from random import *

def genBigRandList(BigR, SIZE): # 랜덤한 난수 발생 함수
    i = 0
    while i < SIZE:
        BigR.append(i) # i를 BigR리스트에 넣어준 후, i를 증가
        i += 1
    shuffle(BigR) #셔플
        
#
def printListSample(L_BigRand, LINE_SIZE, Print_Lines): #난수 리스트 출력 
    SIZE = len(L_BigRand)

    if (SIZE <= 50): #만약 리스트의 개수가 50개 이하인 경우는 그냥 10개씩 출력하게함
        for k in range(0, SIZE // LINE_SIZE + 1):
            for j in range(0, LINE_SIZE): 
                if ((10*k + j) == SIZE): # 만약 배열을 출력할 때 배열에 끝에 도달했다면
                    break #바로 중지
                print("%8d" %(L_BigRand[k*10+j]), end = "") 
            print()
    else: #만약 아니라면
        for k in range(0, Print_Lines) : # 처음 Print_Lines만큼을 먼저 출력
            for j in range(0, LINE_SIZE):
                print("%8d" %(L_BigRand[k*10+j]), end = "")
            print()
        count = SIZE - (Print_Lines * LINE_SIZE) 
        print("\t . . . . . .") # . . . 을 출력
        for k in range(0, Print_Lines) : #마지막 Print_Lines만큼 출력
            for j in range(0, LINE_SIZE): 
                print("%8d" %(L_BigRand[count+k*10+j]), end = "")
            print()
#
