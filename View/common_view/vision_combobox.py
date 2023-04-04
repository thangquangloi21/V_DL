from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import QSize


class VisionCombobox(QComboBox):
    def __init__(self, parent):
        QComboBox.__init__(self, parent=parent)
        self.setup_view()

    def setup_view(self):
        self.setStyleSheet("""
            QComboBox{
                color: white;
                border: 1px solid gray;
                border-radius: 3px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
                background: grey;
            }
            QComboBox QAbstractItemView {
                border: 2px solid darkgray;
                background: rgb(200, 200, 200);
                selection-background-color: blue;
            }
        """)
