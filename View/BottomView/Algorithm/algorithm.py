from PyQt5.QtWidgets import QGridLayout
from View.BottomView.Algorithm.SettingAlgorithm.setting_algorithm import SettingAlgorithm
from View.BottomView.Algorithm.ListMethod.list_method import ListMethod
# from View.MainView.main_window import MainWindow
from View.common_view.vision_frame import VisionFrame


class Algorithm(VisionFrame):
    setting_algorithm: SettingAlgorithm = None
    list_method: ListMethod = None
    grid_Algorithm: QGridLayout

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background: transparent;
        """)
        self.grid_Algorithm = QGridLayout(self)
        self.grid_Algorithm.setContentsMargins(0, 0, 0, 0)

    def setup_view(self):
        self.setup_algorithm()
        self.setup_list_method()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_Algorithm.addWidget(self.setting_algorithm, 0, 0, 1, 1)
        self.grid_Algorithm.addWidget(self.list_method, 0, 1, 1, 1)
        self.grid_Algorithm.setColumnStretch(0, 2)
        self.grid_Algorithm.setColumnStretch(1, 7)

    def setup_algorithm(self):
        self.setting_algorithm = SettingAlgorithm(parent=self, main_window=self.main_window)

    def setup_list_method(self):
        self.list_method = ListMethod(parent=self, main_window=self.main_window)

