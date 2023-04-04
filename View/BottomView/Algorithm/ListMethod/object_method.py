from PyQt5.QtWidgets import QComboBox, QWidget, QGridLayout, QSizePolicy
from View.common_view.vision_frame import VisionFrame
from View.common_view.vision_label import VisionLabel
from View.common_view.vision_check_box import VisionCheckBox
from View.common_view.vision_push_button import VisionPushButton
from View.common_view.vision_combobox import VisionCombobox
# from View.MainView.main_window import MainWindow


class ListObjectMethod(QWidget):
    grid: QGridLayout
    sizePolicy: QSizePolicy

    def __init__(self, parent, main_window):
        QWidget.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.resize(600, 1000)
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)
        self.grid = QGridLayout(self)

    def setup_view(self):
        self.obj0 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj0.lbl_step.setText("0")

        self.obj1 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj1.lbl_step.setText("1")

        self.obj2 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj2.lbl_step.setText("2")

        self.obj3 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj3.lbl_step.setText("3")

        self.obj4 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj4.lbl_step.setText("4")

        self.obj5 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj5.lbl_step.setText("5")

        self.obj6 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj6.lbl_step.setText("6")

        self.obj7 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj7.lbl_step.setText("7")

        self.obj8 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj8.lbl_step.setText("8")

        self.obj9 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj9.lbl_step.setText("9")

        self.obj10 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj10.lbl_step.setText("10")

        self.obj11 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj11.lbl_step.setText("11")

        self.obj12 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj12.lbl_step.setText("12")

        self.obj13 = ObjectMethod(parent=self, main_window=self.main_window)
        self.obj13.lbl_step.setText("13")

        self.grid.addWidget(self.obj0, 0, 0, 1, 1)
        self.grid.addWidget(self.obj1, 1, 0, 1, 1)
        self.grid.addWidget(self.obj2, 2, 0, 1, 1)
        self.grid.addWidget(self.obj3, 3, 0, 1, 1)
        self.grid.addWidget(self.obj4, 4, 0, 1, 1)
        self.grid.addWidget(self.obj5, 5, 0, 1, 1)
        self.grid.addWidget(self.obj6, 6, 0, 1, 1)
        self.grid.addWidget(self.obj7, 7, 0, 1, 1)
        self.grid.addWidget(self.obj8, 8, 0, 1, 1)
        self.grid.addWidget(self.obj9, 9, 0, 1, 1)
        self.grid.addWidget(self.obj10, 10, 0, 1, 1)
        self.grid.addWidget(self.obj11, 11, 0, 1, 1)
        self.grid.addWidget(self.obj12, 12, 0, 1, 1)
        self.grid.addWidget(self.obj13, 13, 0, 1, 1)


class ObjectMethod(VisionFrame):
    check: VisionCheckBox
    lbl_step: VisionLabel
    combobox_method: VisionCombobox
    btn_option: VisionPushButton
    btn_execute: VisionPushButton
    grid_ObjectMethod: QGridLayout

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()
        self.method_List()

    def setup_window(self):
        self.setStyleSheet("""
            QLabel{
                color:white;
                font:16px;
            }   
        """)
        self.grid_ObjectMethod = QGridLayout(self)
        self.grid_ObjectMethod.setHorizontalSpacing(0)

    def setup_view(self):
        self.check = VisionCheckBox(parent=self, width=40, height=30)

        self.lbl_step = VisionLabel( text="0", width=40)

        self.combobox_method = VisionCombobox(parent=self)

        self.btn_option = VisionPushButton(parent=self, text="Option")
        self.btn_option.setStyleSheet("""
            QPushButton:hover{
                color: white;
                font-weight: bold;
                font: 16px;                                
            }
        """)

        self.btn_execute = VisionPushButton(parent=self, text="Execute")

        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_ObjectMethod.addWidget(self.check, 0, 0, 1, 1)
        self.grid_ObjectMethod.addWidget(self.lbl_step, 0, 1, 1, 1)
        self.grid_ObjectMethod.addWidget(self.combobox_method, 0, 2, 1, 1)
        self.grid_ObjectMethod.addWidget(self.btn_option, 0, 3, 1, 1)
        self.grid_ObjectMethod.addWidget(self.btn_execute, 0, 4, 1, 1)

        self.grid_ObjectMethod.setColumnStretch(0, 1)
        self.grid_ObjectMethod.setColumnStretch(1, 1)
        self.grid_ObjectMethod.setColumnStretch(2, 3)
        self.grid_ObjectMethod.setColumnStretch(3, 1)
        self.grid_ObjectMethod.setColumnStretch(4, 1)
        self.grid_ObjectMethod.setColumnStretch(5, 1)

    def method_List(self):
        self.combobox_method.addItems(
            ["Algorithm", "Algorithm", "Algorithm", "Algorithm", "Algorithm", "Algorithm", "Algorithm", "Algorithm",
             "Algorithm", "Algorithm"])
