# KLASIFIKASI WARNA DARI SUATU GAMBAR MENGGUNAKAN ALGORITMA MECHINE
# LEARNING Convolutional Neural Network (CNN).

# Nama : Irvan Falasifa
# NIM  : 1197050056
# IF C

# Library yang digunakan
import cv2
import numpy as np
import pandas as pd
import argparse

# Import gambar dari local computer file dengan library argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
# Membaca gambar dengan OpenCv
img = cv2.imread(img_path)

clicked = False
r = g = b = xpos = ypos = 0

# Membaca CSV file dengan dengan Library Panda dan Memberi simbol pada setiap kolom
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# Funsi untuk menentukan jarak minimum setiap warna dan mencocokkan dengan warna yang terdekat dengan kode warna yang dipilih
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

# Fungsi untuk mengatur nilai koordinat x y dari double klik mouse
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(1):

    cv2.imshow("image",img)
    if (clicked):
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)      
        clicked=False

    # Tekan esc untuk keluar (looping)   
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
