from PyQt5.QtWidgets import QGridLayout
# from View.MainView.main_window import MainWindow
from View.common_view.vision_frame import VisionFrame
from View.common_view.vision_label import VisionLabel
from View.common_view.vision_text_edit import VisionTextEdit
from View.common_view.vision_progress_bar import VisionProgressBar


class ResultTesting(VisionFrame):
    grid_result_testing: QGridLayout
    path_: VisionLabel
    path_img: VisionTextEdit
    lbl_weight: VisionLabel
    path_weight: VisionTextEdit
    lbl_number: VisionLabel
    lbl_n: VisionTextEdit
    lbl_time: VisionLabel
    lbl_t: VisionTextEdit
    lbl_rate: VisionLabel
    text_rate: VisionTextEdit
    lbl_pro: VisionLabel
    process: VisionProgressBar

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            QFrame{
                border: None;
                background: rgb(100, 100, 100);
                color: white;
            }
            QTextEdit{
                background-color: rgb(160, 160, 160);
                border-image: None;
                font: 14px;
                color: black;
            }
            QProgressBar{
                border: 2px solid rgb(160, 160, 160);   
                border-radius: 5px;
            }
        """)
        self.grid_result_testing = QGridLayout(self)

    def setup_view(self):
        self.img_path()
        self.weight_path()
        self.number_img()
        self.time_test()
        self.correct_rate()
        self.processing()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_result_testing.addWidget(self.path_, 0, 0, 1, 1)
        self.grid_result_testing.addWidget(self.path_img, 0, 1, 1, 1)
        self.grid_result_testing.addWidget(self.lbl_weight, 1, 0, 1, 1)
        self.grid_result_testing.addWidget(self.path_weight, 1, 1, 1, 1)
        self.grid_result_testing.addWidget(self.lbl_number, 0, 2, 1, 1)
        self.grid_result_testing.addWidget(self.lbl_n, 0, 3, 1, 1)
        self.grid_result_testing.addWidget(self.lbl_time, 1, 2, 1, 1)
        self.grid_result_testing.addWidget(self.lbl_t, 1, 3, 1, 1)
        self.grid_result_testing.addWidget(self.lbl_rate, 2, 0, 1, 1)
        self.grid_result_testing.addWidget(self.text_rate, 2, 1, 1, 1)
        self.grid_result_testing.addWidget(self.lbl_pro, 3, 0, 1, 1)
        self.grid_result_testing.addWidget(self.process, 3, 1, 1, 2)

        self.grid_result_testing.setVerticalSpacing(20)
        self.grid_result_testing.setRowStretch(0, 1)
        self.grid_result_testing.setRowStretch(1, 1)
        self.grid_result_testing.setRowStretch(2, 1)
        self.grid_result_testing.setRowStretch(3, 1)
        self.grid_result_testing.setColumnStretch(0, 1)
        self.grid_result_testing.setColumnStretch(1, 1)
        self.grid_result_testing.setColumnStretch(2, 1)
        self.grid_result_testing.setColumnStretch(3, 1)
        self.grid_result_testing.setColumnStretch(4, 2)

    def img_path(self):
        self.path_ = VisionLabel( text="Source Image:")
        self.path_img = VisionTextEdit(parent=self)

    def weight_path(self):
        self.lbl_weight = VisionLabel(text="Weight Path:")
        self.path_weight = VisionTextEdit(parent=self)

    def number_img(self):
        self.lbl_number = VisionLabel( text="Number Of Image:")
        self.lbl_n = VisionTextEdit(parent=self)

    def time_test(self):
        self.lbl_time = VisionLabel( text="Time Testing:")
        self.lbl_t = VisionTextEdit(parent=self)

    def correct_rate(self):
        self.lbl_rate = VisionLabel(text="Correct Rate:")
        self.text_rate = VisionTextEdit(parent=self, width=50)

    def processing(self):
        self.lbl_pro = VisionLabel( text="Testing:")
        self.process = VisionProgressBar(parent=self, value=24)

