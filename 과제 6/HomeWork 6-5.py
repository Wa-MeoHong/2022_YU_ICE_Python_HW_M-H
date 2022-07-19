
# 파일명 : HomeWork 6-5
# 프로그램 목적 및 기능: MyMatrix 모듈을 불러와 행렬 연산 및 출력
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

import MyMatrix as Mtrx
print(Mtrx)
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 1]]
B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]]
C = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]

print("A = "); Mtrx.printMtrx(A) #행렬 A 출력
print("B = "); Mtrx.printMtrx(B) #행렬 B 출력
print("C = "); Mtrx.printMtrx(C) #행렬 C 출력

D = Mtrx.mtrxAdd(A, B) #행렬 D 계산
print("A + B= "); Mtrx.printMtrx(D) #행렬 D 출력
E = Mtrx.mtrxSub(A, B) #행렬 E 계산
print("A - B= "); Mtrx.printMtrx(E) #행렬 E 출력
F = Mtrx.mtrxMul(A, C) #행렬 F 계산
print("A * C= "); Mtrx.printMtrx(F) #행렬 F 출력