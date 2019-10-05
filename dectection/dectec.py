from imageai.Detection import VideoObjectDetection
from imageai.Detection import ObjectDetection
import numpy as np
import pyzbar.pyzbar as pyzbar
import cv2
import os
import datetime
import time
import glob
import sys
from basic import Ui_Form
from PyQt5.QtGui import QPixmap,QImage,QIcon
from PyQt5.QtCore import Qt, QThread, QTimer,QSize
from PyQt5.QtWidgets import *
class StartWindows(QMainWindow):
    def __init__(self,camera=None, parent=None):
        super(StartWindows, self).__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.detections = None
        self.frame = None
        self.files=[]
        self.tmp=[]
        self.start=0
    
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update)
        
       
         #User
        self.Qr_User=""
        self.Point=0

        #button
        self.ui.pushButton_2.clicked.connect(self.yolo_tiny)
        self.ui.pushButton.clicked.connect(self.stop)
        #camera
        self.camera = cv2.VideoCapture(0)
        self.update_timer.start(30)
        #qr
        self.qr=cv2.QRCodeDetector()
        
        
        '''
    def update2(self):
        self.update_timer2.start(30)
        ret,self.frame =self.camera.read()
        self.frame=cv2.flip(self.frame,1)
        cv2.imshow("img", img)  
        '''    
        
    def yolo_tiny(self):
     
        self.start=1
        
        self.execution_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath( os.path.join(self.execution_path , "yolo-tiny.h5"))
        self.detector.loadModel(detection_speed="fast")
        print("###you are use yolo_tiny model###")
        
    def update(self):
        
        if(self.start ==0):
            
            ret,self.frame =self.camera.read()
            
            decodedObjects = pyzbar.decode(self.frame)
            
            
            for obj in decodedObjects:
                if obj.data:
                    
                    print("Data", (obj.data))
                    self.Qr_User=str(obj.data)
                   
                
            print(self.Qr_User)
            self.frame=cv2.flip(self.frame,1)
            self.frame = cv2.resize(self.frame,(891,501))
            height, width, channel = self.frame.shape
            bytesPerLine = 3 * width

            qImg = QImage(self.frame.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            pixmap01 = QPixmap.fromImage(qImg)
            pixmap_image = QPixmap(pixmap01)
            self.ui.label.setPixmap(pixmap_image)
            self.ui.user_id.setText(self.Qr_User)

            self.ui.label.show();
            
        if (self.start ==1):
            ret,self.frame =self.camera.read()
            self.frame=cv2.flip(self.frame,1)
            #detected
            custom_objects = self.detector.CustomObjects(bottle=True)
            detected_image_array,self.detections = self.detector.detectCustomObjectsFromImage(custom_objects=custom_objects,input_type="array", input_image=self.frame , output_type="array")
            for eachObject in self.detections:
               
                print(eachObject["name"] , " : ", (eachObject["percentage_probability"]), " : ", eachObject["box_points"] )
                
                
                if int(eachObject["percentage_probability"]) >=50 :
                    self.Point+=1
                    print(self.Point)
                 
            #resize
            
            detected_image_array = cv2.resize(detected_image_array,(891,501))
            height, width, channel = detected_image_array.shape
            bytesPerLine = 3 * width
           
            qImg = QImage(detected_image_array.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            pixmap01 = QPixmap.fromImage(qImg)
            pixmap_image = QPixmap(pixmap01)
            self.ui.label.setPixmap(pixmap_image)
            self.ui.user_id.setText(self.Qr_User)
            self.ui.user_point.setText(str(self.Point))
           
                  
            self.ui.label.show();
    '''
    def score():
        d=self.detections
        for eachObject in d:
          
            if int(eachObject["percentage_probability"]) >=50 :
                self.Point+=1
                print(self.Point)
           '''
    
    def stop(self):
        #ส่งข้อมูลช่วงนี้ก่อนแล้วเคลียค่า
        print(self.Qr_User)
        print(self.Point)
        
        #self.start=0
        self.Qr_User=""
        self.Point=0
        print(self.Qr_User)
        print(self.Point)

       
       
    def start(self):
        self.update_timer.start(30)
        
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = StartWindows()
    window.show()
    app.exit(app.exec_())
