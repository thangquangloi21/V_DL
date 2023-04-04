from CommonAssit import *
from View import *
from PyQt5.QtWidgets import QApplication
import sys


def main():
    # Khai báo màn hình main window ở đây
    print("Start")
    # sys.setrecursionlimit(2000)
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    print("Welcome to Mes Vision Deep Learning Application!")
    main()
