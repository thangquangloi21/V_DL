from PyQt5.QtWidgets import QMenu


class VisionMenu(QMenu):
    def __init__(self, parent):
        QMenu.__init__(self, parent=parent)
        self.setup_view()

    def setup_view(self):
        return
