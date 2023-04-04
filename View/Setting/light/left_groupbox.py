from PyQt5.QtWidgets import QLabel, QGroupBox, QComboBox
import enum
from View.MainView.main_window import MainWindow

SPACERW = 10
SPACERH = 20


class LightBrand(enum.Enum):
    L_light = "L-Light"
    csr_light = "CSR-Light"
    vst_light = "VST-Light"


class LightChanel(enum.Enum):
    _1Chanel = "1 chanel"
    _2Channel = "2 channels"
    _3Channel = "3 channels"
    _4Channel = "4 channels"
    _6Channel = "6 channels"
    _8Channel = "8 channels"
    _16Channel = "16 channels"


class LeftGroupbox(QGroupBox):
    brand_combobox: QComboBox = None
    channel_combobox: QComboBox = None

    list_brand = []
    list_chanel = []

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.initValue()
        self.setup_window()
        self.setup_view()

    def initValue(self):
        self.list_brand = []
        self.list_chanel = []
        for brand in LightBrand:
            self.list_brand.append(brand.value)
        for chanel in LightChanel:
            self.list_chanel.append(chanel.value)

    def setup_window(self):
        self.setTitle("Connection Parameter")
        self.setStyleSheet("""
            QLabel{
                color: black;
                font: 14px;
            }
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
                selection-background-color: rgb(170, 170, 170);
            }
        """)
        self.resize(220, 400)
        return

    def setup_view(self):
        self.setup_brand()
        self.setup_channel()
        return

    def setup_brand(self):
        lbl_brand = QLabel(parent=self, text="Brand")
        lbl_brand.resize(70, 30)
        lbl_brand.move(SPACERW, 2 * SPACERH)

        self.brand_combobox = QComboBox(parent=self)
        self.brand_combobox.addItems(self.list_brand)
        self.brand_combobox.resize(200, 30)
        self.brand_combobox.move(SPACERW, 4 * SPACERH)

    def setup_channel(self):
        lbl_channel = QLabel(parent=self, text="Channel Amount")
        lbl_channel.resize(120, 30)
        lbl_channel.move(SPACERW, 6 * SPACERH)

        self.channel_combobox = QComboBox(parent=self)
        self.channel_combobox.addItems(self.list_chanel)
        self.channel_combobox.resize(200, 30)
        self.channel_combobox.move(SPACERW, 8 * SPACERH)
