# 파일명 : HomeWork 10-3.py
# 프로그램 목적 및 기능: 주어진 리스트를 이용해 정규분포값을 구하고, 그래프로 표현
# 프로그램 작성자 : 신대홍(2022년 5월 14일)
# 최종 Update : Version 1.0.0, 2022년 5월 14일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/14     v1.0.0       최초작성

from numpy import * # NumPy 라이브러리 호출
import matplotlib.pyplot as plt # Matplotlib 패키지 호출

def Gauss(mu, std, X): # 정규분포값으로 변환시키는 함수 Gauss
    Y = 1.0/(std*(sqrt(2*pi))) * exp(-0.5 * pow((X-mu), 2) / pow(std, 2))
    # y = (1/σ√2π) * exp((-1/2) * (x - μ)² / σ²) 
    return Y # Y 반환
#
def GaussMu0(mu, X): # 평균이 0일때 표준편차에 따른 정규분포
    std = 2 # 표준편차가 2일 때
    Y1 = Gauss(mu, std, X) # 정규분포값 생성
    plt.plot(X, Y1, color="blue", label="std = 2.0") # 정규분포 그래프 생성

    std = 1 # 표준편차가 1일 때
    Y2 = Gauss(mu, std, X)  # 정규분포값 생성
    plt.plot(X, Y2, color="green", label="std = 1.0") # 정규분포 그래프 생성
    
    std = 0.5 # 표준편차가 0.5일 때
    Y3 = Gauss(mu, std, X) # 정규분포값 생성
    plt.plot(X, Y3, color="red", label="std = 0.5") # 정규분포 그래프 생성

    plt.title("21912193 Graph 1 - mu = 0.0, std = [0.5, 1.0, 2.0]")
    plt.legend(loc="best")
    plt.grid(True)
    plt.savefig("mu=0_GaussDist.png")
    plt.show() # 정규분포 그래프를 제목, 형식에 맞게 조정 후 출력
#

def GaussSTD1(std, X): # std = 1 일때 평균에 따른 정규분포
    mu = -2.0 # 평균이 -2.0일 때
    Y1 = Gauss(mu, std, X) # 정규분포값 생성
    plt.plot(X, Y1, color="red", label="mu = -2.0") # 정규분포 그래프 생성

    mu = 0.0 # 평균이 0.0일 때
    Y2 = Gauss(mu, std, X) # 정규분포값 생성
    plt.plot(X, Y2, color="green", label="mu = 0.0") # 정규분포 그래프 생성
    
    mu = 2.0 # 평균이 2.0일 때
    Y3 = Gauss(mu, std, X) # 정규분포값 생성
    plt.plot(X, Y3, color="blue", label="mu = 2.0") # 정규분포 그래프 생성

    plt.title("21912193 Graph 2 - mu = [-2.0, 0.0, 2.0], std = 1")
    plt.legend(loc="best")
    plt.grid(True)
    plt.savefig("std=1_GaussDist.png")
    plt.show() # 정규분포 그래프를 제목, 형식에 맞게 조정 후 출력
#

def main(): # 메인함수
    X = linspace(-8, 8, num=100, endpoint=True) # X의 리스트 생성(-8 ~ +8)까지, 100개
    while True:
        print("input normal distribution graph mode")
        print("  1. mu = 0.0, sigma = [0.5, 1.0, 2.0]")
        print("  2. mu = [-2.0, 0.0, 2.0], sigma = 1.0")
        print("  0. quit")
        mode = input("mode = ")
        if mode == "0":
            break
        elif mode == "1": #모드가 1이면 그래프 1 생성
            GaussMu0(0, X) # 평균이 0일때, 표준편차들에 대한 X의 정규분포
        else: #1도 0도 아니면 2번 그래프 생
            GaussSTD1(1, X) # 표준편차가 1일때, 평균들에 대한 X의 정규분포 구하기
#

if __name__ == "__main__": #메인함수 출력
    main()