# 파일명 : Print time using Tuple
# 프로그램 목적 및 기능: 시, 분 초를 받는 튜플을 작성하고, 그 튜플을 묶은 리스트를
#           출력하고, 정렬한 후 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 3월 26일)
# 최종 Update : Version 1.0.0, 2022년 3월 26일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/26     v1.0.0       최초작성

# 이름 리스트
L_name = ['KIM C.S.', 'BAEK D.S.', 'Yoon J.Y', 'PARK K.R', 'CHOI J.W', \
        'MOON T.E', 'JOO Y.H', 'YOO J.H', 'SHIN A J', 'JANG U A']

# 학번 리스트
L_st_ID = ['12341234', '11121132', '14021032', '12204923', '13122191', \
        '20200321', '18192345', '19121301', '18589102', '17821234']

# 전공 리스트
L_major = ['CE', 'EE', 'CE', 'ICE', 'ME', 'ICE', 'EE', 'EE', 'ME', 'CE']

# 학점 리스트
L_GPA = ['4.12', '4.02', '3.76', '3.98', '4.36', '3.11', '2.54', '3.23',\
        '4.01', '3.09']

# 한 요소씩 튜플로 묶어서 리스트로 만듦
L_Student = list(zip(L_name, L_st_ID, L_major, L_GPA)) 

for i in range(len(L_Student)):
    (name, st_id, major, GPA) = L_Student[i]
    print("students[{0:2}] : name({1:8s}), st_id({2:8d}), major({3:3s}, GPA({4:5.2f}))"\
        .format(i+1, name, int(st_id), major, float(GPA)))  # 출력

SORT_L_Student = sorted(L_Student)                          # 이름 오름차순 정렬 후 출력
print("\nAfter sorting in Increasing order : ")
for i in range(len(L_Student)):
    (name, st_id, major, GPA) = SORT_L_Student[i]
    print("students[{:2}] : name({:^8s}), st_id({:8d}), major({:3s}), GPA({:5.2f}))"\
.format(i+1, name, int(st_id), major, float(GPA)))

Dsort_L_Student = sorted(L_Student, key = lambda x : x[3], reverse = True) 
# 학번 내림차순 정렬 후 출력
# key lambda 역할 : 정렬하고 싶은 기준 설정시 사용. x = 튜플 ,x[3] : 튜플의 요소중 GPA 
print("\nAfter sorting in decreasing order : ")
for i in range(len(L_Student)):
    (name, st_id, major, GPA) = Dsort_L_Student[i]
    print("students[{:2}] : name({:^8s}), st_id({:8d}), major({:3s}, GPA({:5.2f}))"\
.format(i+1, name, int(st_id), major, float(GPA)))
