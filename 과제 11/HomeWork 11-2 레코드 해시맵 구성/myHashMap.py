# 파일명 : myHashMap.py
# 프로그램 목적 및 기능:  HashMap 등의 클래스를 만들어둔 파일
# 프로그램 작성자 : 신대홍(2022년 5월 22일)

# Entry 클래스
class Entry:
    def __init__(self,k,v): #초기값 설정
        self.key = k # Key 저장
        self.value = v # 값 저장

    def __str__(self): # 문자열 형태로 값을 반환하는 함수
        return str(self.value) 
#

def CyclicShiftHashCode(str_key): #문자열의 Hash값을 계산하기 위한 함수
    mask = (1 << 32) - 1 # == FFFF FFFF (16)
    h = 0
    for ch in str_key:
        h = ((h << 5) & mask | (h >> 27))
        h += ord(ch)
    return h

# Bucket 클래스
class Bucket(Entry): 
    def __init__(self):
        self._bucket = [] # 버킷을 리스트로 사용한다.

    def _getitem(self, k): # 버킷에 저장한 item에서 값을 찾아서 반환한다.
        for item in self._bucket: # key를 통해 item을 찾고, 
            if (k == item.key): # key가 안에 있으면
                return item.value #그 value 값을 반환한다
        return None #없으면 아무것도 반환하지 않는다.

    def _setitem(self, k, v): #버킷 리스트에 item을 저장하는 함수
        for item in self._bucket: # 버킷리스트안에 item이 있을때, 
            if (k == item.key): # k가 item의 키와같을경우
                item.value = v # 기존의 value를 새로운 값으로 바꾼다.
                return
        self._bucket.append(Entry(k,v)) #없으면 키와 value를 추가해준다.

    def _delitem(self, k): #item 삭제
        for j in range(len(self._bucket)): #bucket안에 있는 아이템들 중
            if (k == self._bucket[j].key): # 삭제할 키가 버킷안에 있으면
                self._bucket.pop(j) # pop 함수를 통해 그 키의 아이템을 드러내준다.
                return 1 #완료되었다는 뜻으로 1을 반환
        return None #없었으면 None 반환

    def __len__(self): #bucket의 길이 반환
        return len(self._bucket)

    def __iter__(self): # 아이템 키값 생산 하는 함수 
        for item in self._bucket:
            yield item.key #키 생성

# HashMap 클래스
class HashMap(Bucket): 
    def __init__(self, capacity = 11, prm=109345121): #초기값 설정 
        self._hash_tbl = capacity * [None] # 해시 테이블의 리스트들
        self._hash_tbl_size = capacity # 해시 테이블 사이즈
        self._num_entry = 0
        self._prime = prm
    
    def _hash_value(self, k): #해시값 
        return CyclicShiftHashCode(k) % self._prime % self._hash_tbl_size

    def __len__(self): #해시 테이블의 개수
        return self._num_entry

    def _getitem(self, k): #해시 테이블안에 bucket을 반환
        hv = self._hash_value(k) # hash table에서 인덱스 번호를 찾음
        bucket = self._hash_tbl[hv]
        return bucket._getitem(k) # Bucket 클래스의 getitem을 통해 반환

    def _setitem(self, k, v): # 해시 테이블안에 bucket을 집어넣음
        hv = self._hash_value(k) 
        if self._hash_tbl[hv] is None:
            self._hash_tbl[hv] = Bucket()
        bucket = self._hash_tbl[hv]
        bucket._setitem(k ,v) # Bucket 클래스를 이용
    
    def _delitem(self, k): # 해시테이블 안에 값을 지움
        hv = self._hash_value(k)
        bucket = self._hash_tbl[hv]
        bucket._delitem(k) # Bucket 클래스를 이용
        self._num_entry -= 1
    
    def __str__(self): # 문자열을 어떻게 출력할 것인가?
        s = ''
        for h in range(len(self._hash_tbl)):
            bucket = self._hash_tbl[h] # 해시테이블안에 있는 버킷
            if bucket is not None: #출력형식 지정
                s += "bucket[{:2d}] : ".format(h)
                for item in bucket:
                    s += str(item) + ", "
                s += "\n "
        return s