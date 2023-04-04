import os
from tkinter import filedialog, messagebox
import cv2
import numpy as np
import CommonAssit.CommonAssit as CommonAssit
from PyQt5.QtWidgets import QFrame, QPushButton, QToolBar, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QImage
from View.MainView.main_window import MainWindow
from WorkingThread import WorkingThread

HEIGHT = 95
SIZE = 30
DISTANCE = 3


class ToolBar(QFrame):
    zoom_reset_btn: QAction

    def __init__(self, parent, main_window):
        QFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.zoom_reset_btn = None
        self.zoom_down_btn = None
        self.zoom_up_btn = None
        self.draw_cir_btn = None
        self.draw_rectangle_btn = None
        self.stop_video_btn = None
        self.cap_video_btn = None
        self.cap_pic_btn = None
        self.save2Btn = None
        self.save1Btn = None
        self.openBtn = None
        self.tool_bar = None
        self.workingThread = WorkingThread(main_window=main_window)
        self.list_name_image_in_folder = None
        self.setup_window()
        self.setup_view()
        self.event_click()
        self.current_index = -1
        # self.originalImage = None
        self.list_image_path = []
        self.zoom_in, self.zoom_out, self.reset_zoom = False, False, False
        self.scale_factor = 1.0
        self.image = ''

    def setup_window(self):
        self.resize(1300, int(HEIGHT / 2))
        self.display_Styleesheet()
        return

    def setup_view(self):
        self.tool_bar = QToolBar(parent=self)
        self.btn_open()
        self.save_orig()
        self.save_process()
        self.capture_pic()
        self.capture_video()
        self.stop_video()
        self.draw_rec()
        self.draw_circle()
        self.zoom_up()
        self.zoom_down()
        self.zoom_reset()

    def btn_open(self):
        icon_open = QIcon()
        icon_open.addPixmap(QPixmap("./Resource/Icon/open-file-icon.png"), QIcon.Normal, QIcon.Off)
        self.openBtn = QAction(parent=self.tool_bar, text="Open Image")
        self.openBtn.setIcon(icon_open)
        self.tool_bar.addAction(self.openBtn)

    def save_orig(self):
        icon_save1 = QIcon()
        icon_save1.addPixmap(QPixmap("./Resource/Icon/save-file-icon-3.png"), QIcon.Normal, QIcon.Off)
        self.save1Btn = QAction(parent=self.tool_bar, text="Save Original Image")
        self.save1Btn.setIcon(icon_save1)
        self.tool_bar.addAction(self.save1Btn)

    def save_process(self):
        icon_save2 = QIcon()
        icon_save2.addPixmap(QPixmap("./Resource/Icon/save-file-icon-3.png"), QIcon.Normal, QIcon.Off)
        self.save2Btn = QAction(parent=self.tool_bar, text="Save Process Image")
        self.save2Btn.setIcon(icon_save2)
        self.tool_bar.addAction(self.save2Btn)

    def capture_pic(self):
        icon_cap_pic = QIcon()
        icon_cap_pic.addPixmap(QPixmap("./Resource/Icon/Camera.png"), QIcon.Normal, QIcon.Off)
        self.cap_pic_btn = QAction(parent=self.tool_bar, text="Capture Image")
        self.cap_pic_btn.setIcon(icon_cap_pic)
        self.tool_bar.addAction(self.cap_pic_btn)

    def capture_video(self):
        icon_cap_video = QIcon()
        icon_cap_video.addPixmap(QPixmap("./Resource/Icon/Camera1.png"), QIcon.Normal, QIcon.Off)
        self.cap_video_btn = QAction(parent=self.tool_bar, text="Capture Video")
        self.cap_video_btn.setIcon(icon_cap_video)
        self.tool_bar.addAction(self.cap_video_btn)

    def stop_video(self):
        icon_stop_video = QIcon()
        icon_stop_video.addPixmap(QPixmap("./Resource/Icon/stopvideo.png"), QIcon.Normal, QIcon.Off)
        self.stop_video_btn = QAction(parent=self.tool_bar, text="Stop Capture Video")
        self.stop_video_btn.setIcon(icon_stop_video)
        self.tool_bar.addAction(self.stop_video_btn)

    def draw_rec(self):
        icon_draw_rec = QIcon()
        icon_draw_rec.addPixmap(QPixmap("./Resource/Icon/reg.png"), QIcon.Normal, QIcon.Off)
        self.draw_rectangle_btn = QAction(parent=self.tool_bar, text="Draw Rectangle")
        self.draw_rectangle_btn.setIcon(icon_draw_rec)
        self.tool_bar.addAction(self.draw_rectangle_btn)

    def draw_circle(self):
        icon_draw_cir = QIcon()
        icon_draw_cir.addPixmap(QPixmap("./Resource/Icon/cirle.png"), QIcon.Normal, QIcon.Off)
        self.draw_cir_btn = QAction(parent=self.tool_bar, text="Draw Circle")
        self.draw_cir_btn.setIcon(icon_draw_cir)
        self.tool_bar.addAction(self.draw_cir_btn)

    def zoom_up(self):
        icon_zoom_up = QIcon()
        icon_zoom_up.addPixmap(QPixmap("./Resource/Icon/zomin.png"), QIcon.Normal, QIcon.Off)
        self.zoom_up_btn = QAction(parent=self.tool_bar, text="Zoom +")
        self.zoom_up_btn.setIcon(icon_zoom_up)
        self.tool_bar.addAction(self.zoom_up_btn)

    def zoom_down(self):
        icon_zoom_down = QIcon()
        icon_zoom_down.addPixmap(QPixmap("./Resource/Icon/zomout.png"), QIcon.Normal, QIcon.Off)
        self.zoom_down_btn = QAction(parent=self.tool_bar, text="Zoom -")
        self.zoom_down_btn.setIcon(icon_zoom_down)
        self.tool_bar.addAction(self.zoom_down_btn)

    def zoom_reset(self):
        icon_zoom_reset = QIcon()
        icon_zoom_reset.addPixmap(QPixmap("./Resource/Icon/zoomreset.png"), QIcon.Normal, QIcon.Off)
        self.zoom_reset_btn = QAction(parent=self.tool_bar, text="Reset Zoom")
        self.zoom_reset_btn.setIcon(icon_zoom_reset)
        self.tool_bar.addAction(self.zoom_reset_btn)
#event
    def event_click(self):
        self.openBtn.triggered.connect(self.open)
        self.save1Btn.triggered.connect(self.saveOriginalImage)
        self.save2Btn.triggered.connect(self.saveProcessedImage)
        # self.zoom_up_btn.triggered.connect(self.zoom_in)
        # self.zoom_down_btn.triggered.connect(self.zoom_out)
        # self.zoom_reset_btn.triggered.connect(self.reset_zoom)
    def open(self):
        self.setup_open()

    # display

    def display_Styleesheet(self):
        self.setStyleSheet("""
            QToolButton{
                background: transparent;
                padding: 2px;
            }
            QToolButton:hover{
                background-color:lightgray;
            }
            QToolButton:pressed{
                background-color:rgb(255, 118, 39);
            }
            QToolButton::menu-button {
                border: 2px solid red;
                border-top-right-radius: 6px;
                border-bottom-right-radius: 6px;
                width: 50px;
            }
        """)

    def setup_open(self):

        files = QFileDialog.getOpenFileName(self, 'Image files', '', "*.jpg *png *.ico *.bmp *.gif *.GIF *.jpeg ")
        self.path_image = files[0]

        # print(self.originalImage)
        self.image_dir = os.path.dirname(self.path_image)
        if len(self.image_dir) != 0:
            self.list_name_image_in_folder = os.listdir(self.image_dir)
            print(self.path_image, self.image_dir)

            list_duoi = ["jpg", "png", "ico", "bmp", "gif", "GIF", "jpeg"]
            for name_image in self.list_name_image_in_folder:
                index = name_image.rfind('.')
                extension_path = name_image[index + 1:]
                if extension_path in list_duoi:
                    path = self.image_dir + '/' + name_image
                    self.list_image_path.append(path)
            self.current_index = self.list_image_path.index(self.path_image)
            print(self.list_image_path)
            print(f"current img idex: {self.current_index}")
        print(len(self.path_image))
        if len(self.path_image) == 0:
            pass
        else:
            self.originalImage = cv2.imdecode(np.fromfile(self.path_image, dtype=np.uint8), cv2.IMREAD_COLOR)
            self.main_window.middle_view.main_show.show_image_with_numpy_image(self.originalImage)


    def get_all_image(self, path_image):
        self.image_dir = os.path.dirname(path_image)
        print(self.image_dir)

        if len(self.image_dir) != 0:
            self.list_name_image_in_folder = os.listdir(self.image_dir)

            list_duoi = ["jpg", "png", "ico", "bmp", "gif", "GIF", "jpeg"]
            for name_image in self.list_name_image_in_folder:
                index = name_image.rfind('.')
                extension_path = name_image[index + 1:]
                if extension_path in list_duoi:
                    path = self.image_dir + '/' + name_image
                    self.list_image_path.append(path)
            print(self.list_image_path)
            self.current_index = self.list_image_path.index(path_image)
            print(f"current img idex: {self.current_index}")
        print(len(path_image))
        if len(path_image) == 0:
            pass
        else:
            self.originalImage = cv2.imdecode(np.fromfile(path_image, dtype=np.uint8), cv2.IMREAD_COLOR)
            self.main_window.middle_view.main_show.show_image_with_numpy_image(self.originalImage)


    def saveOriginalImage(self):

        save_file = QFileDialog.getSaveFileName(self, caption="Save Image", filter ="JPG (*.jpg);;"
                                                                                        " PNG (*.png);; ico (*.ico);;"
                                                                                        " bmp (*.bmp);; gif (*.gif);;"
                                                                                        "GIF (*.GIF);; jpeg (*.jpeg);;"
                                                                                    "All file (*.*)")
        save_file = save_file[0]
        if len(save_file) != 0:
             try:
              fileType, fileName = CommonAssit.getImageTypeFromName(save_file)
              cv2.imencode(fileType, self.originalImage)[1].tofile(fileName)
             except Exception as error:
             # self.mainWindow.runningTab.insertLog("ERROR Save original image: {}".format(error))
               messagebox.showerror('Image saving', 'Cannot save the Image')
               print("save anhr err: ", error)
        else:
               messagebox.showwarning('Image saving', 'Please input the name of Image!')

    def saveProcessedImage(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Saves Image", filter="JPG (*.jpg);;"
                                                                                   " PNG (*.png);; ico (*.ico);; bmp (*.bmp);; gif (*.gif);;"
                                                                                   "GIF (*.GIF);; jpeg (*.jpeg);;All file (*.*)")
        save_file = save_file[0]
        if len(save_file) != 0:
            try:
                fileType, fileName = CommonAssit.getImageTypeFromName(save_file)
                cv2.imencode(fileType, self.originalImage)[1].tofile(fileName)
            except Exception as error:
                # self.mainWindow.runningTab.insertLog("ERROR Save original image: {}".format(error))
                messagebox.showerror('Image saving', 'Cannot save the Image')
        else:
            messagebox.showwarning('Image saving', 'Please input the name of Image!')



           









