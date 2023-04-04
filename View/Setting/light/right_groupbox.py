from PyQt5.QtWidgets import QLabel, QGroupBox, QComboBox
from View.MainView.main_window import MainWindow
import serial.tools.list_ports

SPACERW = 10
SPACERH = 20


class RightGroupbox(QGroupBox):
    comNames = []
    baudRates = ['110', '300', '600', '1200', '2400', '4800', '9600', '14400', '19200', '38400', '57600', '115200',
                 '128000', '256000']
    dataSizes = []
    parities = []
    stopBits = []

    partiesMap = {"NONE": serial.PARITY_NONE,
                  "EVEN": serial.PARITY_EVEN,
                  "ODD": serial.PARITY_ODD,
                  "MARK": serial.PARITY_MARK,
                  "SPACE": serial.PARITY_SPACE}

    stopBitMap = {"1": serial.STOPBITS_ONE,
                  "1.5": serial.STOPBITS_ONE_POINT_FIVE,
                  "2": serial.STOPBITS_TWO}

    dataSizemMap = {"5": serial.FIVEBITS,
                    "6": serial.SIXBITS,
                    "7": serial.SEVENBITS,
                    "8": serial.EIGHTBITS}

    activePorts = serial.tools.list_ports.comports()
    comshows = []

    com_port_combobox: QComboBox = None
    baud_rate_combobox: QComboBox = None
    data_size_combobox: QComboBox = None
    parity_combobox: QComboBox = None
    stop_bit_combobox: QComboBox = None

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.initVariables()
        self.setup_window()
        self.setup_view()

    def initVariables(self):
        self.parities = list(self.partiesMap.keys())
        self.stopBits = list(self.stopBitMap.keys())
        self.dataSizes = list(self.dataSizemMap.keys())

        self.activePorts = serial.tools.list_ports.comports()
        self.comNames = []
        self.comshows = []
        for port in self.activePorts:
            if port[2] != 'n/a':
                self.comshows.append("{} ({})".format(port.device, port.description))
                self.comNames.append("{}".format(port.device))

    def setup_window(self):
        self.setTitle("Serial Parameter")
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
        self.resize(250, 400)
        return

    def setup_view(self):
        self.setup_com_port()
        self.setup_baud_rate()
        self.setup_data_size()
        self.setup_parity()
        self.setup_stop_bit()

    def setup_com_port(self):
        lbl_com_port = QLabel(parent=self, text="COM Port")
        lbl_com_port.resize(120, 30)
        lbl_com_port.move(SPACERW, 1.5 * SPACERH)

        self.com_port_combobox = QComboBox(parent=self)
        self.com_port_combobox.addItems(self.comshows)
        self.com_port_combobox.resize(280, 30)
        self.com_port_combobox.move(SPACERW, 3 * SPACERH)
        return

    def setup_baud_rate(self):
        lbl_baud_rate = QLabel(parent=self, text="Baud rate")
        lbl_baud_rate.resize(120, 30)
        lbl_baud_rate.move(SPACERW, 4.5 * SPACERH)

        self.baud_rate_combobox = QComboBox(parent=self)
        self.baud_rate_combobox.addItems(self.baudRates)
        self.baud_rate_combobox.resize(280, 30)
        self.baud_rate_combobox.move(SPACERW, 6 * SPACERH)
        return

    def setup_data_size(self):
        lbl_data_size = QLabel(parent=self, text="Data size")
        lbl_data_size.resize(120, 30)
        lbl_data_size.move(SPACERW, 7.5 * SPACERH)

        self.data_size_combobox = QComboBox(parent=self)
        self.data_size_combobox.addItems(self.dataSizes)
        self.data_size_combobox.resize(280, 30)
        self.data_size_combobox.move(SPACERW, 9 * SPACERH)
        return

    def setup_parity(self):
        lbl_parity = QLabel(parent=self, text="Parity")
        lbl_parity.resize(120, 30)
        lbl_parity.move(SPACERW, 10.5 * SPACERH)

        self.parity_combobox = QComboBox(parent=self)
        self.parity_combobox.addItems(self.parities)
        self.parity_combobox.resize(280, 30)
        self.parity_combobox.move(SPACERW, 12 * SPACERH)
        return

    def setup_stop_bit(self):
        lbl_stop_bit = QLabel(parent=self, text="Stop bit")
        lbl_stop_bit.resize(120, 30)
        lbl_stop_bit.move(SPACERW, 13.5 * SPACERH)

        self.stop_bit_combobox = QComboBox(parent=self)
        self.stop_bit_combobox.addItems(self.stopBits)
        self.stop_bit_combobox.resize(280, 30)
        self.stop_bit_combobox.move(SPACERW, 15 * SPACERH)
        return
