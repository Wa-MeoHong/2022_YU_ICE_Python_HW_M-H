
# 파일명 : Msg_Server.py
# 프로그램 목적 및 기능: 파이썬 스레드를 이용한 채팅 구현 (서버)
# 프로그램 작성자 : 신대홍(2022년 5월 28일)
# 최종 Update : Version 1.0.0, 2022년 5월 28일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/28     v1.0.0       최초작성

import socket, sys, threading # socket, sys, threading 모듈 설치
from threading import Thread # Thread 설치
import time # 쓰레드에서 Sleep함수가 필요함
import tkinter as tk # 윈도우 GUI 기능
from tkinter import ttk, scrolledtext, END #스크롤 기능 모듈

LocalHost = "127.0.0.1" # 자기와 자신 테스트 할 때, 쓰는 IP addr
SocketChat_PortNumber = 24000 #임의의 포트 넘버

class SocketChatting: # 소켓 채팅 클래스
    def __init__(self, mode): # 소켓 채팅 시스템 초기 설정
        
        global hostAddr # 전역 변수 hostAddr

        self.win = tk.Tk() # 윈도우 창 생성
        self.mode = mode
        self.win.title("Multi-Thread Based Socket Chatting (TCP Server)") # 창 제목
        hostname = socket.gethostname()
        hostAddr= socket.gethostbyname(hostname) #호스트 주소(우리집 ip)표시
        print("My (Server) IP address = {}". format(hostAddr))
        self.myAddr = hostAddr
        self.createWidgets()

        #스레드 만듦, TCPServer 스레드 
        serv_thread = Thread(target=self.TCPServer, daemon=True)
        serv_thread.start() #스레드 시작
   
    def TCPServer(self): # TCP 서버 연결 함수
        self.servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #연결형 TCP 소켓 하나 만듦
        self.servSock.bind((hostAddr, SocketChat_PortNumber))
        self.scr_servDisplay.insert(tk.INSERT,"TCP server is waiting for a client . . .\n")
        self.servSock.listen(1)
        self.conn, self.cliAddr = self.servSock.accept() # 요청이 오면 수락함# client address : (IP주소, port넘버)
        print("TCP Server is connected to client ({})\n".format(self.cliAddr))

        # 상대방이 연결되었다는 메세지를 출력한다. 
        self.scr_servDisplay.insert(tk.INSERT,"TCP server is connected to client\n" )
        self.scr_servDisplay.insert(tk.INSERT, "TCP client IP address : {}\n".format(self.cliAddr[0]))
        self.peerAddr_entry.insert(END, self.cliAddr[0])
        
        # 메세지를 출력을 해주는 것 (Client -> Server)
        while True:
            servRecvMsg = self.conn.recv(512).decode() # 받은 메세지를 문자로 decode한다
            if not servRecvMsg: # 만약에 받은 메세지가 없다면 출력하지 않는다.
                break
            self.scr_servDisplay.insert(tk.INSERT,">>" + servRecvMsg) # 받은 메세지 출력
        self.conn.close()
    
    def _quit(self): # 창 종료 함수
        self.win.quit()
        self.win.destroy()
        exit()

    def serv_send(self): # 메세지 전송 함수 (server -> client)
        msgToCli = str(self.scr_servInput.get(1.0, END))
        self.scr_servInput.delete(1.0, END) # 입력창 초기화
        self.scr_servDisplay.insert(tk.INSERT,"<<" + msgToCli)
        self.conn.send(bytes(msgToCli.encode())) # 메세지를 전송하기 위해 이진수로 변환하고 보낸다.
    
    def createWidgets(self): #윈도우 위젯 설정 함수
        frame = ttk.LabelFrame(self.win, text="Frame (Socket-based Text Message Chatting)")
        frame.grid(column=0, row=0, padx=8, pady=4) # 프레임박스 위치, 크기 설정
        
        # frame안에서 위젯을 넣음
        frame_addr_connect = ttk.LabelFrame(frame, text="") 
        frame_addr_connect.grid(column=0, row=0, padx=40, pady=20, columnspan=2)

        # frame_addr_connect안에 넣는 위젯
        myAddr_label = ttk.Label(frame_addr_connect, text="MyAddr(Server)")
        myAddr_label.grid(column=0, row=0, sticky='W') # 박스 위치 서쪽으로 조정
        peerAddr_label = ttk.Label(frame_addr_connect, text="PeerAddr(Client)")
        peerAddr_label.grid(column=1, row=0, sticky='W') #박스 위치 서쪽 조정

        # 메세지 박스 넣기 (frame_addr_connect 안에)
        # 나의 ip 텍스트박스
        self.myAddr = tk.StringVar()
        self.myAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable=self.myAddr)
        self.myAddr_entry.insert(END, hostAddr)
        self.myAddr_entry.grid(column=0, row=1, sticky='W')
        # 상대방 ip 텍스트 박스
        self.peerAddr = tk.StringVar()
        self.peerAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable="")
        self.peerAddr_entry.grid(column=1, row=1, sticky='W')

        #스크롤텍스트 박스 ( 텍스트 박스 표시, 입력)
        scrol_w, scrol_h = 40, 20
        serv_Display_label = ttk.Label(frame, text="Socket Server Display")
        serv_Display_label.grid(column=0, row=1)
        self.scr_servDisplay = scrolledtext.ScrolledText(frame, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scr_servDisplay.grid(column=0, row=3)

        self.scr_servInput = scrolledtext.ScrolledText(frame, width=40, height=3, wrap=tk.WORD)
        self.scr_servInput.grid(column=0, row=4, columnspan=3)

        # 버튼을 추가 ( 보내기 버튼)
        serv_send_button = ttk.Button(frame,text="Send Message to Client", command=self.serv_send)
        serv_send_button.grid(column=0, row=5, sticky='E')

        #입력 텍스트창에 커서를 넣는다.
        self.scr_servInput.focus()
#-------------------------------------------------------------------
print("Running TCP server")
sockChat = SocketChatting("server")
sockChat.win.mainloop()
