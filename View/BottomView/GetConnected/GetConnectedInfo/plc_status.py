from PyQt5.QtWidgets import QLabel, QGridLayout
from View.common_view.vision_frame import VisionFrame


class PLCStatus(VisionFrame):
    label1: QLabel
    name: QLabel
    label2: QLabel
    id: QLabel
    grid_plc: QGridLayout

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
        self.grid_plc = QGridLayout(self)

    def setup_view(self):
        self.name_plc()
        self.ip_plc()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_plc.addWidget(self.label1, 1, 0, 1, 1)
        self.grid_plc.addWidget(self.name, 1, 1, 1, 1)
        self.grid_plc.addWidget(self.label2, 2, 0, 1, 1)
        self.grid_plc.addWidget(self.id, 2, 1, 1, 1)

        self.grid_plc.setColumnStretch(0, 1)
        self.grid_plc.setColumnStretch(1, 3)
        self.grid_plc.setRowStretch(0, 1)
        self.grid_plc.setRowStretch(1, 1)
        self.grid_plc.setRowStretch(2, 1)
        self.grid_plc.setRowStretch(3, 1)
        self.grid_plc.setRowStretch(4, 1)
        self.grid_plc.setRowStretch(5, 1)

    def name_plc(self):
        self.label1 = QLabel(parent=self, text="Name:")
        self.name = QLabel(parent=self, text="ROBOT")

    def ip_plc(self):
        self.label2 = QLabel(parent=self, text="IP:")
        self.id = QLabel(parent=self, text="None")

    def current_status(self):
        return

    def update_status(self):
        return
