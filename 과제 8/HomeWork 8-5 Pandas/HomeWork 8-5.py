# 파일명 : HomeWork 8-5.py
# 프로그램 목적 및 기능: 엑셀 파일로부터 데이터를 읽어와 학생 평균, 과목평균을 구하고
#           데이터에 추가하여 새로 엑셀파일을 작성하는 프로그램
# 프로그램 작성자 : 신대홍(2022년 5월 1일)
# 최종 Update : Version 1.0.0, 2022년 5월 1일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/01     v1.0.0       최초작성

import pandas as pd #판다스 모듈 호출

df = pd.read_excel("student_scores.xlsx")
#엑셀에서 데이터를 읽어와 df에 저장, 0번째 열 = st_id를 인덱스번호로 맞춤
print("df = ") # 읽어온 초기 데이터를 먼저 출력
print(df,"\n")

avgs_Student = df.loc[:, ['Eng', 'Kor', 'Math', 'Sci']].mean(1)
#df.loc을 통해 계산하고 싶은 열의 데이터들을 가져왔음
#행의 평균(학생의 성적 평균), mean(axis(행,열 구분))
df['Avg'] = avgs_Student #학생 평균 성적 행을 추가

avgs_Class = df.loc[:, ['Eng', 'Kor', 'Math', 'Sci', 'Avg']].mean()
#df.loc을 통해 계산하고 싶은 열의 데이터들을 가져왔음
#열의 평균 (과목당 평균, 학생평균성적의 평균)

print("avg_per_class = ") # 과목 평균 출력
print(avgs_Class,"\n")

df.sort_values('Avg', ascending=False, inplace=True) 
#학생 평균성적을 기준으로 내림차순 정렬 후, 저장(inplace)
df.loc[len(df)] = avgs_Class #과목 평균, 평균 성적의 평균을 추가
df.at[len(df)-1, 'st_name'] = 'Total_Avg' #과목 평균 열의 이름을 추가
print("df_sorted_with_Avg = ") # 통계가 끝난 데이터 출력
print(df,"\n") #출력

print("Writing df to excel File") #엑셀 파일로 작성
with pd.ExcelFile("processed_scores.xlsx") as excel_writer:
    df.to_excel(excel_writer) #작성