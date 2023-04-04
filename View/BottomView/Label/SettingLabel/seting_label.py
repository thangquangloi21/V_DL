import os
import sys
from CONSTANT.constant import DEFAULT_ENCODING
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor, QCursor
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QWidget, QListWidgetItem

# from View.MainView.main_window import MainWindow
from View.BottomView.Label.ShowAllLabel.ShowAllLabel import ShowAllLabel
from View.common_view.vision_push_button import VisionPushButton, VisionColorPushButton
from View.common_view.vision_label import VisionLabel
from View.common_view.vision_text_edit import VisionTextEdit
from PyQt5.QtWidgets import QMainWindow
from View.common_view.thanh_tieu_de import ThanhTieuDe
from View.common_view.vision_list_box import VisionListWidget
from PyQt5.QtWidgets import *
from Modules.DeepLearning.label_xml_file import LabelXmlFile


class SettingLabel(QGroupBox):
    enter_name: VisionTextEdit
    folder_path_text: VisionTextEdit
    select_btn: VisionPushButton
    add_btn: VisionPushButton
    show_all: VisionPushButton
    show_a_lbl: ShowAllLabel = None
    grid_settingLabel: QGridLayout
    name_lbl: VisionLabel
    folder_lbl: VisionLabel
    save_btn: VisionPushButton

    def __init__(self, parent, main_window):
        print("Create")
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.label_xml_file = LabelXmlFile(main_window=self.main_window)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setTitle("Setting Label")
        self.setStyleSheet("""
            QGroupBox {
                color: white;
                font: 18px;
                font-weight: bold;
                background: rgb(100, 100, 100);
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
        """)
        self.grid_settingLabel = QGridLayout(self)
        self.grid_settingLabel.setContentsMargins(20, 20, 20, 0)
        self.grid_settingLabel.setVerticalSpacing(10)

    def setup_view(self):
        self.label_name()
        self.folder_path()
        self.add_select_btn()
        self.save_label_btn()
        self.show_all_label()
        self.list_label_view()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_settingLabel.addWidget(self.name_lbl, 0, 0, 1, 1)
        self.grid_settingLabel.addWidget(self.enter_name, 0, 1, 1, 1)
        self.grid_settingLabel.addWidget(self.folder_lbl, 1, 0, 1, 1)
        self.grid_settingLabel.addWidget(self.folder_path_text, 1, 1, 1, 1)
        self.grid_settingLabel.addWidget(self.save_btn, 2, 1, 1, 1)
        self.grid_settingLabel.addWidget(self.select_btn, 2, 0, 1, 1)
        self.grid_settingLabel.addWidget(self.show_all, 3, 0, 1, 1)
        self.grid_settingLabel.addWidget(self.list_lbl_view, 0, 2, 5, 2)

        self.grid_settingLabel.setColumnStretch(0, 1)
        self.grid_settingLabel.setColumnStretch(1, 3)
        self.grid_settingLabel.setColumnStretch(2, 1)
        self.grid_settingLabel.setColumnStretch(3, 1)
        self.grid_settingLabel.setRowStretch(0, 1)
        self.grid_settingLabel.setRowStretch(1, 1)
        self.grid_settingLabel.setRowStretch(2, 1)
        self.grid_settingLabel.setRowStretch(3, 1)
        self.grid_settingLabel.setRowStretch(4, 1)
        self.grid_settingLabel.setRowStretch(5, 1)

    def label_name(self):
        self.name_lbl = VisionLabel( text="Label name:", width=100)
        self.enter_name = VisionTextEdit(parent=self, width=350)

    def folder_path(self):
        self.folder_lbl = VisionLabel( text="Fordel:", width=100)
        self.folder_path_text = VisionTextEdit(parent=self, width=350)

    def add_select_btn(self):
        self.select_btn = VisionPushButton(parent=self, text="Select Folder", width=100)
        self.select_btn.clicked.connect(self.click_open_folder)

    def save_label_btn(self):
        self.save_btn = VisionPushButton(parent=self, text="Save Label", width=100)
        self.save_btn.clicked.connect(self.click_save_label_to_xml)

    def show_all_label(self):
        self.show_all = VisionPushButton(parent=self, text="Show All Label", width=100)
        self.show_all.clicked.connect(self.click_show_all_label)
    list_lbl_view = None  # labels from drawing

    def list_label_view(self):
        self.list_lbl_view = ListLabelView(parent=self, main_window=self.main_window)
        self.list_lbl_view.setCurrentRow(0)

    # event click
    def click_save_label_to_xml(self):
        path_image_show = self.main_window.middle_view.main_show.image_path
        try:
            output_file_name = path_image_show[:path_image_show.rfind('.')]
            print('output_file_name', output_file_name)

            # hàm này chưa được
            # fix lại tỉ lệ
            shapes = self.main_window.middle_view.main_show.rectangele_process.list_info_label
            print(shapes)
            shapess = self.label_xml_file.convert_list_label_info_scale_to_point(list_label=shapes)
            print('shapes', shapess)
            self.label_xml_file.save_create_xml_format(output_file_name=output_file_name,
                                                       shapes=shapess, image_path=path_image_show)
        except Exception as er:
            print(er)

    def click_open_folder(self):
        try:
            # dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'E:\.Clone vision\MES_Deep_learning',
            #                                         QFileDialog.ShowDirsOnly)
            dir_ = QFileDialog.getOpenFileName(self, 'Image files', '', "*.jpg *png *.ico *.bmp *.gif *.GIF *.jpeg ")[0]
            self.main_window.middle_view.main_show.show_image_with_path(image_path=dir_)
            print(dir_)
            dir_ = dir_[:dir_.rfind('.')] + '.xml'
            self.folder_path_text.setText(dir_)
            self.label_xml_file.load_xml_format(xml_path=dir_)
        except Exception as er:
            print(er)
        return

    def click_show_all_label(self):
        self.show_a_lbl = ShowAllLabel(main_window=self.main_window)

    def update_list_name_label(self, list_label_info_change, index_label_change):
        # print(f"list_label_info_change{list_label_info_change}")
        label_info_change = list_label_info_change[index_label_change]

        self.list_lbl_view.delete_label(index_label_change)
        self.list_lbl_view.insert_label(label_info_change[0], label_info_change[1], index_label_change)

    def delete_a_label(self, index):
        self.list_lbl_view.delete_label(index)

    def delete_all_label(self):
        index = self.list_lbl_view.count()
        while index != -1:
            self.delete_a_label(index)
            index -= 1

    def update_check_state_item_label(self):
        check_state_bool = []   # True/False
        for index in range(self.list_lbl_view.count()):
            if self.list_lbl_view.item(index).checkState() == Qt.Checked:
                check_state_bool.append(True)
            else:
                check_state_bool.append(False)
        list_info_label_change = self.main_window.middle_view.main_show.rectangele_process.list_info_label
        for index, check_bool in enumerate(check_state_bool):
            list_info_label_change[index][1] = check_bool
        self.main_window.middle_view.main_show.rectangele_process.list_info_label = list_info_label_change
        self.main_window.middle_view.main_show.rectangele_process.update_painter_from_setting_label()

        return list_info_label_change

# label từ draw rectangle


class ListLabelView(VisionListWidget):
    item: QListWidgetItem

    def __init__(self, parent, main_window):
        VisionListWidget.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

        # self.currentRowChanged.connect(self.click_item_label)
        # self.currentTextChanged.connect(self.click_item_label)
        # self.currentItemChanged.connect(self.click_item_label)
        # self.itemActivated.connect(self.click_item_label)
        # self.itemDoubleClicked.connect(self.click_item_label)
        # self.itemEntered.connect(self.click_item_label)
        # self.itemSelectionChanged.connect(self.click_item_label)

        # double click item
        self.itemDoubleClicked.connect(self.show_popup)
        # click item
        # self.itemPressed.connect(self.click_item)
        self.itemClicked.connect(self.click_item)
        # check state
        self.itemChanged.connect(self.click_check_state_box)

    def setup_window(self):
        return

    def setup_view(self):
        # for label_info in self.list_label:
        #     text = label_info[0]
        #     self.item = QListWidgetItem(text)
        #     if label_info[1]:
        #         self.item.setCheckState(Qt.Checked)
        #     else:
        #         self.item.setCheckState(Qt.Unchecked)
        #     self.addItem(self.item)
        return

    def add_label(self, label_info):
        text = label_info[0]

        item = QListWidgetItem(text)
        if label_info[1]:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)
        self.addItem(item)

    def insert_label(self, label, state, index):
        item = QListWidgetItem(label)
        if state:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)
        self.insertItem(index, item)

    def delete_label(self, index):
        self.takeItem(index)

    def show_current_item_selected(self, index):
        if self.count() > 0:
            self.setCurrentRow(index)

    def click_check_state_box(self):
        print(self.main_window.bottom_view.laybeling.setting_label.update_check_state_item_label())
        self.main_window.bottom_view.laybeling.setting_label.update_check_state_item_label()

    list_info_label = None

    def click_item(self):
        index = self.currentRow()
        print(str(index))
        self.main_window.middle_view.main_show.rectangele_process.update_show_rectangle_by_current_item_index_selected(index)
    menu: QMenu = None
    edit_label_action: QAction
    delete_select_area_action: QAction

    def show_popup(self):
        index = self.currentRow()
        if self.main_window.middle_view.main_show.rectangele_process.list_info_label[index][1]:
            print("show popup edit")
            self.menu = QMenu()
            self.edit_label_action = QAction("Edit", self)
            self.delete_select_area_action = QAction('Delete label', self)
            self.menu.addAction(self.edit_label_action)
            self.menu.addAction(self.delete_select_area_action)
            # triggered connect
            self.delete_select_area_action.triggered.connect(
                self.main_window.middle_view.main_show.rectangele_process.delete_a_area)
            self.edit_label_action.triggered.connect(
                self.main_window.middle_view.main_show.rectangele_process.edit_label)
            self.menu.popup(QCursor.pos())


class EditLabelWindow(QMainWindow):
    thanh_tieu_de: ThanhTieuDe
    name_label: VisionTextEdit
    grid_layout_edit_label: QGridLayout
    central_widget_edit_label: QWidget
    ok_btn: VisionPushButton
    cancel: VisionPushButton
    color_btn: VisionColorPushButton
    list_box_label: VisionListWidget

    def __init__(self, parent, main_window, name_label="", index_label=None):
        QMainWindow.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.color = self.main_window.middle_view.main_show.rectangele_process.current_color_border_rectangle
        self.name_label_edit = name_label
        self.index_label_edit = index_label
        self.list_current_lbl = ListJsonNameLabel(main_window=self.main_window)
        self.setup_window()
        self.setup_view()
        self.show()

    def setup_window(self):
        self.setWindowTitle("LabelImg")
        self.setStyleSheet("""
            background: rgb(200, 200, 200);
        """)
        self.resize(270, 300)
        self.central_widget_edit_label = QWidget(self)
        self.grid_layout_edit_label = QGridLayout(self.central_widget_edit_label)
        self.grid_layout_edit_label.setContentsMargins(10, 10, 10, 10)

    def setup_view(self):
        # self.setup_thanh_tieu_de()
        self.setup_edit_text()
        self.setup_button()
        self.setup_list_box()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_layout_edit_label.addWidget(self.name_label, 0, 0, 1, 4)
        self.grid_layout_edit_label.addWidget(self.color_btn, 1, 1, 1, 1)
        self.grid_layout_edit_label.addWidget(self.ok_btn, 1, 2, 1, 1)
        self.grid_layout_edit_label.addWidget(self.cancel, 1, 3, 1, 1)
        self.grid_layout_edit_label.addWidget(self.list_box_label, 2, 0, 1, 4)

        self.grid_layout_edit_label.setRowStretch(0, 1)
        self.grid_layout_edit_label.setRowStretch(1, 1)
        self.grid_layout_edit_label.setRowStretch(2, 7)

        self.grid_layout_edit_label.setColumnStretch(0, 7)
        self.grid_layout_edit_label.setColumnStretch(1, 1)
        self.grid_layout_edit_label.setColumnStretch(2, 1)
        self.grid_layout_edit_label.setColumnStretch(3, 1)

        self.setCentralWidget(self.central_widget_edit_label)

    # def setup_thanh_tieu_de(self):
    #     self.thanh_tieu_de = ThanhTieuDe(parent=self, width=self.width(), height=40, name_window="labelImg")

    def setup_edit_text(self):
        self.name_label = VisionTextEdit(parent=self.central_widget_edit_label)
        if self.name_label_edit != '':
            self.name_label.setText(self.name_label_edit)
        self.name_label.setStyleSheet("""
            background: white;
            color: black;
            font: 14px;
        """)
        self.name_label.setMaximumSize(214748364, 30)

    def setup_button(self):
        self.color_btn = VisionColorPushButton(parent=self.central_widget_edit_label, text="Color", color=self.color)
        self.ok_btn = VisionPushButton(parent=self.central_widget_edit_label, text="Save")
        self.ok_btn.clicked.connect(self.save_label)
        self.cancel = VisionPushButton(parent=self.central_widget_edit_label, text="Cancel")
        self.cancel.clicked.connect(self.cancel_edit_label)
    list_label_json = None

    def setup_list_box(self):
        # label load tu file json, ....
        self.list_box_label = VisionListWidget(parent=self.central_widget_edit_label)
        self.load_list_label()
        self.list_box_label.clicked.connect(self.clicked_label_in_list_box)
        return

    # cần label load tu file json, ....

    def load_list_label(self):
        self.list_label_json = self.list_current_lbl.list_json_name_label
        for index_row, label in enumerate(self.list_label_json, 0):
            self.list_box_label.insertItem(index_row, label)
    new_name_label = ''

    def save_label(self):
        # save for Add
        self.new_name_label = self.name_label.toPlainText()
        if self.index_label_edit is None:
            if self.new_name_label.count(" ") != len(self.new_name_label):
                if self.new_name_label != "":
                    # if self.new_name_label not in self.list_label_json:
                    #     self.list_label_json.append(self.new_name_label)
                    self.close()
                    self.main_window.middle_view.main_show.rectangele_process.add_label()
        # save for Edit
        elif len(self.new_name_label) != 0:
            print("edit")
            name_change = self.name_label.toPlainText()
            self.main_window.middle_view.main_show.rectangele_process.edit_name_label(name_change=name_change)
            self.close()

    def cancel_edit_label(self):
        if self.index_label_edit is None:
            self.main_window.middle_view.main_show.rectangele_process.add_label()
            self.main_window.middle_view.main_show.rectangele_process.delete_a_area()
            self.close()
            print("exit + del area")
        else:
            print("casfaf")
            self.close()
            print("exit")

    def clicked_label_in_list_box(self):
        item = self.list_box_label.currentItem()
        self.name_label.setText(item.text())


class ListJsonNameLabel:
    # can load json....
    def __init__(self, main_window):
        self.main_window: MainWindow = main_window
        self.list_json_name_label = ['dog', 'person', 'cat', 'car', 'soup', 'number', 'chicken',
                                     'tree', 'dice', 'book', 'pencil', 'pen']





