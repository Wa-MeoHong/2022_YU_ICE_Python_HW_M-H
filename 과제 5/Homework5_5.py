# 파일명 : Homework5_5.py
# 프로그램 목적 및 기능: 행렬의 출력, 연산 프로그램
# 프로그램 작성자 : 신대홍(2022년 4월 3일)
# 최종 Update : Version 1.0.0, 2022년 4월 3일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/03     v1.0.0       최초작성


def printMtrx(M): #행렬 출력함수 
    LINE_ROW = len(M) #열의 개수 구하기
    LINE_COLUMN = len(M[1]) #행의 개수 구하기 
    for i in range(0, LINE_ROW):
        for j in range(0, LINE_COLUMN):
            print("%5d" %M[i][j], end = "") #출력, 행부터 먼저 출력후, 한줄엔터
        print()
#

def mtrxAdd(M1, M2): # 행렬 덧셈
    D = []
    result = 0
    LINE_ROW = len(M1) # 행렬이 둘다 행, 열이 같아야 덧셈, 뺄셈이 성립하므로
    # M1을 기준으로 행, 열 수를 구하면 된다.
    LINE_COLUMN = len(M1[1])

    for i in range(0, LINE_ROW):
        columns = []
        for j in range(0, LINE_COLUMN):
           result = M1[i][j] + M2[i][j] # 요소의 덧셈을 진행한 후,
           columns.append(result) # 값을 넣어주면서 행을 완성한다.
        D.append(columns) #그 후 완성된 행을 행렬에 집어넣고 반복
    return D # 다하면 반환해준다.
#

def mtrxSub(M1, M2): #행렬 뺄셈, 덧셈과 거의 동일하다.
    E = []
    result = 0
    LINE_ROW = len(M1)
    LINE_COLUMN = len(M1[1])

    for i in range(0, LINE_ROW):
        columns = []
        for j in range(0, LINE_COLUMN):
           result = M1[i][j] - M2[i][j]
           columns.append(result)
        E.append(columns)
    return E   

#

def mtrxMul(M1, M2): #행렬 곱셈 
    F = []
    F_LINE_COLUMNS = len(M2[1]) # 연산된 행렬의 행은 곱해지는(2번째)행렬의 행의 수와 같다
    F_LINE_ROWS = len(M1) # 연산된 행렬의 열은 곱하는(1번째)행렬의 열의 수와 같다
    Common_Line = len(M1[1]) # 공통된 부분( 1번째 행 수, 2번째 열 수)

    for i in range(0, F_LINE_ROWS):
        columns = [] #행을 넣는 곳을 여기서 초기화한다.
        for j in range(0, F_LINE_COLUMNS):
            result = 0 # 요소들 결과를 여기서 초기화
            for k in range(0, Common_Line):
                result += M1[i][k] * M2[k][j] # 요소의 곱을 더해주면서 F의 요소를 완성
            columns.append(result) # 행에 집어넣는다.
        F.append(columns) #그리고 그 행을 행렬F에 집어넣으면서 반복
    return F  # 반환
#-----------------------------------------------------------------------
def main():
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 1]]
    B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]]
    C = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]

    print("A = "); printMtrx(A) #행렬 A 출력
    print("B = "); printMtrx(B) #행렬 B 출력
    print("C = "); printMtrx(C) #행렬 C 출력

    D = mtrxAdd(A, B) #행렬 D 계산
    print("A + B= "); printMtrx(D) #행렬 D 출력
    E = mtrxSub(A, B) #행렬 E 계산
    print("A - B= "); printMtrx(E) #행렬 E 출력
    F = mtrxMul(A, C) #행렬 F 계산
    print("A * C= "); printMtrx(F) #행렬 F 출력

if __name__ == "__main__": 
    main() #메인 함수 출력
