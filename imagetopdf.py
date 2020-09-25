import cv2
import numpy as np
from PIL import Image

import urllib.request
# open a connection to a URL using urllib

circles =np.zeros((4,2),np.int)
cunt = 0


def mouseclick(event,x,y,flags,params):
    global cunt
    if event==cv2.EVENT_LBUTTONDOWN:

        circles[cunt]=x,y
        cunt=cunt + 1
        print(circles)
frame=cv2.imread("resim3.png")
frame=cv2.resize(frame,(480,640))

while True:
    if cunt ==4:
        width,height=480,640
        pts1=np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix=cv2.getPerspectiveTransform(pts1,pts2)
        img_out=cv2.warpPerspective(frame,matrix,(width,height))
        img_out=cv2.cvtColor(img_out, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Output",img_out)
        cv2.imwrite("img_out.jpg",img_out)
        ImgFile = Image.open ("img_out.jpg")

        if ImgFile.mode == "RGBA":

            ImgFile = ImgFile.convert ("RGB")

        ImgFile.save ("test2.pdf", "PDF")


    for x in range(0,4):
        cv2.circle(frame,(circles[x][0],circles[x][1]),3,(0,255,0),cv2.FILLED)




    cv2.imshow("Frame",frame)
    cv2.setMouseCallback("Frame",mouseclick)

    if cv2.waitKey (1) & 0xFF == ord ('q'):
        import webbrowser

        url = 'file:///C:/Users/iamem/PycharmProjects/imageclicktopdf/test2.pdf'
        webbrowser.register ('chrome',
                             None,
                             webbrowser.BackgroundBrowser (
                                 "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get ('chrome').open (url)
        break





















