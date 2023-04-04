from PyQt5.QtWidgets import QGridLayout
from View.BottomView.Tranning.SetUpTrainning.trainning import Trainning
from View.BottomView.Tranning.SetUpTab.set_up_tab import SetUpTab
from View.common_view.vision_frame import VisionFrame
# from View.MainView.main_window import MainWindow


class TrainningView(VisionFrame):
    grid_TrainingView: QGridLayout
    trainning: Trainning
    tabW: SetUpTab

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background: transparent;
        """)
        self.grid_TrainingView = QGridLayout(self)
        self.grid_TrainingView.setContentsMargins(0, 0, 0, 0)

    def setup_view(self):
        self.setup_trainning()
        self.setup_tab_info()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_TrainingView.addWidget(self.trainning, 0, 0, 1, 1)
        self.grid_TrainingView.addWidget(self.tabW, 0, 1, 1, 1)
        self.grid_TrainingView.setColumnStretch(0, 2)
        self.grid_TrainingView.setColumnStretch(1, 7)

    def setup_trainning(self):
        self.trainning = Trainning(parent=self, main_window=self.main_window)

    def setup_tab_info(self):
        self.tabW = SetUpTab(parent=self, main_window=self.main_window)
