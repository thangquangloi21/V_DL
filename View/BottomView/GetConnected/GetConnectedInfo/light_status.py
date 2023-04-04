from PyQt5.QtWidgets import QLabel, QGridLayout
from View.common_view.vision_frame import VisionFrame


class LightStatus(VisionFrame):
    name: QLabel = None
    label1: QLabel
    label2: QLabel
    label3: QLabel
    label4: QLabel
    label5: QLabel
    label6: QLabel
    id: QLabel
    baud: QLabel
    size: QLabel
    par: QLabel
    stop: QLabel
    grid_light: QGridLayout

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
        self.grid_light = QGridLayout(self)

    def setup_view(self):
        self.brand_light()
        self.com_port()
        self.baud_rate()
        self.data_size()
        self.parity()
        self.stop_bit()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_light.addWidget(self.label1, 0, 0, 1, 1)
        self.grid_light.addWidget(self.name, 0, 1, 1, 1)
        self.grid_light.addWidget(self.label2, 1, 0, 1, 1)
        self.grid_light.addWidget(self.id, 1, 1, 1, 1)
        self.grid_light.addWidget(self.label3, 2, 0, 1, 1)
        self.grid_light.addWidget(self.baud, 2, 1, 1, 1)
        self.grid_light.addWidget(self.label4, 3, 0, 1, 1)
        self.grid_light.addWidget(self.size, 3, 1, 1, 1)
        self.grid_light.addWidget(self.label5, 4, 0, 1, 1)
        self.grid_light.addWidget(self.par, 4, 1, 1, 1)
        self.grid_light.addWidget(self.label6, 5, 0, 1, 1)
        self.grid_light.addWidget(self.stop, 5, 1, 1, 1)

        self.grid_light.setColumnStretch(0, 1)
        self.grid_light.setColumnStretch(1, 3)

    def brand_light(self):
        self.label1 = QLabel(parent=self, text="Brand::")
        self.name = QLabel(parent=self, text="VST-Light")

    def com_port(self):
        self.label2 = QLabel(parent=self, text="COM Port:")
        self.id = QLabel(parent=self, text="COM1")

    def baud_rate(self):
        self.label3 = QLabel(parent=self, text="Baud rate:")
        self.baud = QLabel(parent=self, text="38400")

    def data_size(self):
        self.label4 = QLabel(parent=self, text="Data size:")
        self.size = QLabel(parent=self, text="5")

    def parity(self):
        self.label5 = QLabel(parent=self, text="Parity:")
        self.par = QLabel(parent=self, text="None")

    def stop_bit(self):
        self.label6 = QLabel(parent=self, text="Stop bit:")
        self.stop = QLabel(parent=self, text="1")

    def current_status(self):
        return

    def update_status(self):
        return