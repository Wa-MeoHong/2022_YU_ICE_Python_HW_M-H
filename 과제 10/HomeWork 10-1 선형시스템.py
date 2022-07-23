# 파일명 : HomeWork 10-1.py
# 프로그램 목적 및 기능: 선형시스템의 해를 산출하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 5월 14일)
# 최종 Update : Version 1.0.0, 2022년 5월 14일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/14     v1.0.0       최초작성

import numpy as np # NumPy 라이브러리 호출

def main():
    LinearSys = np.array([[10, 10, 0, 0, 0], [1, -1, -1, 0, 0],\
        [0, 0, 1, -1, -1], [0, 10, -5, -10, 0], [0, 0, 0, 10, -10]], dtype=np.int32)
      # A = 선형 시스템 구조, 선형 시스템 구조는 아래에 있음
    Result = np.array([100, 0, 0, 0, 0 ], dtype=np.int32)
      # B = 선형시스템 출력 결과, 단위는 V(볼트), 아래참고

    print("\nLinearSys = \n", LinearSys) # 선형시스템 구조 출력
    print("Result = ", Result) # 선형시스템 출력 구조 출력

    Solution = np.linalg.solve(LinearSys, Result)
    # 유니버셜 함수 solve()를 이용해 선형시스템의 전류값(해)를 구한다.
    CheckResult = np.matmul(LinearSys, Solution)
    # 결과가 맞는지 LinearSys와 X(해)를 행렬곱하여 Result를 구해본다.

    print("\nSolution = ", Solution) # 선형 시스템 해(전류) 출력
    print("CheckResult = np.matmul(LinearSys, Solution) = \n", CheckResult) 
    # 검산결과 출력
#

if __name__ == "__main__": #메인문 출력
    main()

#선형 시스템 구조 
# 10I1 + 10I2                      = 100(V)
#   I1 -   I2 -   I3               = 0(V)
#      +      +   I3 -   I4 -   I5 = 0(V)
#        10I2 -  5I3 - 10I4        = 0(V)
#                    - 10I4 - 10I5 = 0(V)