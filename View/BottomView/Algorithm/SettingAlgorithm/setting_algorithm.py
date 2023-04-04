from PyQt5.QtWidgets import QGroupBox, QComboBox, QGridLayout, QSizePolicy
from PyQt5.QtCore import QSize
# from View.MainView.main_window import MainWindow
from View.common_view.vision_text_edit import VisionTextEdit
from View.common_view.vision_label import VisionLabel
from View.common_view.vision_push_button import VisionPushButton
SPACERX = 10
SPACERY = 50


class SettingAlgorithm(QGroupBox):
    lable_name: VisionLabel
    combobox_algorithm: QComboBox
    rename: VisionLabel
    name_edit: VisionTextEdit
    btnAdd: VisionPushButton
    btnDuplicate: VisionPushButton
    btnDel: VisionPushButton
    btnSave: VisionPushButton
    sizePolicy: QSizePolicy
    grid_setting_algorithm: QGridLayout

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setTitle("Algorithm")
        self.setStyleSheet("""
            QGroupBox {
                background: transparent;
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
        """)
        self.setMaximumSize(QSize(300, 16777215))
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)
        self.grid_setting_algorithm = QGridLayout(self)
        self.grid_setting_algorithm.setContentsMargins(20, 30, 10, 10)
        self.grid_setting_algorithm.setVerticalSpacing(20)

    def setup_view(self):
        self.setup_name_algorithm()
        self.setup_btn()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_setting_algorithm.addWidget(self.lable_name, 0, 0, 1, 1)
        self.grid_setting_algorithm.addWidget(self.combobox_algorithm, 0, 1, 1, 1)
        self.grid_setting_algorithm.addWidget(self.rename, 1, 0, 1, 1)
        self.grid_setting_algorithm.addWidget(self.name_edit, 1, 1, 1, 1)
        self.grid_setting_algorithm.addWidget(self.btnAdd, 2, 0, 1, 1)
        self.grid_setting_algorithm.addWidget(self.btnDuplicate, 2, 1, 1, 1)
        self.grid_setting_algorithm.addWidget(self.btnDel, 3, 0, 1, 1)
        self.grid_setting_algorithm.addWidget(self.btnSave, 3, 1, 1, 1)

        self.grid_setting_algorithm.setRowStretch(0, 1)
        self.grid_setting_algorithm.setRowStretch(1, 1)
        self.grid_setting_algorithm.setRowStretch(2, 1)
        self.grid_setting_algorithm.setRowStretch(3, 1)
        self.grid_setting_algorithm.setRowStretch(4, 1)
        self.grid_setting_algorithm.setColumnStretch(0, 1)
        self.grid_setting_algorithm.setColumnStretch(1, 1)

    def setup_name_algorithm(self):
        self.lable_name = VisionLabel( text="Algorithm:")
        self.combobox_algorithm = QComboBox(parent=self)
        self.combobox_algorithm.addItem("algorithm")
        self.rename = VisionLabel(text="Rename:")
        self.name_edit = VisionTextEdit(parent=self)

    def setup_btn(self):
        self.btn_add()
        self.btn_duplicate()
        self.btn_delete()
        self.btn_save()

    def btn_add(self):
        self.btnAdd = VisionPushButton(parent=self, text="Add")

    def btn_duplicate(self):
        self.btnDuplicate = VisionPushButton(parent=self, text="Duplicate")

    def btn_delete(self):
        self.btnDel = VisionPushButton(parent=self, text="Delete")

    def btn_save(self):
        self.btnSave = VisionPushButton(parent=self, text="Save")
