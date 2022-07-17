# 파일명 : Print ASCIIcode List
# 프로그램 목적 및 기능: ASCII코드에서 영문 대,소문자, 숫자를 리스트로 구성후 출력
# 프로그램 작성자 : 신대홍(2022년 3월 26일)
# 최종 Update : Version 1.0.0, 2022년 3월 26일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/03/26     v1.0.0       최초작성

Upper = list(map(chr, range(65, 91)))           # 영문 대문자 리스트, (‘A’ = 65, ‘Z’ = 90), range(A, B) =A ~ B-1까지
Lower = list(map(chr, range(97, 123)))          # 영문 소문자 리스트, (‘a’ = 97, ‘z’ = 122)
Digit = list(map(chr, range(48, 57)))           # 숫자 리스트 ( ‘0’ = 48, ‘9’ = 56 )
print("Upper case alphabet =\n {}" .format(Upper))  # 출력
print("\nLower case alphabet =\n {}" .format(Lower))
print("\nDigits =\n {}" .format(Digit))