from PyQt5.QtWidgets import QTabWidget, QGridLayout
from View.BottomView.Tranning.SetUpTab.tab_info import TabInfo
from View.BottomView.Tranning.SetUpTab.tab_processing import TabProcess
# from View.MainView.main_window import MainWindow


class SetUpTab(QTabWidget):
    grid_setUpTab: QGridLayout

    def __init__(self, parent, main_window):
        QTabWidget.__init__(self, parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            QTabBar::tab {
                background: transparent;
                color: white;
            }
            QTabBar::tab:selected, QTabBar::tab:hover {
                background: transparent;
            }
            QTabBar::tab:selected {
                background:gray;
            }
        """)

    def setup_view(self):
        self.set_up_tab()

    def set_up_tab(self):
        self.addTab(TabInfo(parent=self, main_window=self.main_window), "Info")
        self.addTab(TabProcess(parent=self, main_window=self.main_window), "Process")
