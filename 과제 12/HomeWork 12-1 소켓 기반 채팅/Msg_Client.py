
# 파일명 : Msg_Client.py
# 프로그램 목적 및 기능: 파이썬 스레드를 이용한 채팅 구현 (클라이언트)
# 프로그램 작성자 : 신대홍(2022년 5월 28일)
# 최종 Update : Version 1.0.0, 2022년 5월 28일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/28     v1.0.0       최초작성

import socket, sys, threading # socket, sys, threading 모듈 설치
from threading import * # Thread 설치
import time # 쓰레드에서 Sleep함수가 필요함
import tkinter as tk # 윈도우 GUI 기능
from tkinter import ttk, scrolledtext, END #스크롤 기능 모듈

LocalHost = "127.0.0.1" # 자기와 자신 테스트 할 때, 쓰는 IP addr
SocketChat_PortNumber = 24000 #임의의 포트 넘버

class SocketChatting: # 소켓 채팅 클래스
    def __init__(self, mode): # 소켓 채팅 시스템 초기 설정
        
        global hostAddr # 전역 변수 hostAddr
        self.win = tk.Tk()
        self.mode = mode #Server 아님 Client

        self.win.title("Multi-Thread Based Socket Chatting (TCP Client)") # 창 제목
        hostname = socket.gethostname()
        hostAddr = socket.gethostbyname(hostname) #호스트 주소(우리집 ip)표시
        print("My (Client) IP address = {}". format(hostAddr))
        self.myAddr = hostAddr
        self.createWidgets()

        serv_thread = Thread(target=self.TCPClient, daemon=True)
        serv_thread.start() #스레드 시작
    
    def TCPClient(self): # TCP 클라언트에 연결할 서버를 입력
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servAddr_str = input("Server IP Addr (e.g. '127.0.0.1') = ")
        self.cliSock.connect((servAddr_str, SocketChat_PortNumber))
        servAddr = self.cliSock.getpeername()
        print("TCP Client is connected to Server ({})\n".format(servAddr))
        self.scr_cliDisplay.insert(tk.INSERT, "TCP client is connected to server \n")
        self.scr_cliDisplay.insert(tk.INSERT, "TCP server IP address : {}\n".format(servAddr[0]))
        self.servAddr_entry.insert(END, servAddr[0])

        while True: # 메세지를 받아와서 디코딩 후 출력
            ClirecvMsg = self.cliSock.recv(8192).decode()
            if not ClirecvMsg: # 메세지가 없다면 출력 X
                break
            self.scr_cliDisplay.insert(tk.INSERT, ">>" + ClirecvMsg)
        self.cliSock.close()

    def _quit(self): # 종료할때의 함수
        self.win.quit() # 창 끄고
        self.win.destroy() # 없애고
        exit() # 나가기

    def connect_server(self): # TCP 서버에 연결을 요청함
        self.scr_cliDisplay.insert(tk.INSERT, "Connecting to server ....")
        self.mylpAddr = self.myAddr.get()
        self.peerIpAddr = self.servAddr.get()
        self.scr_cliDisplay.insert(tk.INSERT, "My IP Address : " + self.mylpAddr + '\n')
        self.scr_cliDisplay.insert(tk.INSERT, "Server's IP Address : " + self.peerlpAddr + '\n')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.peerIpAddr, SocketChat_PortNumber)
        
    def Cli_send(self): # 서버로 메세지를 보내는 함수
        msgToServ = str(self.scr_cliInput.get(1.0, END))
        self.scr_cliInput.delete(1.0, END) # 입력창 초기화
        self.scr_cliDisplay.insert(tk.INSERT,"<<" + msgToServ)
        self.cliSock.send(bytes(msgToServ.encode())) # 메세지를 전송하기 위해 이진수로 변환하고 보낸다.

    def createWidgets(self):
        frame = ttk.LabelFrame(self.win, text="Frame (Socket-based Text Message Chatting)")
        frame.grid(column=0, row=0, padx=8, pady=4) # 프레임박스 위치, 크기 설정
        
        # frame안에서 위젯을 넣음
        frame_addr_connect = ttk.LabelFrame(frame, text="") 
        frame_addr_connect.grid(column=0, row=0, padx=40, pady=20, columnspan=2)

        # frame_addr_connect안에 넣는 위젯
        myAddr_label = ttk.Label(frame_addr_connect, text="MyAddr(Client)")
        myAddr_label.grid(column=0, row=0, sticky='W') # 박스 위치 서쪽으로 조정
        peerAddr_label = ttk.Label(frame_addr_connect, text="Server Addr")
        peerAddr_label.grid(column=1, row=0, sticky='W') #박스 위치 서쪽 조정

        # 메세지 박스 넣기 (frame_addr_connect 안에)
        # 나의 ip 텍스트박스
        self.myAddr = tk.StringVar()
        self.myAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable=self.myAddr)
        self.myAddr_entry.insert(END, hostAddr)
        self.myAddr_entry.grid(column=0, row=1, sticky='W')

        # 상대방 ip 텍스트 박스
        self.servAddr = tk.StringVar()
        self.servAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable="")
        self.servAddr_entry.grid(column=1, row=1, sticky='W')

        # 서버 연결 버튼 
        connect_button = ttk.Button(frame_addr_connect, text="Connect", command=self.connect_server)
        connect_button.grid(column=3, row=1)
        connect_button.configure(state='disabled')

        #클라이언트 메세지 출력칸
        cliDisplay_label = ttk.Label(frame, text="Socket Client Display")
        cliDisplay_label.grid(column=0, row=1)
        scrol_w, scrol_h = 40, 20
        self.scr_cliDisplay = scrolledtext.ScrolledText(frame, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scr_cliDisplay.grid(column=0, row=2, columnspan=3, sticky='WE')

        cliInput_label = ttk.Label(frame, text="Input Text Message(Client):")
        cliInput_label.grid(column=0, row=3)

        # 메세지 입력칸
        self.scr_cliInput = scrolledtext.ScrolledText(frame, width=40, height=3, wrap=tk.WORD)
        self.scr_cliInput.grid(column=0, row=4, columnspan=3)

        #버튼 추가
        cli_send_button = ttk.Button(frame, text="Send Message to Server", command=self.Cli_send)
        cli_send_button.grid(column=0, row=5, sticky='E')

        #메세지 입력 부분 커서 추가
        self.scr_cliInput.focus()

print("Running TCP Client")
sockChat = SocketChatting('client')
sockChat.win.mainloop()