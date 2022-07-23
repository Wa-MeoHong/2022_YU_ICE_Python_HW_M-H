# 파일명 : GUI for recognition.py
# 프로그램 목적 및 기능: 파이썬 필기체 인식 프로그램
# 프로그램 작성자 : 신대홍(2022년 6월 5일)
# 최종 Update : Version 1.0.0, 2022년 6월 5일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/06/05     v1.0.0       최초작성

import os
import PIL
import cv2
import glob
import numpy as np
from tkinter import *
from PIL import Image, ImageDraw, ImageGrab
# 모델 로드
from keras.models import load_model
model = load_model("CNN_Model_Digits")
model.summary()
print("Model is loaded successfully ...")

# 먼저 메인 윈도우창 생성
root = Tk()
root.resizable(0, 0)
root.title("Handwritten Digits Recognition GUI App")

# 변수 정의
lastx, lasty = None, None
image_number = 0

# 숫자를 그릴 캔버스 화면을 먼저 설정
cv = Canvas(root, width=640, height=480, bg='white')
cv.grid(row=0, column=0, pady=2, sticky=W, columnspan=2)

def draw_lines(event): # 선 그리기 함수
    global lastx, lasty
    x, y = event.x, event.y
    cv.create_line((lastx, lasty, x, y), width=8, fill='black',
        capstyle=ROUND, smooth=TRUE, splinesteps=12)
    lastx, lasty = x, y

def clear_widget(): # 위젯 클리어 함수
    global cv
    cv.delete("all")

def activate_event(event): # 이벤트 활성화 함수
    global lastx, lasty
    cv.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y

def recognize_digit(): # 숫자 인식 함수 
    global image_number
    predictions = []
    percentage = []
    #image_number = 0
    filename = f'image_{image_number}.png'
    widget = cv
    #get the widget coordinates
    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    # 이미지를 crop함
    ImageGrab.grab().crop((x, y, x1, y1)).save(filename)

    # 색깔 포멧으로 이미지를 읽어옴
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    # 회색조로 이미지 전환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 쓰레드홀딩 (Bobuyuki Otsu’s method: greyscale to monochrome)
    ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # findContour() function helps in extracting the contours from the image
    contours = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in contours:
        # get bounding box and extract ROI
        x, y, w, h = cv2.boundingRect(cnt)
        # create rectange
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 1)
        top = int(0.05 * th.shape[0])
        bottom = top
        left = int(0.05 * th.shape[1])
        right = left
        th_up = cv2.copyMakeBorder(th, top, bottom, left, right,
            cv2.BORDER_REPLICATE)
        # extract the image ROI
        roi = th[y-top:y+h+bottom, x-left:x+w+right]
        # resize roi image to 28x28 pixels
        img = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
        # reshaping the image to support our model input
        img = img.reshape(1, 28, 28, 1)
        # normalizing the image
        img = img / 255.0
        pred = model.predict([img])[0]
        final_pred = np.argmax(pred)
        data = str(final_pred) + ' ' + str(int(max(pred)*100)) + '%'
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (255, 0, 0)
        thickness = 1
        cv2.putText(image, data, (x, y-5), font, fontScale, color, thickness)

    cv2.imshow("image", image)
    cv2.waitKey(0)

# Tkinter
cv.bind('<Button-1>', activate_event)
# Add buttons and labels
btn_save = Button(text="Recognize Digits", command = recognize_digit)
btn_save.grid(row=2, column=0, padx=1, pady=1)
btn_clear = Button(text="Clear widget", command = clear_widget)
btn_clear.grid(row=2, column=1, padx=1, pady=1)
# mainloop()
root.mainloop()