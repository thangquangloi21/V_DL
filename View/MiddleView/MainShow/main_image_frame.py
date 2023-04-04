from tkinter import EventType

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QLabel, QGridLayout
from View.common_view.vision_frame import VisionFrame
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
# from test_drag_drop_rectangle import RectangleProcess
from Modules.DeepLearning.drag_drop_rectangle import RectangleProcess
from View.MainView.main_window import MainWindow
import cv2 as cv
import numpy as np
import os


class MainShow(VisionFrame):
    rectangele_process: RectangleProcess = None
    show_image_label: QLabel = None
    grid_main_image_frame: QGridLayout = None
    original_image = None
    zoomImage = None
    current_image = None

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.path_file = None
        self.main_window: MainWindow = main_window
        self.original_image = None
        self.image_path = None
        self.setup_window()
        self.setup_view()
        self.setAcceptDrops(True)
        self.current_image = None

    def setup_window(self):
        self.setStyleSheet("""
            background: transparent;
            border-image: None;
        """)
        self.grid_main_image_frame = QGridLayout(self)
        self.grid_main_image_frame.setContentsMargins(0, 0, 0, 15)

    def setup_view(self):
        self.setup_label_view()
        self.setup_rectangle_view()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_main_image_frame.addWidget(self.show_image_label, 0, 0, 1, 1)
        self.grid_main_image_frame.addWidget(self.rectangele_process, 0, 0, 1, 1)

    def setup_label_view(self):
        self.show_image_label = QLabel(parent=self)
        self.show_image_label.setText('\n\n Show Image Here \n\n')
        self.show_image_label.setScaledContents(True)
        self.show_image_label.setStyleSheet("background: #888888")

    def setup_rectangle_view(self):
        self.rectangele_process = RectangleProcess(parent=self, main_window=self.main_window)

    shapes_image = None

    def show_image_with_path(self, image_path):
        self.image_path = image_path
        width, height, depth = QPixmap(image_path).width(), QPixmap(image_path).height(), QPixmap(image_path).depth()
        self.shapes_image = (width, height, depth)
        self.main_window.middle_view.main_show.show_image_label.setPixmap(QPixmap(image_path))
        print(f"shape label on window: {self.show_image_label.width(), self.show_image_label.height()} ")
        print(f"shape_image: {self.shapes_image}")

    def show_image_with_numpy_image(self, numpy_image):
        print(numpy_image.shape)
        self.original_image = numpy_image
        print(self.original_image)
        height, width, channel = numpy_image.shape
        bytes_per_line = 3 * width
        try:
            qt_image = QImage(numpy_image.data, width, height, bytes_per_line, QImage.Format_BGR888)
        except:
            qt_image = QImage(numpy_image.data.tobytes(), width, height, bytes_per_line, QImage.Format_BGR888)
        self.main_window.middle_view.main_show.show_image_label.setPixmap(QtGui.QPixmap(qt_image))

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.main_window.top_view.toolBar.get_all_image(file_path)

            event.accept()
        else:
            event.ignore()

    def resetZoom(self):
        self.resetBasePoint()
        self.zoomImage = None
        self.zoomScale = 100
        self.multipleScale = 10
        self.zoomLabel = "Zoom"

    def resetBasePoint(self):
        self.basePoint = [0, 0, 0, 0]
        self.zoomImage = None
        self.zoomScale = 100

    # def wheelEvent(self, event):
    #     print("img_begin: ", self.original_image.shape)
    #     print("lan", event.pos())
    #     realPosX = event.pos().x()
    #     print(realPosX)
    #     realPosY = event.pos().y()
    #     print(realPosY)
    #
    #     print("angle", event.angleDelta().y())
    #     zoomDelta = event.angleDelta().y()/ 120
    #     # print("Mouse wheel delta = {}".format(zoomDelta))
    #     # print(f"x = {realPosX}, y = {realPosY}")
    #     # print(f"base point = {self.basePoint}")
    #     if self.zoomImage is not None:
    #         baseHeight = self.zoomImage.shape[0]
    #         baseWidth = self.zoomImage.shape[1]
    #         # print(f"height={self.zoomImage.shape[0]}, width = {self.zoomImage.shape[1]}")
    #     else:
    #         self.zoomImage = self.original_image.copy()
    #         print(self.zoomImage)
    #         baseHeight = self.original_image.shape[0]
    #         baseWidth = self.original_image.shape[1]
    #         # print(f"height={self.currentImage.shape[0]}, width = {self.currentImage.shape[1]}")
    #     zoomDelta = int(zoomDelta * self.multipleScale)
    #     print(f"zoom Delta = {zoomDelta}")
    #
    #     if self.zoomScale + zoomDelta > 100:
    #         self.zoomScale = self.zoomScale + zoomDelta
    #         # print(f"zoom scale = {self.zoomScale}")
    #
    #
    #         zoomHeight = int(100 * baseHeight / self.zoomScale)
    #         zoomWidth = int(100 * baseWidth / self.zoomScale)
    #         # print(f"zoom height = {zoomHeight}, zoom width = {zoomWidth}")
    #
    #         zoomCusorX = self.basePoint[0] + realPosX
    #         zoomCusorY = self.basePoint[1] + realPosY
    #
    #         zoomCenterX = self.basePoint[0] + int(self.original_image.shape[1] / 2)
    #         zoomCenterY = self.basePoint[1] + int(self.original_image.shape[0] / 2)
    #
    #         startZoomX = zoomCenterX - int(zoomWidth / 2)
    #         startZoomY = zoomCenterY - int(zoomHeight / 2)
    #
    #         realCusorXAfterZoom = startZoomX + int(event.pos().x() * zoomWidth / self.show_image_label.width())
    #         realCusorYAfterZoom = startZoomY + int(event.pos().y() * zoomHeight / self.show_image_label.height())
    #
    #         deltaMoveX = zoomCusorX - realCusorXAfterZoom
    #         deltaMoveY = zoomCusorY - realCusorYAfterZoom
    #
    #         startZoomX = startZoomX + deltaMoveX
    #         startZoomY = startZoomY + deltaMoveY
    #
    #         endZoomX = startZoomX + zoomWidth
    #         endZoomY = startZoomY + zoomHeight
    #
    #         # print(f"deltaMove X = {deltaMoveX}, delta move y = {deltaMoveY}")
    #
    #         if startZoomX < 0:
    #             startZoomX = 0
    #             endZoomY = startZoomX + zoomWidth
    #         if endZoomX > baseWidth:
    #             endZoomX = baseHeight
    #             startZoomX = baseHeight - zoomWidth
    #         if startZoomY < 0:
    #             startZoomY = 0
    #             endZoomY = startZoomY + zoomHeight
    #         if endZoomY > baseHeight:
    #             endZoomY = baseHeight
    #             startZoomY = baseHeight - zoomHeight
    #
    #         self.original_image = self.zoomImage[startZoomY: endZoomY, startZoomX: endZoomX]
    #         print("nupy", self.original_image)
    #         print("mg_lasst", self.original_image.shape)
    #         self.main_window.top_view.toolBar.originalImage = self.original_image
    #         self.show_image_with_numpy_image(self.original_image)
    #         self.basePoint = (startZoomX, startZoomY, zoomWidth, zoomHeight)
    #
    #     else:
    #         self.original_image = self.zoomImage.copy()
    #         print("mg_lasst", self.original_image)
    #         self.show_image_with_numpy_image(self.original_image)
    #         self.zoomImage = None



