from PyQt5.QtWidgets import QGridLayout
from View.BottomView.Label.Labeling.laybeling import Labeling
from View.BottomView.Label.SettingLabel.seting_label import SettingLabel
# from View.MainView.main_window import MainWindow
from View.common_view.vision_frame import VisionFrame


class LabelingView(VisionFrame):
    laybeling: Labeling = None
    setting_label: SettingLabel = None
    grid_label: QGridLayout

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background:transparent;
            border-image:None;
            font: 14px;
        """)
        self.grid_label = QGridLayout(self)
        self.grid_label.setContentsMargins(0, 0, 0, 0)

    def setup_view(self):
        self.setup_setting()
        self.setup_infomation()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_label.addWidget(self.laybeling, 0, 0, 1, 1)
        self.grid_label.addWidget(self.setting_label, 0, 1, 1, 1)

        self.grid_label.setColumnStretch(0, 2)
        self.grid_label.setColumnStretch(1, 7)

    def setup_setting(self):         # left side
        self.laybeling = Labeling(parent=self, main_window=self.main_window)

    def setup_infomation(self):
        self.setting_label = SettingLabel(parent=self, main_window=self.main_window,)


