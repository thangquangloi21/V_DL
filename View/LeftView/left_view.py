from PyQt5.QtWidgets import QPushButton, QGridLayout, QSizePolicy
from PyQt5.QtCore import QSize
from View.LeftView.StartFr.start_frame import StartFrame
from View.LeftView.SetUpFr.set_up_tools_frame import SetUpTools
from View.LeftView.FinishFr.finish_frame import FinishFrame
from View.MainView.main_window import MainWindow
from View.common_view.vision_frame import VisionFrame

SPACE = 10


class LeftView(VisionFrame):
    start_frame: StartFrame = None
    set_up_tools_frame: SetUpTools = None
    finish_frame: FinishFrame = None
    grid_LeftView: QGridLayout = None
    sizePolicy: QSizePolicy = None

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("border-image: url(./Resource/Icon/Rectangle 4.png);")
        self.setMaximumSize(QSize(300, 16777215))
        self.grid_LeftView = QGridLayout(self)
        self.grid_LeftView.setContentsMargins(5, 5, 5, 5)
        return

    def setup_view(self):
        self.setup_start()
        self.setup_tools()
        self.setup_finish()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_LeftView.addWidget(self.start_frame, 0, 0, 1, 1)
        self.grid_LeftView.addWidget(self.set_up_tools_frame, 1, 0, 1, 1)
        self.grid_LeftView.addWidget(self.finish_frame, 2, 0, 1, 1)

        self.grid_LeftView.setRowStretch(0, 2)
        self.grid_LeftView.setRowStretch(1, 4)
        self.grid_LeftView.setRowStretch(2, 3)

    def setup_start(self):
        self.start_frame = StartFrame(parent=self, main_window=self.main_window)

    def setup_tools(self):
        self.set_up_tools_frame = SetUpTools(parent=self, main_window=self.main_window)

    def setup_finish(self):
        self.finish_frame = FinishFrame(parent=self, main_window=self.main_window)
