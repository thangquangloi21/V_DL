from PyQt5.QtWidgets import QLabel, QGridLayout
from View.common_view.vision_frame import VisionFrame


class CameraStatus(VisionFrame):
    name: QLabel
    label1: QLabel
    label2: QLabel
    id: QLabel
    label3: QLabel
    connection: QLabel
    label4: QLabel
    brand: QLabel
    label5: QLabel
    flip: QLabel
    label6: QLabel
    rotate: QLabel
    grid_camera: QGridLayout

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
        self.grid_camera = QGridLayout(self)

    def setup_view(self):
        self.name_camera()
        self.id_camera()
        self.connection_camera()
        self.brand_camera()
        self.flip_camera()
        self.rotate_camera()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_camera.addWidget(self.label1, 0, 0, 1, 1)
        self.grid_camera.addWidget(self.name, 0, 1, 1, 1)
        self.grid_camera.addWidget(self.label2, 1, 0, 1, 1)
        self.grid_camera.addWidget(self.id, 1, 1, 1, 1)
        self.grid_camera.addWidget(self.label3, 2, 0, 1, 1)
        self.grid_camera.addWidget(self.connection, 2, 1, 1, 1)
        self.grid_camera.addWidget(self.label4, 3, 0, 1, 1)
        self.grid_camera.addWidget(self.brand, 3, 1, 1, 1)
        self.grid_camera.addWidget(self.label5, 4, 0, 1, 1)
        self.grid_camera.addWidget(self.flip, 4, 1, 1, 1)
        self.grid_camera.addWidget(self.label6, 5, 0, 1, 1)
        self.grid_camera.addWidget(self.rotate, 5, 1, 1, 1)

        self.grid_camera.setColumnStretch(0, 1)
        self.grid_camera.setColumnStretch(1, 3)

    def name_camera(self):
        self.label1 = QLabel(parent=self, text="Name:")
        self.name = QLabel(parent=self, text="Camera 0")

    def id_camera(self):
        self.label2 = QLabel(parent=self, text="ID:")
        self.id = QLabel(parent=self, text="0")

    def connection_camera(self):
        self.label3 = QLabel(parent=self, text="Connection:")
        self.connection = QLabel(parent=self, text="USB 3")

    def brand_camera(self):
        self.label4 = QLabel(parent=self, text="Brand:")
        self.brand = QLabel(parent=self, text="HIK Vision")

    def flip_camera(self):
        self.label5 = QLabel(parent=self, text="Flip:")
        self.flip = QLabel(parent=self, text="None")

    def rotate_camera(self):
        self.label6 = QLabel(parent=self, text="Rotate:")
        self.rotate = QLabel(parent=self, text="0")

    def current_status(self):
        return

    def update_status(self):
        return
