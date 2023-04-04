from PyQt5.QtWidgets import QTabWidget, QSizePolicy
from PyQt5.QtCore import QSize
from View.RightView.ResultTab.result_tab import ResultTab
from View.RightView.LogTab.log_tab import LogTab
from View.MainView.main_window import MainWindow


class RightView(QTabWidget):
    sizePolicy: QSizePolicy = None

    def __init__(self, parent, main_window):
        QTabWidget.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background: rgb(170, 170, 170);    
            border-image: url(./Resource/Icon/Rectangle 5.png);
            /*
            QTabWidget::pane {
                border: 1px solid lightgray;
                top:-1px; 
                background: rgb(245, 245, 245);; 
            } 
            QTabBar::tab {
                background: rgb(230, 230, 230); 
                border: 1px solid lightgray; 
                padding: 15px;
            } 
            QTabBar::tab:selected { 
                background: red;
                margin-bottom: -1px; 
            
            }*/
        """)
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)
        self.setMaximumSize(QSize(420, 16777215))

    def setup_view(self):
        self.addTab(ResultTab(parent=self), "Result")
        self.addTab(LogTab(parent=self), "Log")
