from PyQt5.QtWidgets import QMenu
from View.Setting.Camera.camera_setting import CameraForm
from View.MainView.main_window import MainWindow
from WorkingThread import WorkingThread
from Connection.Camera import CameraManager

class CameraMenu:
    setting_cam: CameraForm = None
    camera: QMenu
    workingThread: WorkingThread
    def __init__(self, main_window, camera_manager):
        self.select = None
        self.main_window: MainWindow = main_window
        self.camera_manager = camera_manager
        self.cameraManager = CameraManager(self.main_window)
        self.workingThread = WorkingThread
        self.setup_view()
        self.setup_window()
    def setup_window(self):
        return

    def setup_view(self):
        self.camera = QMenu()
        self.camera.setStyleSheet("""
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
        self.camera.addAction("Setting", self.Setting_camera)
        self.select = self.camera.addMenu("Select")
        self.setup_select_menu()
        self.camera.addAction("Connect", self.Connect_camera)
        self.camera.addAction("Disconnect", self.Disconnect_camera)
        self.camera.addAction("Capture Picture", self.Capture_Picture)
        self.camera.addAction("Capture Video", self.Capture_video)
        self.camera.addAction("Stop Capture Video", self.Stop_capture_video)

    def setup_select_menu(self):
        self.select.addAction("Camera 0")
        self.select.addAction("Camera 1")
        self.select.addAction("Camera 2")
        self.select.addAction("Camera 3")
        self.select.addAction("Camera 4")
        self.select.addAction("Camera 5")

    def Setting_camera(self):
        self.setting_cam = CameraForm(main_window=self.main_window, camera_manager=self.camera_manager)

    def Connect_camera(self):
        self.workingThread.connectCamera(self)

    def Disconnect_camera(self):
        self.workingThread.disconnectCamera(self)

    def Capture_Picture(self):
        self.workingThread.capturePicture(self)

    def Capture_video(self):
        self.workingThread.captureVideo(self)

    def Stop_capture_video(self):
        self.workingThread.stopCaptureVideo(self)