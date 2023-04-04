from PyQt5 import QtCore
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QWidget, QSizePolicy, QGridLayout, QSizeGrip
from PyQt5.QtCore import Qt
from Connection.Camera import CameraNameList
from Connection.Camera import CameraManager
from View.BottomView.GetConnected.GetConnectedSetting.get_connected_setting import GetConnectedSetting
from WorkingThread import WorkingThread
class MainWindow(QMainWindow):
    grid_central_widget: QGridLayout = None
    central_widget: QWidget = None
    size_policy: QSizePolicy = None
    workingThread: WorkingThread
    def __init__(self):
        QMainWindow.__init__(self)
        self.startPos = None
        self.workingThread = WorkingThread
        self.top_view = None
        self.bottom_view = None
        self.middle_view = None
        self.right_view = None
        self.left_view = None
        self.camera_manager = CameraManager(self)
        self.setup_window()
        self.setup_view()
        # hide window hint
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.grip_size = 8
        self.grips = []
        for _ in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.grip_size, self.grip_size)
            self.grips.append(grip)

    def setup_window(self):
        # Tạo khung cho main window, setting các thuộc tính cơ bản cho main window
        self.setWindowTitle("Vision")
        self.resize(1080, 720)
        self.setStyleSheet("background-image: url(./Resource/Icon/background2.png);")
        # self.setMaximumSize(QSize(1600, 1100))
        # not resize
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.central_widget = QWidget(self)
        self.size_policy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.size_policy.setHorizontalStretch(0)
        self.size_policy.setVerticalStretch(0)
        self.size_policy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(self.size_policy)
        self.grid_central_widget = QGridLayout(self.central_widget)
        self.grid_central_widget.setContentsMargins(0, 0, 0, 0)
        self.grid_central_widget.setHorizontalSpacing(3)
        self.grid_central_widget.setVerticalSpacing(3)

    def setup_view(self):
        # xây dựng UI cho main window
        self.setup_menu()
        self.setup_top_view()
        self.setup_left_view()
        self.setup_middle_view()
        self.setup_right_view()
        self.setup_bottom_view()
        self.setup_grid_layout()
        

    def setup_menu(self):
        return

    def setup_grid_layout(self):
        # setting  row: int, column: int, rowSpan: int, columnSpan: int
        self.grid_central_widget.addWidget(self.top_view, 0, 0, 1, 3)  # row? col? rowspan colspan?
        self.grid_central_widget.addWidget(self.left_view, 1, 0, 1, 1)
        self.grid_central_widget.addWidget(self.middle_view, 1, 1, 1, 1)
        self.grid_central_widget.addWidget(self.right_view, 1, 2, 1, 1)
        self.grid_central_widget.addWidget(self.bottom_view, 2, 0, 1, 3)

        # Cột column: int, stretch: int
        self.grid_central_widget.setColumnStretch(0, 2)
        self.grid_central_widget.setColumnStretch(1, 5)
        self.grid_central_widget.setColumnStretch(2, 2)

        # hàng  row: int, stretch: int
        self.grid_central_widget.setRowStretch(0, 2)
        self.grid_central_widget.setRowStretch(1, 11)
        self.grid_central_widget.setRowStretch(2, 4)

        self.setCentralWidget(self.central_widget)

    def setup_left_view(self):
        from View.LeftView import LeftView
        self.left_view = LeftView(parent=self.central_widget, main_window=self)

    def setup_right_view(self):
        from View.RightView.right_view import RightView
        self.right_view = RightView(parent=self.central_widget, main_window=self)

    def setup_bottom_view(self):
        from View.BottomView.bottom_view import BottomView
        self.bottom_view = BottomView(parent=self.central_widget, main_window=self)
        # self.bottom_view.hide()

    def setup_middle_view(self):
        from View.MiddleView.middle_view import MiddleView
        self.middle_view = MiddleView(parent=self.central_widget, main_window=self)

    def setup_top_view(self):
        from View.TopView.top_view import TopView
        self.top_view = TopView(parent=self.central_widget, main_window=self, camera_manager=self.camera_manager)

    # Kéo di Chuyển app
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.startPos = event.pos()

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        # todo reset position
        self.startPos = None
        return

    def mouseMoveEvent(self, event):
        try:
            if self.startPos is None:
                return
            if self.startPos.x() <= self.top_view.width() \
                    and self.startPos.y() <= self.top_view.height() \
                    and not self.isMaximized():
                self.move(self.pos() + (event.pos() - self.startPos))
        except Exception as error:
            print(error)

    # resize
    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        # top left grip doesn't need to be moved...
        # top right
        self.grips[1].move(rect.right() - self.grip_size, 0)
        # bottom right
        self.grips[2].move(
            rect.right() - self.grip_size, rect.bottom() - self.grip_size)
        # bottom left
        self.grips[3].move(0, rect.bottom() - self.grip_size)