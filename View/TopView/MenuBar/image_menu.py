from PyQt5.QtWidgets import QMenu, QFileDialog
from View.MainView.main_window import MainWindow
from PyQt5.QtGui import QPixmap


class ImageMenu:
    image: QMenu

    def __init__(self, main_window):
        self.main_window: MainWindow = main_window
        # self.main_window = main_window
        self.setup_window()
        self.setup_view()
        self.openfile.triggered.connect(self.main_window.top_view.toolBar.setup_open)
        self.save_original_image.triggered.connect(self.main_window.top_view.toolBar.saveOriginalImage)
        self.save_process_image.triggered.connect(self.main_window.top_view.toolBar.saveProcessedImage)
        self.so_thu_tu = 0
        self.list_file = None


    def setup_window(self):
        return

    def setup_view(self):
        self.image = QMenu()
        self.image.setStyleSheet("""
                   QMenu {
                       background-color: #888888;
                   }
                   QMenu::item:selected { 
                       background: #a8a8a8;
                   }
                   QMenu::item {
                       padding: 3px 30px 5px 10px;    
                       border: 1px solid transparent; 
                   }
                   QMenu::item:pressed {
                       background: white;
                       }
               """)
        self.new = self.image.addMenu("New")
        self.openfile = self.image.addAction("Open")
        self.draw = self.image.addMenu("Draw")
        self.save = self.image.addMenu("Save")

        self.setup_new_menu()
        self.setup_draw_menu()
        self.setup_save_menu()

    def setup_new_menu(self):
        self.new.addAction("Black Image")
        self.new.addAction("White Image")

    def setup_draw_menu(self):
        self.draw.addAction("On")
        self.draw.addAction("Draw Cross")
        self.draw.addAction("Draw Rectangle")
        self.draw.addAction("Draw Circle")
        self.draw.addAction("Off")

    def setup_save_menu(self):
       self.save_original_image = self.save.addAction("Save Original Image")
       self.save_process_image = self.save.addAction("Save Process Image")

#




