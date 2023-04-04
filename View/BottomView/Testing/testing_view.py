from PyQt5.QtWidgets import QGridLayout
from View.BottomView.Testing.setup_testing.setup_testing import SetUpTesting
from View.BottomView.Testing.result_testing.result_testing import ResultTesting
from View.common_view.vision_frame import VisionFrame
# from View.MainView.main_window import MainWindow


class TestingView(VisionFrame):
    grid_TestingView: QGridLayout
    testing: SetUpTesting = None
    result: ResultTesting = None

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background: transparent;
        """)
        self.grid_TestingView = QGridLayout(self)
        self.grid_TestingView.setContentsMargins(0, 0, 0, 0)

    def setup_view(self):
        self.setup_trainning()
        self.setup_tab_info()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_TestingView.setColumnStretch(0, 2)
        self.grid_TestingView.setColumnStretch(1, 7)
        self.grid_TestingView.addWidget(self.testing, 0, 0, 1, 1)
        self.grid_TestingView.addWidget(self.result, 0, 1, 1, 1)

    def setup_trainning(self):
        self.testing = SetUpTesting(parent=self, main_window=self.main_window)

    def setup_tab_info(self):
        self.result = ResultTesting(parent=self, main_window=self.main_window)