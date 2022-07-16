# 파일명 : Find Min Max Average grade
#프로그램 목적 및 기능: 10명의 성적을 입력받고, 최대값, 최솟값, 평균을 출력하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 3월 5일)
# 최종 Update : Version 1.0.0, 2022년 3월 5일(신대홍)

N = 10
student_list = []  #배열 지정
for i in range(10):
    s = int(input("성적을 입력하세요 : ")) #성적 입력
    student_list.append(s)
MAX = max(student_list) #최댓값 찾기
MIN = min(student_list) #최소값 찾기
avg = sum(student_list)/N #평균 찾기
print("성적 : "+str(student_list)) #출력
print("최대값 :"+str(MAX)+" 최솟값 :"+str(MIN)+" 평균 :"+str(avg))