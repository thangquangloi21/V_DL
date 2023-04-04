from PyQt5.QtWidgets import QMainWindow, QLabel, QComboBox, QTextEdit, QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from View.MainView.main_window import MainWindow
from View.common_view.thanh_tieu_de import ThanhTieuDe
from View.Setting.Camera.camera_parameter import CameraFlip
from View.Setting.Camera.camera_parameter import CameraBrand
from View.Setting.Camera.camera_parameter import CameraRotate
from View.Setting.Camera.camera_parameter import CameraParameter
from View.Setting.Camera.camera_parameter import CameraInterface
from View.Setting.Camera.camera_name_list import CameraNameList
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMessageBox
from Connection.Camera import CameraManager
from Connection.Camera import Camera
SPACERW = 20
SPACERH = 22


class CameraForm(QMainWindow):
    thanh_tieu_de: ThanhTieuDe = None

    name_camera: QComboBox
    id_camera: QComboBox
    connection_camera: QComboBox
    brand_camera: QComboBox
    flip_camera: QComboBox
    rotate_camera: QComboBox
    text_size: QTextEdit
    text_thickness: QTextEdit
    btn_ok: QPushButton
    btn_close: QPushButton

    listName = []
    listId = []
    listBrand = []
    listType = []
    listRotate = []
    listFlip = []
    parameterList = []

    def __init__(self, main_window, camera_manager):
        QMainWindow.__init__(self)
        self.startPos = None
        self.main_window: MainWindow = main_window
        self.cameraManger: CameraManager = camera_manager
        self.currentCameraParameter = CameraParameter
        self.camera = Camera(main_window=self.main_window)
        self.init_value()
        self.setup_window()
        self.setup_view()
        self.show()
        self.showCurrentCameraParameter(0)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def init_value(self):

        self.listName = []
        self.listId = []
        self.listBrand = []
        self.listType = []
        self.listRotate = []
        self.listFlip = []
        self.parameterList = []

        for camera in self.cameraManger.cameraList:
            self.parameterList.append(camera.parameter)
        self.currentCameraParameter = self.parameterList[0]

        for idx in range(15):
            self.listId.append(str(idx))

        for name in CameraNameList:
            self.listName.append(name.value)

        for type in CameraInterface:
            self.listType.append(type.value)

        for brand in CameraBrand:
            self.listBrand.append(brand.value)

        for flip in CameraFlip:
            self.listFlip.append(flip.value)

        for rotate in CameraRotate:
            self.listRotate.append(rotate.value)

    def setup_window(self):
        self.setFixedSize(320, 470)
        self.setWindowTitle("Setting Camera")
        # self.setStyleSheet("rgb(207, 216, 220")
        self.setStyleSheet("""
            QMainWindow{
                background: rgb(170, 170, 170);
            }
            QGroupBox {
                color: white;
                font: 18px;
                font-weight: bold;
                background-color:transparent;
                border: 2px solid gray;
                border-radius: 5px;
                margin-top: 1ex; /* leave space at the top for the title */
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 0px 0px 0px;
                border-image: None;
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
            /*QComboBox:editable {
                background: white;
            }*/
            QLabel{
                color: black;
                font: 15px;
            }
            QPushButton{
                background: grey;
                font: 15px;
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: rgb(127, 127, 127);
            }
            QPushButton:pressed{
                background-color: rgb(14, 68, 184);
            }
            QTextEdit{
                 background: white;
                color: black;
            }
        """)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    def setup_view(self):
        self.setup_thanh_tieu_de()
        self.setup_lbl_combobox()
        self.setup_btn()

    def setup_thanh_tieu_de(self):
        self.thanh_tieu_de = ThanhTieuDe(parent=self, width=self.width(), height=35, name_window="Camera Setting")
        self.thanh_tieu_de.resize(self.width(), 35)
        self.thanh_tieu_de.move(0, 0)
        return

    def setup_lbl_combobox(self):
        lbl_name = QLabel(parent=self, text="Name:")
        lbl_name.resize(70, 30)
        lbl_name.move(SPACERW, 2 * SPACERH)
        self.name_camera = QComboBox(parent=self)
        self.name_camera.addItems(self.listName)
        self.name_camera.currentIndexChanged.connect(self.cameraNameSelected)
        self.name_camera.resize(200, 30)
        self.name_camera.move(5 * SPACERW, 2 * SPACERH)

        lbl_id = QLabel(parent=self, text="ID:")
        lbl_id.resize(70, 30)
        lbl_id.move(SPACERW, 4 * SPACERH)
        self.id_camera = QComboBox(parent=self)
        self.id_camera.addItems(self.listId)
        # self.id_camera.currentTextChanged.connect(self.camIdSelected)
        self.id_camera.resize(200, 30)
        self.id_camera.move(5 * SPACERW, 4 * SPACERH)

        lbl_connection = QLabel(parent=self, text="Connection:")
        lbl_connection.resize(70, 30)
        lbl_connection.move(SPACERW, 6 * SPACERH)
        self.connection_camera = QComboBox(parent=self)
        self.connection_camera.addItems(self.listType)
        # self.connection_camera.currentTextChanged.connect(self.typeSelected)
        self.connection_camera.resize(200, 30)
        self.connection_camera.move(5 * SPACERW, 6 * SPACERH)

        lbl_brand = QLabel(parent=self, text="Brand:")
        lbl_brand.resize(70, 30)
        lbl_brand.move(SPACERW, 8 * SPACERH)
        self.brand_camera = QComboBox(parent=self)
        self.brand_camera.addItems(self.listBrand)
        # self.brand_camera.currentTextChanged.connect(self.brandSelected)
        self.brand_camera.resize(200, 30)
        self.brand_camera.move(5 * SPACERW, 8 * SPACERH)

        lbl_flip = QLabel(parent=self, text="Flip:")
        lbl_flip.resize(70, 30)
        lbl_flip.move(SPACERW, 10 * SPACERH)
        self.flip_camera = QComboBox(parent=self)
        self.flip_camera.addItems(self.listFlip)
        # self.flip_camera.currentTextChanged.connect(self.flipSelected)
        self.flip_camera.resize(200, 30)
        self.flip_camera.move(5 * SPACERW, 10 * SPACERH)

        lbl_rotate = QLabel(parent=self, text="Rotate:")
        lbl_rotate.resize(70, 30)
        lbl_rotate.move(SPACERW, 12 * SPACERH)
        self.rotate_camera = QComboBox(parent=self)
        self.rotate_camera.addItems(self.listRotate)
        # self.rotate_camera.currentTextChanged.connect(self.rotateSelected)
        self.rotate_camera.resize(200, 30)
        self.rotate_camera.move(5 * SPACERW, 12 * SPACERH)

        lbl_text_size = QLabel(parent=self, text="Text size:")
        lbl_text_size.resize(70, 30)
        lbl_text_size.move(SPACERW, 14 * SPACERH)
        self.text_size = QTextEdit(parent=self)
        self.text_size.resize(70, 30)
        self.text_size.move(7 * SPACERW, 14 * SPACERH)

        lbl_text_thickness = QLabel(parent=self, text="Text thickness:")
        lbl_text_thickness.resize(70, 30)
        lbl_text_thickness.move(SPACERW, 16.5 * SPACERH)
        self.text_thickness = QTextEdit(parent=self)
        self.text_thickness.resize(70, 30)
        self.text_thickness.move(7 * SPACERW, 16.5 * SPACERH)

    def setup_btn(self):
        self.setup_ok_btn()
        self.setup_close_btn()

    def setup_ok_btn(self):
        self.btn_ok = QPushButton(parent=self, text="OK")
        self.btn_ok.resize(100, 30)
        self.btn_ok.move(2 * SPACERW, 19 * SPACERH)
        self.btn_ok.clicked.connect(self.click_ok_btn)

    def setup_close_btn(self):
        self.btn_close = QPushButton(parent=self, text="Close")
        self.btn_close.resize(100, 30)
        self.btn_close.move(9 * SPACERW, 19 * SPACERH)
        self.btn_close.clicked.connect(self.click_close_btn)

    def click_ok_btn(self):
        try:
            self.saveCameraSelected()
            self.cameraManger.getInfo()
        except Exception as error:
            QMessageBox.about(self, "Title", "ERROR Camera setting : {}".format(error))
            print("ERROR Camera setting : {}".format(error))
            # QMessageBox.Ok(self.mainWindow.languageManager.localized("cameraChangeTitle"), "{}".format(error))
        self.close()

    def click_close_btn(self):
        self.close()

    def showCurrentCameraParameter(self, index=None):
        if index is not None:
            cameraPos = index
        else:
            cameraPos = self.name_camera.currentIndex()

        currentCamera = self.parameterList[cameraPos]
        self.name_camera.setCurrentIndex(index)
        self.name_camera.setCurrentText(str(currentCamera.name))
        self.id_camera.setCurrentText(str(currentCamera.id))
        self.connection_camera.setCurrentText(str(currentCamera.interface))
        self.brand_camera.setCurrentText(str(currentCamera.brand))
        self.flip_camera.setCurrentText(str(currentCamera.flip))
        self.rotate_camera.setCurrentText(str(currentCamera.rotate))
        self.text_size.setPlainText(str(currentCamera.textScale))
        self.text_thickness.setPlainText(str(currentCamera.textThickness))

    def saveCameraSelected(self):
        try:
            self.currentCameraParameter.name = self.name_camera.currentText()
            self.currentCameraParameter.id = self.id_camera.currentText()
            self.currentCameraParameter.interface = self.connection_camera.currentText()
            self.currentCameraParameter.brand = self.brand_camera.currentText()
            self.currentCameraParameter.flip = self.flip_camera.currentText()
            self.currentCameraParameter.rotate = self.rotate_camera.currentText()
            self.currentCameraParameter.textScale = self.text_size.toPlainText()
            self.currentCameraParameter.textThickness = self.text_thickness.toPlainText()
        except Exception as error:
            QMessageBox.about(self, "error", "Detail: {}".format(error))
            print("Detail: {}".format(error))
        self.parameterList[self.name_camera.currentIndex()] = self.currentCameraParameter
        self.cameraManger.save(self.parameterList)

    def cameraNameSelected(self, index):
        self.currentCameraParameter = self.parameterList[self.name_camera.currentIndex()]
        self.showCurrentCameraParameter(index)
        print("ok")

    def camIdSelected(self):
        value = self.id_camera.currentIndex()
        self.currentCameraParameter.id = value
        self.saveCameraSelected()

    def typeSelected(self):
        value = self.connection_camera.currentText()
        self.currentCameraParameter.interface = value
        self.saveCameraSelected()

    def brandSelected(self):
        value = self.brand_camera.currentText()
        self.currentCameraParameter.brand = value
        self.saveCameraSelected()

    def flipSelected(self):
        value = self.flip_camera.currentText()
        self.currentCameraParameter.flip = value
        self.saveCameraSelected()

    def rotateSelected(self):
        value = self.rotate_camera.currentText()
        self.currentCameraParameter.rotate = value
        self.saveCameraSelected()

    # Kéo di Chuyển app
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.startPos = event.pos()

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        # todo reset position
        self.startPos = None
        return

    def mouseMoveEvent(self, event):
        try:
            if self.startPos is None:
                return
            if self.startPos.x() <= self.thanh_tieu_de.width \
                    and self.startPos.y() <= self.thanh_tieu_de.height \
                    and not self.isMaximized():
                self.move(self.pos() + (event.pos() - self.startPos))
        except Exception as error:
            print(error)
