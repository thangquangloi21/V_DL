from PyQt5.QtWidgets import QGroupBox, QGridLayout, QSizePolicy
from PyQt5.QtCore import QSize
# from View.MainView.main_window import MainWindow
from View.common_view.vision_push_button import VisionPushButton


class CreateLabel(QGroupBox):
    grid_createLabel: QGridLayout
    open_fordel: VisionPushButton
    create_img: VisionPushButton
    create_label: VisionPushButton
    sizePolicy: QSizePolicy

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setTitle("Create Label")
        self.setStyleSheet("""
            QGroupBox {
                background: transparent;
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
        self.setMaximumSize(QSize(300, 16777215))

        self.grid_createLabel = QGridLayout(self)

        self.grid_createLabel.setVerticalSpacing(30)
        self.grid_createLabel.setContentsMargins(10, 50, 10, 0)

    def setup_view(self):
        self.setup_open_btn()
        self.setup_create_img()
        self.setup_create_labe()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_createLabel.addWidget(self.open_fordel, 0, 0, 1, 1)
        self.grid_createLabel.addWidget(self.create_img, 1, 0, 1, 1)
        self.grid_createLabel.addWidget(self.create_label, 2, 0, 1, 1)

        self.grid_createLabel.setRowStretch(0, 1)
        self.grid_createLabel.setRowStretch(1, 1)
        self.grid_createLabel.setRowStretch(2, 1)
        self.grid_createLabel.setRowStretch(3, 1)

    def setup_open_btn(self):
        self.open_fordel = VisionPushButton(parent=self, text="Open folder")

    def setup_create_img(self):
        self.create_img = VisionPushButton(parent=self, text="Create image")

    def setup_create_labe(self):
        self.create_label = VisionPushButton(parent=self, text="Create label")