from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
# from View.MainView.main_window import MainWindow
import os
import threading
import cv2 as cv
import numpy as np
from View.Setting.Camera.camera_parameter import CameraBrand
# from Connection.ConnectionStatus import ConnectionStatus

class WorkingThread:
    # cameraManager: CameraManager

    def __init__(self, main_window):
        from Connection.Camera import CameraManager
        self.captureVideoFlag = False
        self.originalImage = None
        self.main_window: MainWindow = main_window
        self.cameraManager = CameraManager
        self.runningFlag = True
        # self.captureVideoThread()

    def open_image(self):
        files = QFileDialog.getOpenFileNames(None, "", "", "Python file(*.png), Text Files(*)")
        path_img = files[0]
        print(path_img)
        if len(path_img):
            path_img = path_img[0]
            # print(path)
            self.main_window.middle_view.main_show.show_image_with_path(image_path=path_img)

    def connectCamera(self):
        if self.cameraManager.currentCamera.connect():
            # if not self.checkingCameraConnectionFlag:
            #     _thread.start_new_thread(self.checkCameraConnectionThread, ())
            return True
        else:
            return False

    def capturePicture(self):
        try:
            ret, image = self.cameraManager.currentCamera.takePicture()
            if ret:
                self.originalImage = image
                self.main_window.middle_view.main_show.show_image_with_numpy_image(self.originalImage)
                # if self.mainWindow.runningTab.isSelected and (
                #         self.mainWindow.startingWindow.machineName == MachineList.RUConnectorScrewMachine):
                #     self.mainWindow.ru_connectorImageFrame.showCurrentImage(self.originalImage)
                # else:
                #     self.mainWindow.showImage(
                #         self.originalImage,
                #         True, title=f"Image from camera {self.cameraManager.currentCamera.parameter.id}")
            return ret, image
        except Exception as error:
            # self.mainWindow.runningTab.insertLog("ERROR Capture picture: {}".format(error))
            print("Capture picture: {}".format(error))
            return False, ()

    def captureVideo(self):
        if self.cameraManager.currentCamera.parameter.brand == CameraBrand.basler.value:
            self.captureVideoFlag = True
            self.cameraManager.currentCamera.baslerGigECaptureVideo(self.captureVideoFlag)
        elif self.cameraManager.currentCamera.parameter.brand == CameraBrand.hikVision.value:
            self.captureVideoFlag = True
            self.cameraManager.currentCamera.hikCaptureVideo()
        else:
            self.captureVideoFlag = True
            while self.captureVideoFlag:
                try:
                    ret, _ = self.main_window.workingThread.capturePicture(self)
                    if not ret:
                        self.captureVideoFlag = False
                except Exception as error:
                    text = ("ERROR Capture video: {}".format(error))
                    print(text)
                    self.captureVideoFlag = False
                cv.waitKey(3)
            self.captureVideoFlag = False
            # self.captureVideoFlag = True
            # self.captureVideoThread()
            # thread = threading.Thread(target=self.captureVideoThread, args=())
            # thread.start()
        # _thread.start_new_thread(self.captureVideoThread, ())

    def stopCaptureVideo(self):
        self.captureVideoFlag = False
        if self.captureVideoFlag == False:
            self.main_window.workingThread.capturePicture(self)
        if self.cameraManager.currentCamera.parameter.brand == CameraBrand.basler.value:
            self.cameraManager.currentCamera.baslerGigECaptureVideo(self.captureVideoFlag)
        elif self.cameraManager.currentCamera.parameter.brand == CameraBrand.hikVision.value:
            self.cameraManager.currentCamera.hikStopCaptureVideo()

    def disconnectCamera(self):
        self.cameraManager.currentCamera.disconnect()

    def captureVideoThread(self):
        self.captureVideoFlag = True
        while self.captureVideoFlag:
            try:
                ret, _ = self.capturePicture()
                if not ret:
                    self.captureVideoFlag = False
            except Exception as error:
                print("ERROR Capture video: {}".format(error))
                self.captureVideoFlag = False
            cv.waitKey(3)
        self.captureVideoFlag = False