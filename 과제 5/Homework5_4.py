# 파일명 : Homework5_4.py
# 프로그램 목적 및 기능:  Fibonacci 수열을 신속하게 계산할 수 있도록 memo 기능을
#   포함하는 재귀함수 dynFibo(n)를 구성하고, 시작 (start), 끝 (end), 간격 (stride)의
#   정수를입력 받은 후 해당 순서의 피보나치 수열을 출력하는 프로그램을 작성하라.
# 프로그램 작성자 : 신대홍(2022년 4월 4일)
# 최종 Update : Version 1.1.0, 2022년 4월 4일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/03     v1.0.0       최초작성
#     신대홍     2022/04/04     v1.1.0       ms → μs로 수정

from time import * #시간 모듈 불러오기(time을 안써도되게 만듬)
FIBO_memo = dict() #피보나치를 작성할 때, 중복계산을 하지않도록 값을 저장해주는곳
#dictionary로 만들면 편하다 ex) dict A = (0 : a, 1 : b ,...)

def dynFibonacci(n):
    if n in FIBO_memo: # 만약 이미 계산한 값이 있다면
        return FIBO_memo[n] #그걸 가져와서 쓴다
    elif n == 0 or n == 1 : # 계산을 안했고, 만약 0, 1이라면
        FIBO_memo[n] = n #0과 1은 그대로 쓴다.
        return n #반환 
    else: # 피보나치 수열 2번째부터는 
        fibo = dynFibonacci(n-1) + dynFibonacci(n-2) #피보나치 공식
        FIBO_memo[n] = fibo #결과를 딕셔너리에 저장
        return fibo #반환
#

start, end, stride = map(int, input("input start, stop, step of Fibonacci Serise : ").split())
#start, end, stride (시작, 끝, 증감할 수)를 입력
for i in range(start, end+1, stride): #for문
    t_before = time() # 피보나치 계산전 시간 측정 
    fibo_i = dynFibonacci(i) # 계산
    t_after = time() # 피보나치 계산후 시간 측정 
    t_diff = (t_after - t_before) * 1000000
    # micro second로 계산하기 때문에 1000000을 곱한다.
    print("dynFibo(%3d}) = %25.0lf, took %.2lf[micro_sec]"\
        %(i, fibo_i, t_diff)) #출력
