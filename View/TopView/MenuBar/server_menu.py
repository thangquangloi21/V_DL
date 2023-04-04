from PyQt5.QtWidgets import QPushButton, QMenu, QFrame, QMenuBar
from View.Setting.Commnunication.communication_setting import CommunicationSetting


class ServerMenu:
    server: QMenu
    setting_server: CommunicationSetting = None

    def __init__(self):
        self.setup_view()
        self.setup_window()

    def setup_window(self):
        return

    def setup_view(self):
        self.server = QMenu()
        self.server.setStyleSheet("""
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
        self.server.addAction("Setting", lambda: self.click_setting_server(name="Server Setting"))
        self.server.addAction("Connect")
        self.server.addAction("Disconnect")
        self.server.addAction("Send Test")

    def click_setting_server(self, name):
        self.setting_server = CommunicationSetting(name=name)
