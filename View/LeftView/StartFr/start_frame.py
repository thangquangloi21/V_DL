from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QFont, QCursor
from View.MainView.main_window import MainWindow
from View.common_view import VisionPushButton
from View.common_view.vision_frame import VisionFrame


class StartFrame(VisionFrame):
    get_connected_btn: QPushButton = None
    grid_startFrame: QGridLayout = None
    start_label: QLabel = None

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background: transparent;    
            border-image: url(./Resource/Icon/1. Start.png);
        """)
        self.grid_startFrame = QGridLayout(self)
        self.grid_startFrame.setContentsMargins(30, 0, 30, 0)
        self.grid_startFrame.setHorizontalSpacing(0)
        self.grid_startFrame.setVerticalSpacing(0)
        return

    def setup_view(self):
        self.get_connected_view()
        self.setup_grid_layout()
        return

    def setup_grid_layout(self):
        # setting  row: int, column: int, rowSpan: int, columnSpan: int
        self.grid_startFrame.addWidget(self.get_connected_btn, 0, 0, 1, 1)

    def get_connected_view(self):
        self.get_connected_btn = VisionPushButton(parent=self,text= "Get Connected")

        self.get_connected_btn.clicked.connect(self.get_connected_btn_click)

    def get_connected_btn_click(self):
        self.main_window.bottom_view.show_frame(name="Get Connected")
