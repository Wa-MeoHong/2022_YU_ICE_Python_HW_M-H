
# 파일명 : Video_Server.py
# 프로그램 목적 및 기능: 파이썬 스레드를 이용한 화상통화 구현 (서버)
# 프로그램 작성자 : 신대홍(2022년 5월 28일)
# 최종 Update : Version 1.0.0, 2022년 5월 28일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/28     v1.0.0       최초작성

import socket   # 소켓 라이브러리 호출
import cv2  # Opencv 라이브러리 호춣
import numpy  # NumPy 라이브러리 호출 (영상, 이미지는 데이터가 행렬의 형식을 띈다.)
from queue import Queue  # 큐 라이브러리 모듈 호출
from _thread import *  # 쓰레드 관련 함수 호출

SERVER_WEBCAM = 0  # 전역 변수 호출

# 영상 전송하는데 있어서 버퍼가 필요하기 때문에 버퍼에 관한 함수를 넣는다.
def recvall(sock, count):
    buf = b''
    while count: # count가 있을 때,
        newbuf = sock.recv(count) # 새로운 버퍼가 들어온다.
        if not newbuf: # 만약 새로운 버퍼(영상)이 없다면 그대로 None을 반호나
            return None
        buf += newbuf # 버퍼를 추가한다.
        count -= len(newbuf) # 새로운 버퍼를 count에서 뺀다.
    return buf # 버퍼 반환

def SendtoCli(Clisock, addr, queue): # 영상을 클라이언트에 보낸다.
    print('Server:: connected to ({} : {})'.format(addr[0],addr[1]))
    while True:
        try: # 평시엔 이런 코드를 사용한다. (Try)
            if not queue.empty(): # 만약 큐에 데이터가 없다면 
                stringData = queue.get() # 데이터를 얻어서
                Clisock.send(str(len(stringData)).ljust(16).encode()) # 클라이언트에 보낸다.
                Clisock.send(stringData)
        except ConnectionResetError as e: # 만약 예외사항(연결 리셋 에러)가 발생하면 끝낸다.
            break
    Clisock.close()

def VideoChat_Serv(queue): # 비디오챗을 하면서 영상을 이미지 바이트 형식으로 저장하는 함수
    server_webcam = cv2.VideoCapture(SERVER_WEBCAM)
    while True:
        ret, serv_frame = server_webcam.read() # 영상을 읽어옴
        if ret == False: # 만약 웹캠에서 읽어온 데이터가 없다면 
            continue # 반복문을 첨부터 다시 반복
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90] # 인코딩된 영상은 JPEG의 형태로 가공된다.
        result, imgencode = cv2.imencode('.jpg', serv_frame, encode_param)
        img_data = numpy.array(imgencode) # 이미지로 인코딩된 영상 자료를 배열(numpy)의 형식으로 만들어 저장한다.
        stringData = img_data.tobytes() # 배열의 형태로 저장된 이미지 데이터를 byte 형태로 변환한다.
        queue.put(stringData) # 이걸 큐(버퍼들)에 집어넣는다.
        key = cv2.waitKey(1)
        if key == 27: # ESC를 누르면 나가기
            break

# 메인함수     
if __name__ == "__main__":  # 클라이언트와 연결하고 대화
    enclosure_queue = Queue()
    serverAddr = '127.0.0.1'  # 자기 주소
    PORT = 9999  # 임의의 포트
    hostname = socket.gethostname()  # 호스트 이름, 서버 주소 얻음
    serverAddr = socket.gethostbyname(hostname)
    print("Server IP address = {}".format(serverAddr)) # 서버 주소 출력
    
    servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    servsock.bind((serverAddr, PORT))  # 묶어줌
    servsock.listen()
    print('Server:: Video chatting Server started')
    print('Server:: Waiting for Client...')
    Clisock, addr = servsock.accept() # 만약 클라이언트에서 연결 요청을 하면 받아준다.
    print('Server:: connected to ({} : {})'.format(Clisock, addr,)) # 연결 완료
    start_new_thread(VideoChat_Serv, (enclosure_queue,)) # 쓰레드 생성(비디오챗 함수)
    start_new_thread(SendtoCli, (Clisock, addr, enclosure_queue,)) # 새로운 쓰레드 생성(클라이언트로 영상 송출)
    while True:
        length = recvall(Clisock, 16) # 처음 영상을 가져올 땐 16바이트의 버퍼를 가져옴
        stringData = recvall(Clisock, int(length)) # 그 후, 다시한번더 새로운 데이터를 받아옴
        data = numpy.frombuffer(stringData, dtype='uint8')
        decimg = cv2.imdecode(data, 1) # 이제 클라이언트로부터 받은 영상 데이터를 디코딩
        cv2.imshow('Server:: Received from Client', decimg) # 출력
        key = cv2.waitKey(1)
        if key == 27: # 만약 ESC 눌렀다면 종료
            break
    servsock.close() #닫기