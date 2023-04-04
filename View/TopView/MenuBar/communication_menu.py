from PyQt5.QtWidgets import QMenu
from View.Setting.Commnunication.communication_setting import CommunicationSetting
from View.MainView.main_window import MainWindow

class CommnunicationMenu:
    setting_client: CommunicationSetting = None
    setting_server: CommunicationSetting = None
    setting_serial: CommunicationSetting = None
    commnunication: QMenu

    def __init__(self,main_window):
        self.main_window: MainWindow = main_window
        self.setup_view()
        self.setup_window()

    def setup_window(self):
        return

    def setup_view(self):
        self.commnunication = QMenu()
        self.commnunication.setStyleSheet("""
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
        self.select = self.commnunication.addMenu("Select Type")
        self.client = self.commnunication.addMenu("Via Ethernet Client")
        self.server = self.commnunication.addMenu("Via Ethernet Server")
        self.serial = self.commnunication.addMenu("Via Serial")

        self.setup_select_menu()
        self.setup_server()
        self.setup_client()
        self.setup_serial()

    def setup_select_menu(self):
        self.select.addAction("Via Ethernet Client")
        self.select.addAction("Via Ethernet Server")
        self.select.addAction("Via Serial")

    def setup_client(self):
        self.client.addAction("Setting", lambda: self.click_setting_client(name="Client Setting"))
        self.client.addAction("Connect")
        self.client.addAction("Disconnect")
        self.client.addAction("Send Test")

    def setup_server(self):
        self.server.addAction("Setting", lambda: self.click_setting_server(name="Server Setting"))
        self.server.addAction("Connect")
        self.server.addAction("Disconnect")
        self.server.addAction("Send Test")

    def setup_serial(self):
        self.serial.addAction("Setting", lambda: self.click_setting_serial(name="Serial Setting"))
        self.serial.addAction("Connect")
        self.serial.addAction("Disconnect")
        self.serial.addAction("Send Test")

    def click_setting_client(self, name):
        self.setting_client = CommunicationSetting(name=name)

    def click_setting_server(self, name):
        self.setting_server = CommunicationSetting(name=name)

    def click_setting_serial(self, name):
        self.setting_serial = CommunicationSetting(name=name)
