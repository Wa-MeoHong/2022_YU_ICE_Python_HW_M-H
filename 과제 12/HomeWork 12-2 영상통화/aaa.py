"""
이름: 길민성
날짜: 2021.05.28
프로그램: 양방향 화상 채팅 프로그램(Client)
"""
import socket #socket 모듈 설치
import cv2 #cv2 모듈 설치
import numpy #numpy 모듈 설치
from queue import Queue #que  설치
from _thread import * #thread의 모든 것

CLIENT_WEBCAM = 1 #2개의 카메라를 사용할때에는  0 or 1

def recvall(sock, count):
     buf = b'' #byts로 정의
     while count:
          newbuf = sock.recv(count)
          if not newbuf:
               return None
          buf += newbuf
          count -= len(newbuf)
     return buf
def video_sendto_server(client_socket, queue):
     while True:
          try:
               if not queue.empty ():
                    stringData = queue.get()
                    client_socket.send(str(len(stringData)).ljust(16).encode()) #길이의 정보를 먼저 보낸 후
                    client_socket.send(stringData) #문자열을 전송
          except ConnectionResetError as e:
               break
     client_socket.close()

def video_chat_client(queue):
     client_webcam = cv2.VideoCapture(CLIENT_WEBCAM)
     while True:
          ret, frame = client_webcam.read() #이미지 읽어옴
          if ret == False:
               continue
          encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
          result, imgencode = cv2.imencode('.jpg', frame, encode_param)
          img_data = numpy.array(imgencode) #이미지 코드를 넘파이로 저장
          stringData = img_data.tostring()
          queue.put(stringData) #que에 담기
          key = cv2.waitKey(1)
          if key == 27: #ESC키를 누르면 중단
               break

if __name__ == "__main__":
     serverAddr = '192.168.219.107'
     PORT = 9999
     enclosure_queue = Queue()
     serverAddr = input("Input server IP address = ")
     print('Client::Connecting to Server')
     client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #소켓 연
     client_socket.connect((serverAddr, PORT)) #컴퓨터간 연결
     print('Client::Connected to Server({}:{})'.format(serverAddr, PORT)) #연결 완료되면 상태 출력
     start_new_thread(video_chat_client, (enclosure_queue,))
     start_new_thread(video_sendto_server, (client_socket, enclosure_queue,))
     while True:
          length = recvall (client_socket, 16) #16byte 길이 정보 읽기
          stringData = recvall(client_socket, int(length)) #길이정보 int 변환 후 전송
          data = numpy.frombuffer(stringData, dtype='uint8') #유니코드-8의 모맷으로 준비
          decimg=cv2.imdecode(data,1)
          cv2.imshow('Client:: Received from Server',decimg) #이미지 화면에 보이기
          key = cv2.waitKey(1)
          if key == 27: #ESC키를 눌르면 중단
               break
     client_socket.close()
