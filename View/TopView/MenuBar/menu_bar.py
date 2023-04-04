from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame, QMenuBar, QSizePolicy
from View.TopView.MenuBar.camera_menu import CameraMenu
from View.TopView.MenuBar.image_menu import ImageMenu
from View.TopView.MenuBar.communication_menu import CommnunicationMenu
from View.TopView.MenuBar.light_menu import LightMenu
from View.TopView.MenuBar.server_menu import ServerMenu
from View.TopView.MenuBar.languages_menu import LanguagesMenu
from View.TopView.MenuBar.zoom_menu import ZoomMenu
from View.MainView.main_window import MainWindow

HEIGHT = 95
Y = 35
SPACE = 10
SIZE = 40


class MenuBar(QFrame):
    menu_bar: QMenuBar = None
    camera_menu: CameraMenu = None
    imageMenu: ImageMenu = None
    communicationMenu: CommnunicationMenu = None
    lightMenu: LightMenu = None
    serverMenu: ServerMenu = None
    languagesMenu: LanguagesMenu = None
    zoomMenu: ZoomMenu = None
    sizePolicy: QSizePolicy

    def __init__(self, parent, main_window, camera_manager):
        QFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.camera_manager = camera_manager
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.resize(1250, int(HEIGHT / 2))
        self.setMaximumSize(600, int(HEIGHT / 2))
        self.display()
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)

    def setup_view(self):
        self.menu_bar = QMenuBar(self)

        self.menu_bar.addAction("Camera", self.setup_camera_menu)
        self.menu_bar.addAction("Image", self.setup_image_menu)
        self.menu_bar.addAction("Communication", self.setup_communication_menu)
        self.menu_bar.addAction("Light", self.setup_light_menu)
        self.menu_bar.addAction("Server", self.setup_server_menu)
        self.menu_bar.addAction("Languages", self.setup_languages_menu)
        self.menu_bar.addAction("Reset Error", self.setup_reset_error_menu)
        self.menu_bar.addAction("Zoom", self.setup_zoom_menu)

    def setup_camera_menu(self):
        self.camera_menu = CameraMenu(main_window=self.main_window, camera_manager=self.camera_manager)
        self.camera_menu.camera.popup(self.mapToGlobal(QPoint(0, Y)))

    def setup_image_menu(self):
        self.imageMenu = ImageMenu(main_window=self.main_window)
        self.imageMenu.image.popup(self.mapToGlobal(QPoint(70, Y)))

    def setup_communication_menu(self):
        self.communicationMenu = CommnunicationMenu(main_window=self.main_window)
        self.communicationMenu.commnunication.popup(self.mapToGlobal(QPoint(125, Y)))

    def setup_light_menu(self):
        self.lightMenu = LightMenu(main_window=self.main_window)
        self.lightMenu.light.popup(self.mapToGlobal(QPoint(245, Y)))

    def setup_server_menu(self):
        self.serverMenu = ServerMenu()
        self.serverMenu.server.popup(self.mapToGlobal(QPoint(295, Y)))

    def setup_languages_menu(self):
        self.languagesMenu = LanguagesMenu()
        self.languagesMenu.languages.popup(self.mapToGlobal(QPoint(350, Y)))

    def setup_reset_error_menu(self):
        return

    def setup_zoom_menu(self):
        self.zoomMenu = ZoomMenu()
        self.zoomMenu.zoom.popup(self.mapToGlobal(QPoint(525, Y)))

    def display(self):
        self.setStyleSheet("""
            QMenuBar {
                color: white;
                padding: 10px 0px 0px 5px;
            }
            QMenuBar::item:selected { 
                background: #a8a8a8;
            }
            QMenuBar::item:pressed {
                background: #888888;
            }
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
