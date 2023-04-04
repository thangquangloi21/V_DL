import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from View.MiddleView.MainShow.main_image_frame import MainShow
from View.MiddleView.ListImage.list_image_frame import ListImage
from View.MiddleView.Status.status_frame import Startus
from View.MainView.main_window import MainWindow
from View.common_view.vision_frame import VisionFrame


class MiddleView(VisionFrame):
    main_show: MainShow = None
    list_image: ListImage = None
    statuss: Startus = None
    next_btn: QPushButton = None
    last_btn: QPushButton = None
    grid_MiddleView: QGridLayout = None

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            QFrame{
                background: transparent;
                border-image: url(./Resource/Icon/Rectangle 6.png);
            }
            QPushButton{
                background: transparent;
                height:200px;
                width:20px;
            }
            QPushButton:hover{
                background-color:grey;
            }
            QPushButton:pressed{
                background-color:rgb(255, 118, 39);
            }
        """)
        self.grid_MiddleView = QGridLayout(self)
        self.grid_MiddleView.setContentsMargins(0, 10, 0, 0)  # left top right bt

    def setup_view(self):
        self.setup_main_show()
        self.setup_last_btn()
        self.setup_next_btn()
        self.setup_status()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        # setting  row: int, column: int, rowSpan: int, columnSpan: int
        self.grid_MiddleView.addWidget(self.main_show, 0, 1, 3, 3)
        self.grid_MiddleView.addWidget(self.last_btn, 1, 0, 1, 1)
        self.grid_MiddleView.addWidget(self.next_btn, 1, 4, 1, 1)
        self.grid_MiddleView.addWidget(self.statuss, 3, 0, 1, 5)

        # Hàng  row: int, stretch: int
        self.grid_MiddleView.setRowStretch(0, 4)
        self.grid_MiddleView.setRowStretch(1, 3)
        self.grid_MiddleView.setRowStretch(2, 4)
        self.grid_MiddleView.setRowStretch(3, 1)

        # Cột column: int, stretch: int
        self.grid_MiddleView.setColumnStretch(0, 1)
        self.grid_MiddleView.setColumnStretch(1, 1)
        self.grid_MiddleView.setColumnStretch(2, 6)
        self.grid_MiddleView.setColumnStretch(3, 1)
        self.grid_MiddleView.setColumnStretch(4, 1)

    def setup_main_show(self):
        self.main_show = MainShow(parent=self, main_window=self.main_window)
        # self.main_show.setMaximumSize(QSize(700, 500))

    def setup_status(self):
        self.statuss = Startus(parent=self)

    def setup_next_btn(self):
        self.next_btn = QPushButton(parent=self)
        icon_next_btn = QIcon()
        icon_next_btn.addPixmap(QPixmap("./Resource/Icon/next_button.png"), QIcon.Normal, QIcon.Off)
        self.next_btn.setIcon(icon_next_btn)
        self.next_btn.setMaximumSize(QSize(50, 200))
        self.next_btn.clicked.connect(self.next_pic)

    def setup_last_btn(self):
        self.last_btn = QPushButton(parent=self)
        icon_last_btn = QIcon()
        icon_last_btn.addPixmap(QPixmap("./Resource/Icon/previous_button.png"), QIcon.Normal, QIcon.Off)
        self.last_btn.setIcon(icon_last_btn)
        self.last_btn.setMaximumSize(QSize(50, 200))
        self.last_btn.clicked.connect(self.back_pic)

    def next_pic(self):
        if self.main_window.top_view.toolBar.current_index < len(self.main_window.top_view.toolBar.list_image_path) - 1:
            self.main_window.top_view.toolBar.current_index += 1
            print(self.main_window.top_view.toolBar.current_index)
            self.main_window.top_view.toolBar.originalImage = cv.imdecode(np.fromfile(self.main_window.top_view.toolBar.list_image_path[self.main_window.top_view.toolBar.current_index], dtype=np.uint8), cv.IMREAD_COLOR)
            self.main_window.middle_view.main_show.show_image_with_numpy_image(self.main_window.top_view.toolBar.originalImage)

    def back_pic(self):
        if self.main_window.top_view.toolBar.current_index > 0:
            self.main_window.top_view.toolBar.current_index -= 1
            print(self.main_window.top_view.toolBar.current_index)
            self.main_window.top_view.toolBar.originalImage = cv.imdecode(
                np.fromfile(self.main_window.top_view.toolBar.list_image_path[self.main_window.top_view.toolBar.current_index], dtype=np.uint8), cv.IMREAD_COLOR)
            self.main_window.middle_view.main_show.show_image_with_numpy_image( self.main_window.top_view.toolBar.originalImage)
