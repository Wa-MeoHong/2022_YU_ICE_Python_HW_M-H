# 파일명 : HomeWork 8-3~4.py
# 프로그램 목적 및 기능: 파일로부터 행렬의 데이터를 읽어와서 행렬 연산하는 프로그램,
#           또한, json파일, pickle파일과의 크기 차이를 비교해본다.
# 프로그램 작성자 : 신대홍(2022년 4월 30일)
# 최종 Update : Version 2.0.0, 2022년 5월 1일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/01     v1.0.0       최초작성
#     신대홍     2022/05/01     v2.0.0       클래스 형식을 이용해 새로 제작

from Classes import Matrix

def FgetMtrx(fin): #파일 입력 함수(행렬까진 만들지 않음)
    
    Mtrx_row_col = fin.readline() # 파일에서 먼저 한줄 읽어옮
    while Mtrx_row_col == "\n": #만약 읽어온 값이 공백밖에 없으면(줄바꿈 포함)
        Mtrx_row_col = fin.readline() #다시 한줄을 읽어온다
    row, col = map(int, Mtrx_row_col.split()) #읽어온 행, 열의 값을 split하고 그값을 각각 대입
    Mtrx_Lst = []
    for i in range(0, row):
        num = fin.readline()
        Mtrx_Lst += list(map(float, num.split())) # 행렬 값을 읽어와 리스트에 담음

    return Mtrx_Lst, row, col #읽어온 행, 열의 값과 행렬리스트를 반환
#
def main ():
    InputMtrx = "matrix_data.txt"
    fin = open(InputMtrx, 'r') #파일을 먼저 열어준다

    La, a_row, a_col = FgetMtrx(fin)  #연 파일을 통해 리스트 A, B, C를 만든다
    Lb, b_row, b_col = FgetMtrx(fin)
    Lc, c_row, c_col = FgetMtrx(fin)

    mA = Matrix("mA", a_row, a_col, La)
    mB = Matrix("mB", b_row, b_col, Lb)
    mC = Matrix("mC", c_row, c_col, Lc)
    print(mA)
    print(mB)
    print(mC) #행렬 A, B, C출력

    mD = mA + mB #__add__(self, other)
    mD.setName("mD = mA + mB") # 이름 설정
    print(mD) #행렬덧셈 후 출력

    mE = mA - mB #__sub__(self, other)
    mE.setName("mE = mA - mB") # 이름 설정
    print(mE) #행렬뺄셈 후 출력

    mF = mA * mC #__mul__(self, other)
    mF.setName("mF = mA * mC") # 이름 설정
    print(mF) #행렬곱셈 후 출력

    fin.close() #파일 닫기
#----------------------------------------------------------------------------
    #JSON 텍스트파일 과 pinkle 이진 파일 크기비교
    from Classes import CustomEncoder #Classes.py에서 클래스를 끌어옴
    import os
    import json #json파일을 만들기 위한 라이브러리
    import pickle #이진파일을 만들기위한 라이브러리

    f_json = open("mA_json.txt", "w") #JSON파일을 생성
    json.dump(mA, f_json, indent=4, cls=CustomEncoder) #파이썬 객체를 json문자열로 변환하여 집어넣음
    f_json.close()
    size_f_json = os.path.getsize("mA_json.txt") #크기 측정
    print("size of mA_json.txt = ", size_f_json) #사이즈 출력

    f_pickle = open("mA_pickle.bin", "wb") #이진파일(pickle 파일) 생성
    pickle.dump(mA, f_pickle) #파이썬 객체를 pickle(이진파일)형식으로 변환
    f_pickle.close()
    size_f_pickle = os.path.getsize("mA_pickle.bin") #사이즈 측정
    print("size of mA_pickle.bin = ", size_f_pickle) #사이즈 출력

    f_mtrx_p = open("mA_pickle.bin", "rb") #아까 만든 pickle 파일을 불러옴
    mG = pickle.load(f_mtrx_p) #파일에 있는 내용을 파이썬 객체로 변환하여 읽어옴
    mG.setName("mG")
    print(mG) #출력 
    f_mtrx_p.close()
#
if __name__ == "__main__":
    print("Executing main()")
    main()