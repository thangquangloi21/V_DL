from PyQt5.QtWidgets import QGridLayout
from View.BottomView.GetConnected.GetConnectedInfo.get_connected_info import GetConnectedInfo

# from View.MainView.main_window import MainWindow
from View.common_view.vision_frame import VisionFrame


class GetConnected(VisionFrame):
    get_connected_info: GetConnectedInfo
    grid_GetConnected: QGridLayout
    get_connected_setting = None
    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background:transparent;
            border-image:None;
        """)
        self.grid_GetConnected = QGridLayout(self)
        self.grid_GetConnected.setContentsMargins(0, 0, 0, 0)

    def setup_view(self):
        self.setup_setting()
        self.setup_infomation()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_GetConnected.addWidget(self.get_connected_setting, 0, 0, 1, 1)
        self.grid_GetConnected.addWidget(self.get_connected_info, 0, 1, 1, 1)

        self.grid_GetConnected.setColumnStretch(0, 2)
        self.grid_GetConnected.setColumnStretch(1, 7)

    def setup_setting(self):
        from View.BottomView.GetConnected.GetConnectedSetting.get_connected_setting import GetConnectedSetting
        self.get_connected_setting = GetConnectedSetting(parent=self, main_window=self.main_window)

    def setup_infomation(self):
        self.get_connected_info = GetConnectedInfo(parent=self, main_window=self.main_window)

