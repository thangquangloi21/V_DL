from PyQt5.QtWidgets import QLabel, QGridLayout
from View.common_view.vision_frame import VisionFrame


class ServerStatus(VisionFrame):
    label1: QLabel
    ip: QLabel
    grid_server: QGridLayout

    def __init__(self, parent):
        VisionFrame.__init__(self, parent=parent)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            QFrame{
                background: transparent;
            }
            QLabel{
                color: white;
                font: 15px;
            }
        """)
        self.grid_server = QGridLayout(self)

    def setup_view(self):
        self.ip_plc()
        self.grid_server.addWidget(self.label1, 1, 0, 1, 1)
        self.grid_server.addWidget(self.ip, 1, 1, 1, 1)
        self.grid_server.setColumnStretch(0, 1)
        self.grid_server.setColumnStretch(1, 3)
        self.grid_server.setRowStretch(0, 1)
        self.grid_server.setRowStretch(1, 1)
        self.grid_server.setRowStretch(2, 1)
        self.grid_server.setRowStretch(3, 1)
        self.grid_server.setRowStretch(4, 1)
        self.grid_server.setRowStretch(5, 1)

    def ip_plc(self):
        self.label1 = QLabel(parent=self, text="IP:")
        self.ip = QLabel(parent=self, text="None")

    def current_status(self):
        return

    def update_status(self):
        return
