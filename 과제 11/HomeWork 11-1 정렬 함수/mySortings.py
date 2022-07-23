# 파일명 : mySortings.py
# 프로그램 목적 및 기능: 정렬 함수들을 담은 파일
# 프로그램 작성자 : 신대홍(2022년 5월 22일)

# 선택 정렬 (Selection Sort)
def SelectionSort(L): 
    L_SIZE = len(L) # 먼저 리스트의 크기를 알아낸다.

    for i in range(0, L_SIZE-1): # i = 0일때부터 L_SIZE - 1까지
        # L_SIZE - 1 를 하는 이유는 인덱스 번호는 L_SIZE-1까지이며, L_SIZE까지 하면 비교할 인덱스가 넘어서기 때문 
        index_MIN = i # 가장 작은 요소의 인덱스번호 초기화
        MIN_Eliment = L[i] # 가장작은 요소를 복사

        for j in range(i + 1, L_SIZE): # i + 1번째부터 끝까지 그 중에서 가장작은 요소를 찾고 갱신
            if (L[j] < MIN_Eliment): # 이미 저장되있던 최소값과 비교해서 더 작은게 발견되면 최소값 갱신
                index_MIN = j
                MIN_Eliment = L[j]
        
        if(index_MIN != i): #찾고 난후, 만약 그 작은게 자기자신이 아니라면
            L[index_MIN] = L[i] # SWAP해준다.
            L[i] = MIN_Eliment
#

# 병합 정렬 (Merge Sort)
def merge(L_left, L_right):  #병합 정렬 하기 위한 함수
    L_res = []
    i, j = 0, 0
    len_left, len_right = len(L_left), len(L_right) #왼, 오른쪽 리스트의 길이
    
    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]: 
            L_res.append(L_left[i]) #만약 왼쪽 리스트에 있는 것이 작다면 왼쪽리스트에 있는 걸 추가 
            i += 1 
        else:
            L_res.append(L_right[j]) #아니면 오른쪽
            j += 1 

    while (i < len_left): # 나머지 요소를 추가해준다. 
        L_res.append(L_left[i]) # 왼쪽요소 추가
        i += 1
    while (j < len_right): # 오른쪽 요소도 추가 해준다.
        L_res.append(L_right[j])
        j += 1
    return L_res #이제 반환
#
def mergeSort(L): #병합정렬 함수
    if len(L) < 2:
        return L[:] #2개 이하면 그냥 출력
    else:
        middle = len(L) // 2 #중간지점(나눌부분)찾음
        L_left = mergeSort(L[:middle]) #처음엔 가장 작은 부분(왼쪽 2개)부터 시작해서 점점 늘어감
        L_right = mergeSort(L[middle:]) 
    return merge(L_left, L_right) #정렬 시작
#

# 퀵정렬 (Quick Sort)
def Partition(L, L_left, L_right, P_I): # P_I의 좌측엔 P_I의 값보다 작은값, 우측엔 더 큰값으로 만드는 함수
    P_V = L[P_I] #먼저 P_I의 값을 L의 가장 우측으로 밀어버리고, 그 맨 우측의 값을 인덱스P_I의 위치에 옮긴다.
    L[P_I] = L[L_right]
    L[L_right] = P_V
    # SWAP 끝

    newPI = L_left # 새로운 P_I를 저장

    for i in range(L_left, L_right): # 범위 내에서
        if(L[i] <= P_V): # P_V = L[P_I]의 값보다 작다면
            temp = L[i] # 값 교환이 일어남. (작으면 왼쪽으로 이동함.)
            L[i] = L[newPI]
            L[newPI] = temp
            newPI += 1 # Swap이 일어난 후, newPI가 갱신된다. 
    
    P_V = L[L_right] #newPI를 모두 갱신된 후에는 맨 우측으로 옮겨놓았던 P_I의 값을 다시 제자리로 보냄
    L[L_right] = L[newPI]
    L[newPI] = P_V

    return newPI #모든 작업이 끝난후 반환한다.
#
def Quick_Sorting(L, L_left, L_right): #퀵정렬 본함수
    if (L_left >= L_right): #만약 Left와 Right가 같거나 Left가 더 커진다면
        return # 다시 돌아간다. 
    else:
        #P_I = Pivot_Index (기준 인덱스 번호, 주로 Left, Right의 중간) 
        P_I = (L_left + L_right) // 2 #인덱스번호는 정수이므로 //를 통해 내림연산을 해준다.

    New_P_I = Partition(L, L_left, L_right, P_I)

    if(L_left < (New_P_I - 1)):
        Quick_Sorting(L, L_left, New_P_I-1)
    if((New_P_I + 1) < L_right):
        Quick_Sorting(L, New_P_I+1, L_right)
#
def QuickSort(L): #퀵정렬 초기 시작함수
    L_SIZE = len(L)
    Quick_Sorting(L, 0, L_SIZE-1)