from PyQt5.QtWidgets import QGroupBox, QSizePolicy, QGridLayout
from View.BottomView.GetConnected.GetConnectedInfo.ip_status import IpStatus
from View.BottomView.GetConnected.GetConnectedInfo.camera_status import CameraStatus
from View.BottomView.GetConnected.GetConnectedInfo.plc_status import PLCStatus
from View.BottomView.GetConnected.GetConnectedInfo.server_status import ServerStatus
from View.BottomView.GetConnected.GetConnectedInfo.light_status import LightStatus
# from View.MainView.main_window import MainWindow


class GetConnectedInfo(QGroupBox):
    current_showed_connected_frame = None
    sizePolicy: QSizePolicy
    ip_status: IpStatus = None
    cam_status: CameraStatus = None
    plc_status: PLCStatus = None
    server_status: ServerStatus = None
    light_status: LightStatus = None
    grid_get_connected_info: QGridLayout

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setTitle("Infomation")
        self.setStyleSheet("""
            QGroupBox {
                background: rgb(100, 100, 100);
                color: white;
                font: 18px;
                font-weight: bold;
                /*background-color:transparent;*/
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
        self.grid_get_connected_info = QGridLayout(self)

    def setup_view(self):
        self.setup_ip_status()
        self.setup_cam_status()
        self.setup_plc_status()
        self.setup_server()
        self.setup_light()

        self.cam_status.show()
        self.current_showed_connected_frame = self.cam_status
        self.plc_status.hide()
        self.server_status.hide()
        self.light_status.hide()

        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_get_connected_info.addWidget(self.ip_status, 0, 0, 1, 1)
        self.grid_get_connected_info.addWidget(self.cam_status, 0, 1, 1, 1)
        self.grid_get_connected_info.addWidget(self.plc_status, 0, 1, 1, 1)
        self.grid_get_connected_info.addWidget(self.server_status, 0, 1, 1, 1)
        self.grid_get_connected_info.addWidget(self.light_status, 0, 1, 1, 1)

        self.grid_get_connected_info.setColumnStretch(0, 2)
        self.grid_get_connected_info.setColumnStretch(1, 5)

    def setup_ip_status(self):
        self.ip_status = IpStatus(parent=self)

    def setup_cam_status(self):
        self.cam_status = CameraStatus(parent=self)

    def setup_plc_status(self):
        self.plc_status = PLCStatus(parent=self)

    def setup_server(self):
        self.server_status = ServerStatus(parent=self)
        
    def setup_light(self):
        self.light_status = LightStatus(parent=self)

    def show_connected_frame(self, name):
        if self.current_showed_connected_frame is not None:
            self.current_showed_connected_frame.hide()
        if name == "Camera status":
            self.cam_status.show()
            self.current_showed_connected_frame = self.cam_status
        elif name == "Plc status":
            self.plc_status.show()
            self.current_showed_connected_frame = self.plc_status
        elif name == "Server status":
            self.server_status.show()
            self.current_showed_connected_frame = self.server_status
        elif name == "Light status":
            self.light_status.show()
            self.current_showed_connected_frame = self.light_status

