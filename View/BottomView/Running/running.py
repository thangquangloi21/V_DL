from PyQt5.QtWidgets import QGridLayout
from View.BottomView.Running.RunningInfo.running_info import RunningInfo
from View.BottomView.Running.RunningResult.running_result import RunningResult
from View.common_view.vision_frame import VisionFrame
# from View.MainView.main_window import MainWindow


class Running(VisionFrame):
    grid_Running: QGridLayout
    running_info: RunningInfo = None
    running_result: RunningResult = None

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        # self.resize(1300, 280)
        # self.setMinimumSize(1000, 300)

        self.setStyleSheet("""
            background:transparent;
            border-image:None;
        """)
        self.grid_Running = QGridLayout(self)
        self.grid_Running.setContentsMargins(0, 0, 0, 0)

    def setup_view(self):
        self.setup_running_info()
        self.setup_running_result()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_Running.setColumnStretch(0, 2)
        self.grid_Running.setColumnStretch(1, 7)
        self.grid_Running.addWidget(self.running_info, 0, 0, 1, 1)
        self.grid_Running.addWidget(self.running_result, 0, 1, 1, 1)

    def setup_running_info(self):
        self.running_info = RunningInfo(parent=self, main_window=self.main_window)

    def setup_running_result(self):
        self.running_result = RunningResult(parent=self, main_window=self.main_window)
