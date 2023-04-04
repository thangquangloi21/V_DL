from PyQt5.QtWidgets import QMenu


class LanguagesMenu:
    languages: QMenu

    def __init__(self):

        self.setup_view()
        self.setup_window()

    def setup_window(self):
        return

    def setup_view(self):
        self.languages = QMenu()
        self.languages.setStyleSheet("""
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
        self.languages.addAction("English")
        self.languages.addAction("Tiếng Việt")

    def event_click(self):
        return
