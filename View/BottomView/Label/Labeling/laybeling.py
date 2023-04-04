from PyQt5.QtWidgets import QGroupBox, QGridLayout, QSizePolicy
from PyQt5.QtCore import QSize
# from View.MainView.main_window import MainWindow
from View.common_view.vision_label import VisionLabel


class Labeling(QGroupBox):
    sizePolicy: QSizePolicy
    grid_laybeling: QGridLayout
    show_img: VisionLabel

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setTitle("Labeling")
        self.setStyleSheet("""
            QGroupBox {
                background: red;
                color: white;
                font: 18px;
                font-weight: bold;
                background-color:transparent;
                border: 2px solid gray;
                border-radius: 5px;
                margin-top: 1ex; /* leave space at the top for the title */
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 0px 0px 0px; 
                border-image: None;
            }
        """)
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)
        self.setMaximumSize(QSize(300, 16777215))
        self.grid_laybeling = QGridLayout(self)

    def setup_view(self):
        self.setup_show_img()
        self.grid_laybeling.addWidget(self.show_img, 0, 0, 1, 1)

    def setup_show_img(self):
        self.show_img = VisionLabel( text="ShowImage")
