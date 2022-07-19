# 파일명 : Homework5_1.py
# 프로그램 목적 및 기능: 학생 10명의 리스트를 받아 성적의 최대, 최소, 평균 계산
# 프로그램 작성자 : 신대홍(2022년 4월 2일)
# 최종 Update : Version 1.0.0, 2022년 4월 2일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/04/02     v1.0.0       최초작성

def statistics_student_GPA(L_GPA): # GPA의 계산 함수 
    num_ST = len(L_GPA) # 리스트 개수 측정
    stud_MAX = max(L_GPA) # Max 측정
    stud_MIN = min(L_GPA) # Min 측정
    stud_sum = sum(L_GPA) # Sum 계산
    stud_AVG = stud_sum / num_ST # 평균 계산
    return num_ST, stud_MIN, stud_MAX, stud_AVG #값 반환
#

L_name = ['KIM', 'BAEK', 'Yoon', 'PARK', 'CHOI', \
        'MOON', 'JOO', 'YOO', 'SHIN', 'JANG'] #이름 리스트

L_major = ['CE', 'EE', 'CE', 'ICE', 'ME',\
     'ICE', 'EE', 'EE', 'ME', 'CE'] #전공 리스트

L_birth = [] #생일 리스트 

L_st_ID = [12341, 11221, 14021, 12204, 13122, \
        20200, 18192, 19121, 18589, 17821] #학번 리스트

L_GPA = [4.1, 4.0, 3.7, 3.9, 4.3,\
     3.1, 2.5, 3.2, 4.0, 3.0] #학점 리스트

L_B_Y = [2000,2001,2002,1999,1997,\
    1999,2000,2002, 2001,1999] #생년 리스트
L_B_M = [2, 4, 5, 9, 1, 11, 9, 12, 3, 3] #생월 리스트
L_B_D = [15, 9, 21, 13, 8, 16, 28, 12, 3, 3] #생일 리스트

L_birth = list(zip(L_B_Y, L_B_M, L_B_D)) #학생들 생일 리스트를 받아 튜플로 묶기
L_Student = list(zip(L_name, L_major, L_st_ID, L_birth, L_GPA)) # 학생 정보 튜플로 묶기

print("students = ")
for i in range(len(L_Student)):
    print(L_Student[i]) # 튜플들 출력
ST_num, ST_Min, ST_Max, ST_Avg = statistics_student_GPA(L_GPA) #계산함수로 계산후 값받아옴

print("statistics_student_GPA :: ") #출력
print(" - L_GPAs =", L_GPA)
print(" - num_students =", ST_num)
print(" - Statistics of GPAs : Max ({0:.1f}), Min ({1:.1f}), Avg ({2:f})"\
     .format(ST_Max, ST_Min, ST_Avg))
