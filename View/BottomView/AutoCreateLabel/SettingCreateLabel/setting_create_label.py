from PyQt5.QtWidgets import QGroupBox, QGridLayout
from View.BottomView.AutoCreateLabel.SettingCreateLabel.object_setting_frame import ObjectSettingLabel
# from View.MainView.main_window import MainWindow
from View.common_view.vision_text_edit import VisionTextEdit
from View.common_view.vision_label import VisionLabel
from View.common_view.vision_group_box import VisionGroupBox


class SettingCreateLabel(QGroupBox):
    label_path: VisionLabel
    edit_text: VisionTextEdit
    object1: ObjectSettingLabel = None
    object2: ObjectSettingLabel = None
    object3: ObjectSettingLabel = None
    object4: ObjectSettingLabel = None
    grid_settingCreateLabel: QGridLayout

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setTitle("Setting")
        self.setStyleSheet("""
            QGroupBox {
                background: rgb(100, 100, 100);
                color: white;
                font: 18px;
                font-weight: bold;
                border-image: None;
                border: 2px solid gray;
                border-radius: 5px;
                margin-top: 1ex; /* leave space at the top for the title */
            }
            QGroupBox::title {
                background: transparent;
                color: white;
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 0px 0px 0px; 
                border-image: None;
            }             
        """)
        self.grid_settingCreateLabel = QGridLayout(self)
        self.grid_settingCreateLabel.setContentsMargins(20, 15, 0, 0)

    def setup_view(self):
        self.setup_path()
        self.setup_setting()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_settingCreateLabel.addWidget(self.label_path, 0, 0, 1, 1)
        self.grid_settingCreateLabel.addWidget(self.edit_text, 0, 1, 1, 1)
        self.grid_settingCreateLabel.addWidget(self.object1, 1, 1, 1, 1)
        self.grid_settingCreateLabel.addWidget(self.object2, 2, 1, 1, 1)
        self.grid_settingCreateLabel.addWidget(self.object3, 3, 1, 1, 1)
        self.grid_settingCreateLabel.addWidget(self.object4, 4, 1, 1, 1)

        self.grid_settingCreateLabel.setColumnStretch(0, 1)
        self.grid_settingCreateLabel.setColumnStretch(1, 4)
        self.grid_settingCreateLabel.setColumnStretch(2, 1)
        self.grid_settingCreateLabel.setColumnStretch(3, 1)
        self.grid_settingCreateLabel.setColumnStretch(4, 1)

        self.grid_settingCreateLabel.setRowStretch(0, 1)
        self.grid_settingCreateLabel.setRowStretch(1, 1)
        self.grid_settingCreateLabel.setRowStretch(2, 1)
        self.grid_settingCreateLabel.setRowStretch(3, 1)
        self.grid_settingCreateLabel.setRowStretch(4, 1)

    def setup_path(self):
        self.label_path = VisionLabel( text="Source:")
        self.edit_text = VisionTextEdit(parent=self, width=350)

    def setup_setting(self):
        self.object1 = ObjectSettingLabel(parent=self)
        self.object2 = ObjectSettingLabel(parent=self)
        self.object3 = ObjectSettingLabel(parent=self)
        self.object4 = ObjectSettingLabel(parent=self)

