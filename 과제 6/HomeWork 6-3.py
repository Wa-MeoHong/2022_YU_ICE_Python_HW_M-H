# 파일명 : HomeWork 6-3
# 프로그램 목적 및 기능: array 모듈을 사용해 생성한 배열과 리스트의
#              정렬 시간차 출력 
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

from array import *
from time import *
import MyList as Rand #만들어둔 MyList 모듈 호출
import MySortings as Sort #만들어둔 MySortings 모듈 호출
print(Rand) #경로 출력
print(Sort) #경로 출력

AR = array('i') #int형 배열 AR하나 생성

L = []
SIZE = 50000
Rand.genBigRandList(L,SIZE) #난수발생

AR.fromlist(L) # 생성한 배엻 AR에 리스트를 넣어줌(배열에 삽입)

print("Array (SIZE : %d) before sorting : " %SIZE)
Rand.printListSample(AR, SIZE, 10, 2) #출력
t1 = time() #시간측정 1
Sort.selectionSort(AR) # 선택정렬 
t2 = time() #시간측정 2
print("\nArray (SIZE : %d) After sorting : " %SIZE)
Rand.printListSample(AR, SIZE, 10, 2) # 정렬 후 출력
print("Selection Sorting for array of {} integers took {} sec" \
     .format(SIZE, t2-t1)) #결과 출력

#위와 거의 동일, 그러나 리스트인점만 다름
print("\nList (SIZE : %d) before sorting : " %SIZE)
Rand.printListSample(L, SIZE, 10, 2)
t1 = time()
Sort.selectionSort(L)
t2 = time()
print("\nList(SIZE : %d) After sorting : " %SIZE)
Rand.printListSample(L, SIZE, 10, 2)
print("Selection Sorting for list of {} integers took {} sec" \
     .format(SIZE, t2-t1))
