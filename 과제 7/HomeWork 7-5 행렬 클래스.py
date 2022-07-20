# 파일명 : HomeWork 7-5
# 프로그램 목적 및 기능: 클래스 Matrix를 만들어 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 4월 16일)
# 최종 Update : Version 1.0.0, 2022년 4월 16일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/16     v1.0.0       최초작성

from Classes import Matrix
if __name__ == "__main__":
    La = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    Lb = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
    Lc = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]

    mA = Matrix("mA", 3, 5, La)
    print(mA)
    mB = Matrix("mB", 3, 5, Lb)
    print(mB)
    mC = Matrix("mC", 5, 3, Lc)
    print(mC)

    mD = mA + mB 
    mD.setName("mD = mA + mB") # 이름 설정
    print(mD)
    mE = mA - mB #__sub__(self, other)
    mE.setName("mE = mA - mB") # 이름 설정
    print(mE)
    mF = mA * mC #__mul__(self, other)
    mF.setName("mF = mA * mB") # 이름 설정
    print(mF)