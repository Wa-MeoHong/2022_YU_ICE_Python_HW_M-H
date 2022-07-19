# 파일명 : HomeWork 6-1
# 프로그램 목적 및 기능: 미리 만들어둔 MyList.py를 모듈로써 불러와 함수 실행
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

import MyList as Rand #만들어둔 MyList 모듈 호출

print(Rand) #경로 출력

L = [] # L(리스트 설정)
SIZE = 100 # SIZE 설정 

Rand.genBigRandList(L,SIZE)
Rand.printListSample(L, SIZE, 10, 5)

input() # 명령프롬프트가 끝나는 것을 방지하기 위함