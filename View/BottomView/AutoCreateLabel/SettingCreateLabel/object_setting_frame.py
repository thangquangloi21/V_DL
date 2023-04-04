from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QCheckBox, QComboBox, QPushButton, QGridLayout
from View.common_view.vision_frame import VisionFrame


class ObjectSettingLabel(VisionFrame):
    icon: QIcon
    check: QCheckBox
    combobox: QComboBox
    setting_btn: QPushButton
    grid_object: QGridLayout

    def __init__(self, parent):
        VisionFrame.__init__(self, parent=parent)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            QPushButton{
                background-color: transparent;
                border-image: None;
            }
            QPushButton:hover{
                background-color: rgb(127, 127, 127);
            }
            QPushButton:pressed{
                background-color: rgb(14, 68, 184);
            }
            QComboBox{
                color: white;
                border: 1px solid gray;
                border-radius: 3px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
            }
            QComboBox:editable {
                 background: gray;
            }
            QCheckbox{
                background: gray;
            }
        """)
        self.setMaximumSize(330, 40)
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap("./Resource/Icon/icon_settings.png"), QIcon.Normal, QIcon.Off)

        self.grid_object = QGridLayout(self)
        self.grid_object.setContentsMargins(0, 0, 0, 0)

    def setup_view(self):
        self.setup_check_box()
        self.setup_combobox()
        self.setup_setting_btn()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_object.addWidget(self.check, 0, 0, 1, 1)
        self.grid_object.addWidget(self.combobox, 0, 1, 1, 1)
        self.grid_object.addWidget(self.setting_btn, 0, 2, 1, 1)
        self.grid_object.setColumnStretch(0, 1)
        self.grid_object.setColumnStretch(1, 1)
        self.grid_object.setColumnStretch(2, 1)

    def setup_check_box(self):
        self.check = QCheckBox(parent=self)
        self.check.setMaximumSize(30, 30)

    def setup_combobox(self):
        self.combobox = QComboBox(parent=self)
        self.combobox.setMaximumSize(250, 30)
        self.combobox.addItem("Rotate")
        self.combobox.addItem("Sighting")
        self.combobox.addItem("Color")

    def setup_setting_btn(self):
        self.setting_btn = QPushButton(parent=self)
        self.setting_btn.setMaximumSize(30, 30)
        self.setting_btn.setIcon(self.icon)