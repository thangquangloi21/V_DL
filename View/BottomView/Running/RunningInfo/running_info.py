from PyQt5.QtWidgets import QGroupBox, QGridLayout, QSizePolicy
from PyQt5.QtCore import QSize
# from View.MainView.main_window import MainWindow
from View.common_view.vision_label import VisionLabel
from View.common_view.vision_push_button import VisionPushButton
from Connection.ConnectionStatus import ConnectionStatus

class RunningInfo(QGroupBox):
    grid_running_info: QGridLayout
    lbl_cam: VisionLabel
    cam_status: VisionLabel
    lbl_plc: VisionLabel
    plc_status: VisionLabel
    lbl_server: VisionLabel
    server_status: VisionLabel
    lbl_light: VisionLabel
    light_status: VisionLabel
    btn_start: VisionPushButton
    sizePolicy: QSizePolicy

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setTitle("Running")
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
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)
        self.grid_running_info = QGridLayout(self)

    def setup_view(self):
        self.setup_label()
        self.setup_btn()
        self.setup_grid_layoutt()

    def setup_grid_layoutt(self):
        self.grid_running_info.addWidget(self.lbl_cam, 0, 0, 1, 2)
        self.grid_running_info.addWidget(self.cam_status, 0, 3, 1, 1)
        self.grid_running_info.addWidget(self.lbl_plc, 1, 0, 1, 2)
        self.grid_running_info.addWidget(self.plc_status, 1, 3, 1, 1)
        self.grid_running_info.addWidget(self.lbl_server, 2, 0, 1, 2)
        self.grid_running_info.addWidget(self.server_status, 2, 3, 1, 1)
        self.grid_running_info.addWidget(self.lbl_light, 3, 0, 1, 2)
        self.grid_running_info.addWidget(self.light_status, 3, 3, 1, 1)
        self.grid_running_info.addWidget(self.btn_start, 4, 1, 1, 3)

        self.grid_running_info.setColumnStretch(0, 1)
        self.grid_running_info.setColumnStretch(1, 1)
        self.grid_running_info.setColumnStretch(2, 5)
        self.grid_running_info.setColumnStretch(3, 5)

        self.grid_running_info.setRowStretch(0, 1)
        self.grid_running_info.setRowStretch(1, 1)
        self.grid_running_info.setRowStretch(2, 1)
        self.grid_running_info.setRowStretch(3, 1)
        self.grid_running_info.setRowStretch(4, 1)

    def setup_label(self):
        self.lbl_cam = VisionLabel( text="Camera Status:")
        self.cam_status = VisionLabel( text="Disconnected")
        self.cam_status.red_color()
        self.lbl_plc = VisionLabel( text="PLC Status:")
        self.plc_status = VisionLabel( text="Disconnected")
        self.plc_status.red_color()
        self.lbl_server = VisionLabel( text="Server Status:")
        self.server_status = VisionLabel( text="Disconnected")
        self.server_status.red_color()
        self.lbl_light = VisionLabel( text="Light Status:")
        self.light_status = VisionLabel( text="Disconnected")
        self.light_status.red_color()

    def setup_btn(self):
        self.btn_start = VisionPushButton(parent=self, text="Start")
