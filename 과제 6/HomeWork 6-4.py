# 파일명 : HomeWork 6-4
# 프로그램 목적 및 기능: 병합정렬과 선택정렬의 시간차이를 계산해서 출력
# 프로그램 작성자 : 신대홍(2022년 4월 9일)
# 최종 Update : Version 1.0.0, 2022년 4월 9일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/09     v1.0.0       최초작성

import sys #다른 경로에 있는 모듈을 불러오기 위한 sys모듈
myPyPK_dir = "C:/MyPyPackage/myModules" # 파일 경로 설정 
sys.path.append(myPyPK_dir) #지정된 경로를 추가해준다.
#이게 있으면 import할때 다른 폴더명을 추가로 쓸일이 없다.

import MyList as Rand
import MySortings as Sort
from time import *
print(Rand)
print(Sort)

L = []
SIZE = int(input("\nsize of list (0 to terminate) = "))
if SIZE == 0:
     exit()
Rand.genBigRandList(L,SIZE) #난수발생

#병합정렬 시간 측정
print("\nList (SIZE : %d) before merge sorting : " %SIZE) 
Rand.printListSample(L, SIZE, 10, 2)
t1 = time()
L = Sort.mergeSort(L)
t2 = time()
print("\nList(SIZE : %d) After merge sorting : " %SIZE)
Rand.printListSample(L, SIZE, 10, 2)
print("Merge Sorting for list of {} integers took {} sec" \
     .format(SIZE, t2-t1)) 
#병합정렬 후 셔플
Rand.suffleList(L,SIZE)
#선택정렬 후 시간 측정
print("\nList (SIZE : %d) before Selection sorting : " %SIZE)
Rand.printListSample(L, SIZE, 10, 2)
t1 = time()
Sort.selectionSort(L)
t2 = time()
print("\nList(SIZE : %d) After Selection sorting : " %SIZE)
Rand.printListSample(L, SIZE, 10, 2)
print("Selection Sorting for list of {} integers took {} sec" \
     .format(SIZE, t2-t1))
