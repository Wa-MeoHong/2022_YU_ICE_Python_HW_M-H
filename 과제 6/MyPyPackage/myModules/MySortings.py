
def  selectionSort(L): #선택 정렬 
    for round in range(0, len(L)):
        index_MIN = round #최소값 인덱스번호 초기화 
        min_num = L[round] #최소값 초기화
        for i in range(round, len(L)): #round 부터 끝까지
            if(L[i] < min_num):
            #만약 서치하면서 더 적은 수를 찾았다면
                index_MIN = i # 인덱스번호 최신화, 최소값 최신화한다.
                min_num = L[i] 
        if(index_MIN != round):
        #가장 작은 최소값을 찾은 후엔 값을 처음 비교한 값과 교체
            L[index_MIN] = L[round]
            L[round] = min_num

def mergeSort(L): #병합정렬 함수
    if len(L) < 2:
        return L[:] #2개 이하면 그냥 출력
    else:
        middle = len(L) // 2 #중간지점(나눌부분)찾음
        L_left = mergeSort(L[:middle]) #처음엔 가장 작은 부분(왼쪽 2개)부터 시작해서 점점 늘어감
        L_right = mergeSort(L[middle:]) 
    return merge(L_left, L_right) #정렬 시작
#

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

    while (i < len_left): #왼쪽 정렬된 
        L_res.append(L_left[i])
        i += 1
    while (j < len_right):
        L_res.append(L_right[j])
        j += 1
    return L_res
#

