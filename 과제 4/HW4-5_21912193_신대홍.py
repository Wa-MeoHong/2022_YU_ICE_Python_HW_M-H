# 파일명 : Print country in dictionary
# 프로그램 목적 및 기능: 10개 정도의 나라와 수도를 입력해서 그걸로 dictionary를
#               만든 후에, 나라를 입력하면 수도가 출력되게 하는 프로그램 
# 프로그램 작성자 : 신대홍(2022년 3월 26일)
# 최종 Update : Version 1.0.0, 2022년 3월 26일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/26     v1.0.0       최초작성

L_Country = []                              # 리스트 생성

while 1:                                    # 나라와 수도에 . 입력하기 전까지 무한반복
    (country, capital) = tuple(map(str,input("input country, capital : ").split())) # 나라와 수도를 입력받아 튜플로써 생성
    if( country == '.' or capital == '.'):  # 만약 나라나 수도에 '.'을 입력하면 종료
        break
    L_Country.append((country, capital))    # 튜플을 리스트에 집어넣음

D_Country = dict(L_Country)                 # 만들어진 리스트를 Dictionary로 생성
print("D_Country = ", D_Country)            # 딕셔너리 출력

while 1:                                    # 종료하기 전까지 반복
    country = input("input nation to find its capital (. to quit) : ")
    if(country == '.'):                     # 나라에 '.'입력시 종료
        break
    else: 
        if (country in D_Country):          # 만약 나라가 Dictionary 안에 있으면 출력
            print("the capital of {} is {} ".format(country, D_Country[country])) # 딕셔너리 출력
        else:                               # 아니면 없다고 출력
            print("It's not in this dictionary")