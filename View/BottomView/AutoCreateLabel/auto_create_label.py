from PyQt5.QtWidgets import QGridLayout
from View.BottomView.AutoCreateLabel.CreateLabel.createLabel import CreateLabel
from View.BottomView.AutoCreateLabel.SettingCreateLabel.setting_create_label import SettingCreateLabel
from View.common_view.vision_frame import VisionFrame
# from View.MainView.main_window import MainWindow


class AutoCreateLable(VisionFrame):
    create_label: CreateLabel = None
    setting: SettingCreateLabel = None
    grid_autoCreateLabel: QGridLayout

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window : MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background: transparent;
            border-image: None;
        """)
        self.grid_autoCreateLabel = QGridLayout(self)
        self.grid_autoCreateLabel.setContentsMargins(0, 0, 0, 0)

    def setup_view(self):
        self.setup_create_label()
        self.setup_setting()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_autoCreateLabel.addWidget(self.create_label, 0, 0, 1, 1)
        self.grid_autoCreateLabel.addWidget(self.setting, 0, 1, 1, 1)
        self.grid_autoCreateLabel.setColumnStretch(0, 2)
        self.grid_autoCreateLabel.setColumnStretch(1, 7)

    def setup_create_label(self):
        self.create_label = CreateLabel(parent=self, main_window=self.main_window)

    def setup_setting(self):
        self.setting = SettingCreateLabel(parent=self, main_window=self.main_window)
