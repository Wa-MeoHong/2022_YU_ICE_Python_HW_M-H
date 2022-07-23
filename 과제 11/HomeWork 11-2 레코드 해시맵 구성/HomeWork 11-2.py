# 파일명 : HomeWork 11-2.py
# 프로그램 목적 및 기능: 학생 정보 레코드의 HashMap 구성 및 검색
# 프로그램 작성자 : 신대홍(2022년 5월 22일)
# 최종 Update : Version 1.0.0, 2022년 5월 22일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/22     v1.0.0       최초작성

import myHashMap

def main():
    HashMap_Capacity = 7 # 해시 맵의 버킷 개수

    print("Creating a HashMap of Capacity ({})".format(HashMap_Capacity))
    hsMap = myHashMap.HashMap(capacity=HashMap_Capacity) # 해시맵을 생성함
    Entries = [("Kim", 19345, "ICE", 4.0), ("Park", 18234, "CS", 4.2), ("Hong", 20456, "EE", 3.9),\
            ("Lee", 20987, "ME", 3.8), ("Yoon", 21654, "ICE", 3.7), ("Moon", 21001, "CHEM", 4.1),\
            ("Hwang", 21123, "CE", 3.7), ("Choi", 19003, "EE", 4.3), ("Yeo", 20234, "ME", 3.8),\
            ("Jeong", 18005, "PH", 4.3)] #Entry로 사용할 학생 리스트
    for i in range(len(Entries)): #학생 리스트를 해시맵에 집어넣는다.
        entry = Entries[i] 
        key = entry[0]
        hsMap._setitem(key, entry)
        print("Entry[{:2}] : {}".format(i, Entries[i])) #엔트리 됨
    print("Current HashMap Internal Structure:\n", hsMap)

    print("Checking entry searching in HashMap") #해시맵에 있는 엔트리된 학생수를 서치
    while True:
        key = input("Input student name to search (. to quit) : ") #.입력 전까지
        if (key == '.'):
            break
        v = hsMap._getitem(key) # 해시맵에서 입력한 key를 통해 학생 리스트를 찾아서 가져온다
        if v == None:
            print("key ({}) is not found in hashmap !!".format(key)) #없으면 없다고 출력
        else:
            print("key ({}) : Value ({})".format(key,v)) #찾으면 키와 학생리스트를 출력한다.
#

if __name__ == "__main__":
    main()