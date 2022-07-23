"""
이름: 길민성
날짜: 2021.05.28
프로그램: 양방향 화상 채팅 프로그램(Server)
"""
import socket
import cv2
import numpy
from queue import Queue
from _thread import *
SERVER_WEBCAM = 0

def recvall(sock, count):
     buf = b'' #byts로 정의
     while count:
          newbuf = sock.recv(count)
          if not newbuf: 
              return None
          buf += newbuf
          count -= len(newbuf)
     return buf

def video_sendto_client(client_socket, addr, queue):
     print('Server::connected to ({} : {})'.format(addr[0], addr[1]))
     while True:
          try:
               if not queue.empty():
                    stringData = queue.get()
                    client_socket.send(str(len(stringData)).ljust(16).encode()) #길이의 정보를 먼저 보낸 후
                    client_socket.send(stringData) #문자열을 전송
          except ConnectionResetError as e:
               break
     client_socket.close()

def video_chat_server(queue):
     server_webcam = cv2.VideoCapture(SERVER_WEBCAM)
     while True:
          ret, serv_frame = server_webcam.read() #이미지 읽어옴
          if ret == False:
               continue
          encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
          result, imgencode = cv2.imencode('.jpg', serv_frame, encode_param)    
          img_data = numpy.array(imgencode) #이미지 코드를 넘파이로 저장
          stringData = img_data.tostring()
          queue.put(stringData) #que에 담기
          key = cv2.waitKey(1)
          if key == 27: #ESC키를 누르면 중단
               break
def video_recvfrom_client (client_socket): #서버에 클라이언트로
     while True:
          length = recvall(client_socket, 16) #이미지 길이정보, 16byte, length에 저장
          stringData = recvall(client_socket, int(length)) #영상정보를 StringData에 저장
          data = numpy.frombuffer(stringData, dtype='uint8') #유니코드-8fh wjwkd
          decimg=cv2.imdecode(data,1)
          cv2.imshow('Server:: Received from Client',decimg) #상대방 영상 출력
          key = cv2.waitKey(1)
          if key == 27: #ESC키를 누르면 중단
               break

if __name__ == "__main__":
    enclosure_queue = Queue() #Que생성
    serverAddr = '192.168.219.107' 
    PORT = 9999
    hostname = socket.gethostname()
    serverAddr = socket.gethostbyname(hostname)
    print("Server IP address = {}".format(serverAddr))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((serverAddr, PORT))
    server_socket.listen() #대기
    print('Server::Video chatting server started')
    start_new_thread(video_chat_server, (enclosure_queue,))
    print('Server::Waitint for client …. ')
    client_socket, addr = server_socket.accept() 
    print('Server::connected to ({} : {})'.format(client_socket, addr))
    start_new_thread(video_sendto_client, (client_socket, addr, enclosure_queue,))
    while True:
        length = recvall(client_socket, 16) #이미지 길이정보, 16byte, length에 저장
        stringData = recvall(client_socket, int(length)) #영상정보를 StringData에 저장
        data = numpy.frombuffer(stringData, dtype='uint8') #유니코드-8fh wjwkd
        decimg=cv2.imdecode(data,1)
        cv2.imshow('Server:: Received from Client',decimg) #상대방 영상 출력
        key = cv2.waitKey(1)
        if key == 27: #ESC키를 누르면 중단
            break
    server_socket.close()
