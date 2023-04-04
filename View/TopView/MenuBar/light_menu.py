from PyQt5.QtWidgets import QMenu
from View.Setting.light.light_setting import LightForm
from View.Setting.light.setting_value_view import SettingValueView
from View.MainView.main_window import MainWindow


class LightMenu:
    light: QMenu
    light_setting_form: LightForm = None
    light_setting_val: SettingValueView = None

    def __init__(self, main_window):
        self.main_window: MainWindow = main_window
        self.setup_view()
        self.setup_window()

    def setup_window(self):
        return

    def setup_view(self):
        self.light = QMenu()
        self.light.setStyleSheet("""
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
        self.light.addAction("Setting", self.setting_light)
        self.light.addAction("Connect")
        self.light.addAction("Disconnect")
        self.light.addAction("Turn On")
        self.light.addAction("Turn Off")
        self.light.addAction("Setting Value", self.setting_value)
        self.light.addAction("Refresh")

    def setting_light(self):
        self.light_setting_form = LightForm(main_window=self.main_window)
        return

    def setting_value(self):
        self.light_setting_val = SettingValueView(main_window=self.main_window)
        return
