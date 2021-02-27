import cv2
import pytesseract as ts
import os
ts.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#psm → Page segmentation mode 6 i.e. detects a block of text
#oem → Engine mode 2 i.e. uses both tesseract and cube
conf="--psm 6 --oem 2" 
Visual=1 #Determines whether it outputs only the text or the text marked on the image
file="f01.png"
img=cv2.imread(file)

def Words(inImage,outImage):
        '''For visualisation of the image with red boxes and red text'''
        
        imgHeight,imgWidth=inImage.shape[:2]
        Boxes=ts.image_to_data(inImage,config=conf)
        
        for i in Boxes.splitlines()[1:]:
                s=i.split()
                if len(s)==12 and int(s[10])>0:
                        txtX,txtY,txtW,txtH=map(int,s[6:10])
                        cv2.rectangle(outImage,(txtX,txtY),(txtX+txtW,txtY+txtH),(0,0,255),1) #Creating rect around every word
                        cv2.putText(outImage,s[11],(txtX,txtY-2),cv2.FONT_HERSHEY_COMPLEX,0.5,color=(0,0,255)) #Displaying every word
                        
        return outImage

if Visual:
        outputimg=img
        
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converts image colour from BGR to grayscale
img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,7) #Changes contrast of the image
##img=cv2.resize(img,None,fx=1,fy=1)
os.system(file)

print(ts.image_to_string(img,config=conf)) #Reads text from img and prints it

if Visual:
        cv2.imshow("ting",Words(img,outputimg))
        cv2.waitKey(0)

