from PyQt5.QtWidgets import QFrame, QSizePolicy, QGridLayout
from View.BottomView.GetConnected.get_connected import GetConnected
from View.BottomView.Label.label import LabelingView
from View.BottomView.AutoCreateLabel.auto_create_label import AutoCreateLable
from View.BottomView.Tranning.trainning_view import TrainningView
from View.BottomView.Testing.testing_view import TestingView
from View.BottomView.Algorithm.algorithm import Algorithm
from View.BottomView.Running.running import Running
from View.MainView.main_window import MainWindow
from View.common_view.vision_frame import VisionFrame


class BottomView(VisionFrame):
    current_showed_frame = None
    get_connected: GetConnected = None
    laybeling: LabelingView = None
    create_label: AutoCreateLable = None
    trainning: TrainningView = None
    testing: TestingView = None
    algorithm: Algorithm = None
    running: Running = None
    sizePolicy: QSizePolicy
    grid_bottom: QGridLayout

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
        QFrame{
               background: transparent;
        /*border-image: url(./Resource/Icon/Rectangle 9.png);*/
        }

        """)
        self.grid_bottom = QGridLayout(self)
        self.grid_bottom.setContentsMargins(2, 2, 2, 2)
        return

    def setup_view(self):

        # show Bottom
        self.setup_get_connected()
        self.setup_lable()
        self.setup_create_lable()
        self.setup_trainning()
        self.setup_testing()
        self.setup_algorithm()
        self.setup_running()

        self.get_connected.show()
        self.current_showed_frame = self.get_connected
        self.laybeling.hide()
        self.create_label.hide()
        self.trainning.hide()
        self.testing.hide()
        self.algorithm.hide()
        self.running.hide()

    def setup_get_connected(self):
        self.get_connected = GetConnected(parent=self, main_window=self.main_window)
        self.grid_bottom.addWidget(self.get_connected, 0, 0, 1, 1)

    def setup_lable(self):
        self.laybeling = LabelingView(parent=self, main_window=self.main_window)
        self.grid_bottom.addWidget(self.laybeling, 0, 0, 1, 1)

    def setup_create_lable(self):
        self.create_label = AutoCreateLable(parent=self, main_window=self.main_window)
        self.grid_bottom.addWidget(self.create_label, 0, 0, 1, 1)

    def setup_trainning(self):
        self.trainning = TrainningView(parent=self, main_window=self.main_window)
        self.grid_bottom.addWidget(self.trainning, 0, 0, 1, 1)

    def setup_testing(self):
        self.testing = TestingView(parent=self, main_window=self.main_window)
        self.grid_bottom.addWidget(self.testing, 0, 0, 1, 1)

    def setup_algorithm(self):
        self.algorithm = Algorithm(parent=self, main_window=self.main_window)
        self.grid_bottom.addWidget(self.algorithm, 0, 0, 1, 1)

    def setup_running(self):
        self.running = Running(parent=self, main_window=self.main_window)
        self.grid_bottom.addWidget(self.running, 0, 0, 1, 1)

    def show_frame(self, name):
        if self.current_showed_frame is not None:
            self.current_showed_frame.hide()
        if name == "Get Connected":
            self.get_connected.show()
            self.current_showed_frame = self.get_connected
        elif name == "Labeling":
            self.laybeling.show()
            self.current_showed_frame = self.laybeling
        elif name == "Auto Create Label":
            self.create_label.show()
            self.current_showed_frame = self.create_label
        elif name == "Trainning":
            self.trainning.show()
            self.current_showed_frame = self.trainning
        elif name == "Testing":
            self.testing.show()
            self.current_showed_frame = self.testing
        elif name == "Algorithm":
            self.algorithm.show()
            self.current_showed_frame = self.algorithm
        elif name == "Running":
            self.running.show()
            self.current_showed_frame = self.running
