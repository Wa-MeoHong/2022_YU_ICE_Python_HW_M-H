# 파일명 : HomeWork 11-1.py
# 프로그램 목적 및 기능: 정수형 랜덤 리스트 생성 후, 병합정렬을 통해 정렬하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 5월 22일)
# 최종 Update : Version 1.0.0, 2022년 5월 22일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/22     v1.0.0       최초작성

import time
import myList, mySortings

L = []

def main():
    SS_Limit = 50000 
    # 선택정렬은 개수가 많으면 너무나 많은 시간이 걸리기에 할수 있는 갯수에 제한을 검

    while True:
        print("\nComparisons of Sorting Algorithms") 
        L_SIZE = int(input("Input Array/List Size (0 to Quit) = ")) # L_SIZE입력
        if (L_SIZE == 0):
            break
        myList.genBigRandList(L, L_SIZE) # 입력한 갯수만큼 랜덤한 수 생성(중복은 없다)

        #Testing Selection Sort
        if (L_SIZE <= SS_Limit): #만약 L_SIZE가 50000 이하라면 선택정렬 진행
            L_res = L.copy() #원본훼손을 방지하기 위해 복사본을 사용한다.

            print("\nBefore Selection Sort of L : ") #정렬전 출력
            myList.printListSample(L, 10, 3)
            t1 = time.time() #정렬 전 시간 측정
            mySortings.SelectionSort(L_res) # L복사본을 선택정렬 한다.
            t2 = time.time() #정렬 후 시간 측정
            print("After Selection Sort of L . . .") #정렬된 L을 출력함
            myList.printListSample(L_res, 10, 3) #추력
            time_elapsed = t2- t1 # 걸린 시간 구함
            print("Selection Sorting took {0:.6f} sec".format(float(time_elapsed))) #걸린 시간 출력
        
        #Testing Merge Sort 
        L_res = L.copy() #얘도 복사본 사용한다.
        print("\nBefore Merge Sort of L :") #정렬 전 출력
        myList.printListSample(L, 10, 3) 
        t1 = time.time() # 정렬 전 시간 측정
        L_sorted = mySortings.mergeSort(L_res) # 병합정렬 진행 후 반환 받음
        t2 = time.time() # 정렬 후 시간 측정
        print("After Merge Sort of L . . .") # 정렬 후 출력
        myList.printListSample(L_sorted, 10, 3) # 출력
        time_elapsed = t2- t1 # 걸린 시간 구함
        print("Merge Sorting took {0:.6f} sec".format(float(time_elapsed))) #럴린 시간 출력

        #Testing Quick Sort 퀵정렬
        L_res = L.copy() # 복사본 사용
        print("\nBefore Quick Sort of L :") # 정렬 전 출력
        myList.printListSample(L, 10, 3) # 
        t1 = time.time()
        mySortings.QuickSort(L_res) # 복사본을 정렬
        t2 = time.time()
        print("After Quick Sort of L . . .") #L_res 과 L은 같은 리스트이므로 L_res를 정렬 후 출력
        myList.printListSample(L_res, 10, 3)
        time_elapsed = t2- t1 #걸린 시간 구함
        print("Quick Sorting took {0:.6f} sec".format(float(time_elapsed))) #걸린 시간 출력

#
if __name__ == "__main__": #메인함수 출력
    main()
