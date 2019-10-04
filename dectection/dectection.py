from imageai.Detection import VideoObjectDetection
from imageai.Detection import ObjectDetection
import numpy as np
import cv2
import os
import datetime
import time
import glob
import sys
from gui_finish import Ui_Form
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

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update)
        #button
       
        #camera
        self.camera = cv2.VideoCapture(0)
        self.update_timer.start(30)
        self.execution_path = os.getcwd()
        #model
        
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath( os.path.join(self.execution_path , "yolo-tiny.h5"))
        self.detector.loadModel(detection_speed="fast")
        print("###you are use yolo_tiny model###")
        
    def update(self):
        
        ret,self.frame =self.camera.read()
        self.frame=cv2.flip(self.frame,1)
        #detected
        custom=self.ui.comboBox_2.currentText()
        print(custom)
        custom_objects = self.detector.CustomObjects(bottle=True)
        detected_image_array,self.detections = self.detector.detectCustomObjectsFromImage(custom_objects=custom_objects,input_type="array", input_image=self.frame , output_type="array")
        #detected_image_array, detections = self.detector.detectCustomObjectsFromImage(custom_objects=custom_objects,output_type="array",input_type="array", input_image= frame,display_percentage_probability=True, display_object_name=True)
        for eachObject in self.detections:
            print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    
            
            
        #resize
        detected_image_array = cv2.resize(detected_image_array,(851,471))
        height, width, channel = detected_image_array.shape
        bytesPerLine = 3 * width

        qImg = QImage(detected_image_array.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        pixmap01 = QPixmap.fromImage(qImg)
        pixmap_image = QPixmap(pixmap01)
        self.ui.label.setPixmap(pixmap_image)

              
        self.ui.label.show();
if __name__ == '__main__':
    app = QApplication([])
    window = StartWindows()
    window.show()
    app.exit(app.exec_())
