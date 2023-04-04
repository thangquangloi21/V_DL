from PyQt5.QtWidgets import QGridLayout
# from View.MainView.main_window import MainWindow
from View.common_view.vision_frame import VisionFrame
from View.common_view.vision_label import VisionLabel
from View.common_view.vision_text_edit import VisionTextEdit
from View.common_view.vision_progress_bar import VisionProgressBar


class TabInfo(VisionFrame):
    path_img: VisionTextEdit
    path_weight: VisionTextEdit
    lbl_n: VisionTextEdit
    lbl_t: VisionTextEdit
    process: VisionProgressBar
    path_: VisionLabel
    lbl_weight: VisionLabel
    lbl_number: VisionLabel
    lbl_time: VisionLabel
    lbl_pro: VisionLabel
    grid_tab_info: QGridLayout

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
        self.grid_tab_info = QGridLayout(self)

    def setup_view(self):
        self.img_path()
        self.weight_path()
        self.number_img()
        self.time_train()
        self.processing()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_tab_info.addWidget(self.path_, 0, 0, 1, 1)
        self.grid_tab_info.addWidget(self.path_img, 0, 1, 1, 1)
        self.grid_tab_info.addWidget(self.lbl_weight, 1, 0, 1, 1)
        self.grid_tab_info.addWidget(self.path_weight, 1, 1, 1, 1)
        self.grid_tab_info.addWidget(self.lbl_number, 0, 2, 1, 1)
        self.grid_tab_info.addWidget(self.lbl_n, 0, 3, 1, 1)
        self.grid_tab_info.addWidget(self.lbl_time, 1, 2, 1, 1)
        self.grid_tab_info.addWidget(self.lbl_t, 1, 3, 1, 1)
        self.grid_tab_info.addWidget(self.lbl_pro, 2, 0, 1, 1)
        self.grid_tab_info.addWidget(self.process, 2, 1, 1, 2)

        self.grid_tab_info.setVerticalSpacing(20)
        self.grid_tab_info.setRowStretch(0, 1)
        self.grid_tab_info.setRowStretch(1, 1)
        self.grid_tab_info.setRowStretch(2, 1)
        self.grid_tab_info.setColumnStretch(0, 1)
        self.grid_tab_info.setColumnStretch(1, 1)
        self.grid_tab_info.setColumnStretch(2, 1)
        self.grid_tab_info.setColumnStretch(3, 1)
        self.grid_tab_info.setColumnStretch(4, 2)

    def img_path(self):
        self.path_ = VisionLabel( text="Folder Image:")
        self.path_img = VisionTextEdit(parent=self)

    def weight_path(self):
        self.lbl_weight = VisionLabel( text="Weight Path:")
        self.path_weight = VisionTextEdit(parent=self)

    def number_img(self):
        self.lbl_number = VisionLabel( text="Number Of Image:")
        self.lbl_n = VisionTextEdit(parent=self)

    def time_train(self):
        self.lbl_time = VisionLabel(text="Time Trainning:")
        self.lbl_t = VisionTextEdit(parent=self)

    def processing(self):
        self.lbl_pro = VisionLabel( text="Processing:")
        self.process = VisionProgressBar(parent=self, value=24)

