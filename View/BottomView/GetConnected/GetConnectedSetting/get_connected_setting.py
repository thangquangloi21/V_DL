from PyQt5.QtWidgets import QGroupBox, QPushButton, QGridLayout, QSizePolicy,QLabel,QLineEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from View.BottomView.GetConnected.get_connected import GetConnected
from View.common_view.vision_label import VisionLabel
from Connection.ConnectionStatus import ConnectionStatus

class GetConnectedSetting(QGroupBox):
    icon: QIcon
    camera_label: VisionLabel
    cam_stt: QLabel
    cam_btn: QPushButton
    plc_label: VisionLabel
    plc_stt: VisionLabel
    plc_btn: QPushButton
    server_label: VisionLabel
    server_stt: VisionLabel
    server_btn: QPushButton
    light_label: VisionLabel
    light_stt: VisionLabel
    light_btn: QPushButton
    grid_getconnected: QGridLayout
    sizePolicy: QSizePolicy

    def __init__(self, parent, main_window):
        from View.MainView.main_window import MainWindow
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.get_connected: GetConnected = parent
        self.setup_window()
        self.setup_view()
        self.setCameraStatus()



    def setup_window(self):
        self.setTitle("Get Connected")
        self.setStyleSheet("""
            QGroupBox {
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
            QPushButton{
                background-color: transparent;
            }
            QPushButton:hover{
                background-color: rgb(127, 127, 127);
            }
            QPushButton:pressed{
                background-color: rgb(14, 68, 184);
            }
        """)
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap("./Resource/Icon/icon_info.png"), QIcon.Normal, QIcon.Off)
        self.setMaximumSize(QSize(300, 16777215))
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)

        self.grid_getconnected = QGridLayout(self)
        self.grid_getconnected.setContentsMargins(5, 5, 5, 5)
        self.grid_getconnected.setVerticalSpacing(1)

    def setup_view(self):
        self.camera_status()
        self.plc_status()
        self.server_status()
        self.light_status()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_getconnected.addWidget(self.camera_label, 0, 0, 1, 1)
        self.grid_getconnected.addWidget(self.cam_stt, 0, 1, 1, 1)
        self.grid_getconnected.addWidget(self.cam_btn, 0, 2, 1, 1)

        self.grid_getconnected.addWidget(self.plc_label, 1, 0, 1, 1)
        self.grid_getconnected.addWidget(self.plc_stt, 1, 1, 1, 1)
        self.grid_getconnected.addWidget(self.plc_btn, 1, 2, 1, 1)

        self.grid_getconnected.addWidget(self.server_label, 2, 0, 1, 1)
        self.grid_getconnected.addWidget(self.server_stt, 2, 1, 1, 1)
        self.grid_getconnected.addWidget(self.server_btn, 2, 2, 1, 1)

        self.grid_getconnected.addWidget(self.light_label, 3, 0, 1, 1)
        self.grid_getconnected.addWidget(self.light_stt, 3, 1, 1, 1)
        self.grid_getconnected.addWidget(self.light_btn, 3, 2, 1, 1)

        self.grid_getconnected.setColumnStretch(0, 4)
        self.grid_getconnected.setColumnStretch(1, 4)
        self.grid_getconnected.setColumnStretch(2, 1)

        self.grid_getconnected.setRowStretch(0, 1)
        self.grid_getconnected.setRowStretch(1, 1)
        self.grid_getconnected.setRowStretch(2, 5)
        self.grid_getconnected.setRowStretch(3, 1)

    def camera_status(self):
        self.camera_label = VisionLabel( text="Camera Status:")
        self.cam_stt = VisionLabel(text="Disconnected")
        self.cam_stt.red_color()
        # self.cam_stt = QLabel()
        # self.cam_stt= QLabel(text="Disconnected")
        # self.cam_stt.red_color()
        self.cam_btn = QPushButton(parent=self)
        self.cam_btn.setIcon(self.icon)
        self.cam_btn.clicked.connect(self.click_cam_status_btn)

    def setCameraStatus(self,status=ConnectionStatus.disconnected):
        if status == ConnectionStatus.connected:
            self.cam_stt.setText("Connected")
            # self.cam_stt = VisionLabel(text="Connected")
            self.cam_stt.green_color()

        elif status == ConnectionStatus.disconnected:
            # self.cam_stt.setText("Disconnected")
            self.cam_stt.setText("Disconnected")
            self.cam_stt.red_color()
        # print(self.cam_stt)

        # elif status == ConnectionStatus.reconnecting:
        #     self.cam_stt = QLineEdit("Disconnected")

    def plc_status(self):
        self.plc_label = VisionLabel( text="PLC Status:")
        self.plc_stt = VisionLabel( text="Disconnected")
        self.plc_stt.red_color()
        self.plc_btn = QPushButton(parent=self)
        self.plc_btn.setIcon(self.icon)
        self.plc_btn.clicked.connect(self.click_plc_status_btn)

    def server_status(self):
        self.server_label = VisionLabel( text="Server Status:")
        self.server_stt = VisionLabel( text="Disconnected")
        self.server_stt.red_color()
        self.server_btn = QPushButton(parent=self)
        self.server_btn.setIcon(self.icon)
        self.server_btn.clicked.connect(self.click_server_status_btn)

    def light_status(self):
        self.light_label = VisionLabel( text="Light Status:")
        self.light_stt = VisionLabel( text="Disconnected")
        self.light_stt.red_color()
        self.light_btn = QPushButton(parent=self)
        self.light_btn.setIcon(self.icon)
        self.light_btn.clicked.connect(self.click_light_status_btn)

    def click_cam_status_btn(self):
        self.get_connected.get_connected_info.show_connected_frame("Camera status")

    def click_plc_status_btn(self):
        self.get_connected.get_connected_info.show_connected_frame("Plc status")

    def click_server_status_btn(self):
        self.get_connected.get_connected_info.show_connected_frame("Server status")

    def click_light_status_btn(self):
        self.get_connected.get_connected_info.show_connected_frame("Light status")
