from PyQt5.QtWidgets import QPushButton, QSizePolicy
from View.common_view.vision_frame import VisionFrame


class ResultTab(VisionFrame):
    Close: QPushButton
    sizePolicy: QSizePolicy

    def __init__(self, parent):
        VisionFrame.__init__(self, parent=parent)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)
        self.setStyleSheet("""
            QFrame{
                background: transparent;
                border-image: None;
            }
            QPushButton{
                background: grey;
                font: 15px;
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: orange;
            }
            QPushButton:pressed{
                background-color: rgb(14, 68, 184);
            } 
        """)

    def setup_view(self):
        self.Close = QPushButton(parent=self, text="OK")
        self.Close.resize(50, 50)
        self.Close.move(50, 50)
