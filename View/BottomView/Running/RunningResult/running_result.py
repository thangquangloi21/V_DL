from PyQt5.QtWidgets import QGroupBox, QGridLayout
# from View.MainView.main_window import MainWindow
from View.common_view.vision_label import VisionLabel


class RunningResult(QGroupBox):
    grid_running_result: QGridLayout
    lbl_stt: VisionLabel

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setTitle("Result")
        self.setStyleSheet("""
            QGroupBox {
                background: rgb(100, 100, 100);
                color: white;
                font: 18px;
                font-weight: bold;
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
        """)
        self.grid_running_result = QGridLayout(self)

    def setup_view(self):
        self.setup_label()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_running_result.addWidget(self.lbl_stt)

    def setup_label(self):
        self.lbl_stt = VisionLabel( text="RESULT")
