# 파일명 : Homework5_2.py
# 프로그램 목적 및 기능: 정수형 랜덤 리스트 생성 후, 병합정렬을 통해 정렬하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 4월 3일)
# 최종 Update : Version 1.0.0, 2022년 4월 3일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/03     v1.0.0       최초작성

from random import *
import time as t

LINE_SIZE = 10

def genBigRandList(BigR, SIZE): # 랜덤한 난수 발생 함수
    i = 0
    while i < SIZE:
        rand = choice(range(0,SIZE))
        if rand in BigR:
            continue
        BigR.append(rand)
        i += 1
        
#
def printListSample(L_BigRand, LINE_SIZE, Print_Lines): #난수 리스트 출력 
    SIZE = len(L_BigRand)

    if (SIZE <= 50): #만약 리스트의 개수가 50개 이하인 경우는 그냥 10개씩 출력하게함
        for k in range(0, SIZE // LINE_SIZE + 1):
            for j in range(0, LINE_SIZE):
                if ((10*k + j) == SIZE):
                    break
                print("%8d" %(L_BigRand[k*10+j]), end = "") 
            print()
    else: #만약 아니라면
        for k in range(0, Print_Lines) : # 처음 두줄을 먼저 출력
            for j in range(0, LINE_SIZE):
                print("%8d" %(L_BigRand[k*10+j]), end = "")
            print()
        count = SIZE - (Print_Lines * LINE_SIZE) 
        print("\t . . . . . .") # . . . 을 출력
        for k in range(0, Print_Lines) : #마지막 두줄 출력
            for j in range(0, LINE_SIZE): 
                print("%8d" %(L_BigRand[count+k*10+j]), end = "")
            print()
#
def merge(L_left, L_right):  #병합 정렬 하기 위한 함수
    L_res = []
    i, j = 0, 0
    len_left, len_right = len(L_left), len(L_right) #왼, 오른쪽 리스트의 길이
    
    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]: 
            L_res.append(L_left[i]) #만약 왼쪽 리스트에 있는 것이 작다면 왼쪽리스트에 있는 걸 추가 
            i += 1 
        else:
            L_res.append(L_right[j]) #아니면 오른쪽
            j += 1 

    while (i < len_left): # 나머지 요소를 추가해준다. 
        L_res.append(L_left[i]) # 왼쪽요소 추가
        i += 1
    while (j < len_right): # 오른쪽 요소도 추가 해준다.
        L_res.append(L_right[j])
        j += 1
    return L_res #이제 반환
#
def mergeSort(L): #병합정렬 함수
    if len(L) < 2:
        return L[:] #2개 이하면 그냥 출력
    else:
        middle = len(L) // 2 #중간지점(나눌부분)찾음
        L_left = mergeSort(L[:middle]) #처음엔 가장 작은 부분(왼쪽 2개)부터 시작해서 점점 늘어감
        L_right = mergeSort(L[middle:]) 
    return merge(L_left, L_right) #정렬 시작
#


# 퀵정렬 (Quick Sort)
def Partition(L, L_left, L_right, P_I): # P_I의 좌측엔 P_I의 값보다 작은값, 우측엔 더 큰값으로 만드는 함수
    P_V = L[P_I] #먼저 P_I의 값을 L의 가장 우측으로 밀어버리고, 그 맨 우측의 값을 인덱스P_I의 위치에 옮긴다.
    L[P_I] = L[L_right]
    L[L_right] = P_V
    # SWAP 끝

    newPI = L_left # 새로운 P_I를 저장

    for i in range(L_left, L_right): # 범위 내에서
        if(L[i] <= P_V): # P_V = L[P_I]의 값보다 작다면
            temp = L[i] # 값 교환이 일어남. (작으면 왼쪽으로 이동함.)
            L[i] = L[newPI]
            L[newPI] = temp
            newPI += 1 # Swap이 일어난 후, newPI가 갱신된다. 
    
    P_V = L[L_right] #newPI를 모두 갱신된 후에는 맨 우측으로 옮겨놓았던 P_I의 값을 다시 제자리로 보냄
    L[L_right] = L[newPI]
    L[newPI] = P_V

    return newPI #모든 작업이 끝난후 반환한다.
#

def Quick_Sorting(L, L_left, L_right): #퀵정렬 본함수
    if (L_left >= L_right): #만약 Left와 Right가 같거나 Left가 더 커진다면
        return # 다시 돌아간다. 
    else:
        #P_I = Pivot_Index (기준 인덱스 번호, 주로 Left, Right의 중간) 
        P_I = (L_left + L_right) // 2 #인덱스번호는 정수이므로 //를 통해 내림연산을 해준다.

    New_P_I = Partition(L, L_left, L_right, P_I)

    if(L_left < (New_P_I - 1)):
        Quick_Sorting(L, L_left, New_P_I-1)
    if((New_P_I + 1) < L_right):
        Quick_Sorting(L, New_P_I+1, L_right)
#

def QuickSort(L): #퀵정렬 초기 시작함수
    L_SIZE = len(L)
    Quick_Sorting(L, 0, L_SIZE-1)

L_BigR = []
SIZE = int(input("Input size of random list L (-1 to quit) = "))
if (SIZE == -1):
    exit(-1)
genBigRandList(L_BigR, SIZE) # 중복되지 않는 난수 리스트 작성
print("\n Before mergeSort of L : ") 
printListSample(L_BigR, 10, 3) # 리스트 출력(정렬 X)
print("\n After mergeSort of L : ")
start = t.time() #시간측정(정렬전)
QuickSort(L_BigR)
finish = t.time() #정렬후 시간측정
printListSample(L_BigR, 10, 3) #정렬후 리스트 출력
print("mergeSort () for list L (size = %d) took %lfsec" %(SIZE, finish-start))
