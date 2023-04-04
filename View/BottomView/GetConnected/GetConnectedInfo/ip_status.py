from PyQt5.QtWidgets import QLabel, QGridLayout
from View.common_view.vision_frame import VisionFrame
from PyQt5.QtCore import QSize


class IpStatus(VisionFrame):
    label1: QLabel
    ip_cam: QLabel
    label2: QLabel
    ip_plc: QLabel
    label3: QLabel
    ip_server: QLabel
    grid_ipStatus: QGridLayout

    def __init__(self, parent):
        VisionFrame.__init__(self, parent)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            QLabel{
                color: white;
                font: 15px;
            }
            QFrame{
                background: transparent;
            }
        """)
        self.grid_ipStatus = QGridLayout(self)
        self.grid_ipStatus.setContentsMargins(30, 0, 0, 0)
        self.grid_ipStatus.setVerticalSpacing(20)
        self.grid_ipStatus.setHorizontalSpacing(10)
        self.setMaximumSize(QSize(300, 200))

    def setup_view(self):
        self.camera_ip()
        self.plc_ip()
        self.server_ip()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_ipStatus.addWidget(self.label1, 1, 0, 1, 1)
        self.grid_ipStatus.addWidget(self.ip_cam, 1, 1, 1, 1)
        self.grid_ipStatus.addWidget(self.label2, 2, 0, 1, 1)
        self.grid_ipStatus.addWidget(self.ip_plc, 2, 1, 1, 1)
        self.grid_ipStatus.addWidget(self.label3, 3, 0, 1, 1)
        self.grid_ipStatus.addWidget(self.ip_server, 3, 1, 1, 1)

        self.grid_ipStatus.setColumnStretch(0, 1)
        self.grid_ipStatus.setColumnStretch(1, 2)
        self.grid_ipStatus.setRowStretch(0, 1)
        self.grid_ipStatus.setRowStretch(1, 1)
        self.grid_ipStatus.setRowStretch(2, 1)
        self.grid_ipStatus.setRowStretch(3, 1)
        self.grid_ipStatus.setRowStretch(4, 1)
        self.grid_ipStatus.setRowStretch(5, 1)

    def camera_ip(self):
        self.label1 = QLabel(parent=self, text="IP Camera:")
        self.ip_cam = QLabel(parent=self, text="None")

    def plc_ip(self):
        self.label2 = QLabel(parent=self, text="IP PLC:")
        self.ip_plc = QLabel(parent=self, text="None")

    def server_ip(self):
        self.label3 = QLabel(parent=self, text="IP Server:")
        self.ip_server = QLabel(parent=self, text="None")

    def current_ip(self):
        return

    def update_ip(self):
        return