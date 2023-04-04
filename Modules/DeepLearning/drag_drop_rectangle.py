import math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Modules.DeepLearning.draw_rectangle import DrawCorner, DrawRectangle, ColorDrawing
from View.BottomView.Label.SettingLabel.seting_label import EditLabelWindow
from View.MainView.main_window import MainWindow
FREE_STATE = 11         # Trạng thái tự do
BUILDING_SQUARE = 22     # Xây dựng

TOP_LEFT_EDIT = 1     # chỉnh sửa resize 4goc
TOP_RIGHT_EDIT = 2
BOTTOM_LEFT_EDIT = 3
BOTTOM_RIGHT_EDIT = 4
BOTTOM_CENTER_EDIT = 5
MOVE_RECT_EDIT = 6
MOVE_A_RECT_EDIT = 8     # edit hcn dang chon trong list

CURSOR_ON_TOP_LEFT_SIDE = 1    # Con trỏ ở ?
CURSOR_ON_TOP_RIGHT_SIDE = 2
CURSOR_ON_BOTTOM_LEFT_SIDE = 3
CURSOR_ON_BOTTOM_RIGHT_SIDE = 4
CURSOR_ON_BOTTOM_CENTER_SIDE = 5
MOVE_RECT = 6
MOVE_A_RECT = 8       # chon 1 hcn trong cac hcn dang show
CURSOR_ON_OUT_SIDE = 7

CURSOR_ON_RECT_ = 98            #
CURSOR_ON_RECT_IN_LIST = 99     # rectangle in list

SUB_LOCATION = 10
BUTTON_SIZE_WID = 10
BUTTON_SIZE_HEI = 10

STEP_ROTATE = 1


class RectangleProcess(QWidget):
    last_global_pos = None
    top_right: QPoint
    top_left: QPoint
    bottom_left: QPoint
    bottom_right: QPoint
    rotate: QPoint
    background_rectangle: QBrush
    background_4_corner: QBrush
    draw_4_corner: QPainter
    drawing_rect_color: QBrush
    color_transparent: QBrush
    drawing_circle_color: QBrush

    def __init__(self, parent, main_window):
        QWidget.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.color_drawing = ColorDrawing
        self.current_color_border_rectangle = "#00ff00"
        self.khoi_tao()
        self.setup_color_begin()
        self.begin_pos, self.end_pos = QPoint(), QPoint()

        self.rota_parameter = 0
        self.state = FREE_STATE

        self.setMouseTracking(True)   # mui ten chinh khoang cach
        self.free_cursor_on_side = 0  # con tro o ben
        self.notPress = True

        self.coor_a = self.top_left
        self.coor_b = self.top_right
        self.coor_c = self.bottom_left
        self.coor_d = self.bottom_right

        self.move_counter_clockwise = False
        # quy uoc goc rectangle
        #  1         2       a      b
        #  3         4       c      d
        self.list_info_label = []  # list info của các label tọa độ hiển thị trên màn view
        # 1 label: tên, status hiển thị, tọa độ, ma tran anh [name_label, True, coordinate, numpy_image]
        self.real_list_info_label = []  # tọa độ vùng thật trên ảnh


        self.top_left_rect_in_list = (0, 0)    # toa do hcn dang chon trong danh sach
        self.bottom_right_in_list = (0, 0)
        # self.a_rectangle_selected_in_list = (0, 0, 0, 0)  # (x1, y1, x2, x2)
        # self.current_click_a_rectangle_selected_in_list = (0, 0, 0, 0)

        self.check_in_rectangle = CURSOR_ON_RECT_   # cursor on rect not in list
        self.flag_draw = False

    def khoi_tao(self):
        self.top_left, self.top_right = QPoint(), QPoint()
        self.bottom_right, self.bottom_left = QPoint(), QPoint()
        # self.current_click_a_rectangle_selected_in_list = (0, 0, 0, 0)
        self.background_rectangle = QBrush(Qt.FDiagPattern)
        self.rotate = QPoint()
        self.flag_draw = False

    def setup_color_begin(self):
        self.drawing_circle_color = self.background_4_corner = \
            self.drawing_rect_color = self.color_drawing.color_transparent

    def setup_color_drawing(self):
        self.drawing_rect_color = self.color_drawing.color_green
        self.drawing_circle_color = self.color_drawing.color_yellow
        self.background_4_corner = self.color_drawing.color_yellow

    def paintEvent(self, event):
        self.top_right = QPoint(self.bottom_right.x(), self.top_left.y())
        self.bottom_left = QPoint(self.top_left.x(), self.bottom_right.y())
        self.current_click_a_rectangle_selected_in_list = \
            (self.convert_two_qpoint_to_tuple(self.top_left, self.bottom_right))

        self.current_click_a_rectangle_selected_in_list = \
            self.correct_point_for_list_rectangle(tuple_point=self.current_click_a_rectangle_selected_in_list)

        # convert current_click_a_rectangle_selected_in_list to scale
        # self.current_click_a_rectangle_selected_in_list = \
        #     self.convert_tuple_to_tuple_scale(tuple_coordinate=self.current_click_a_rectangle_selected_in_list)

        # x_center = int((self.bottom_right.x() - self.bottom_left.x()) / 2) + self.bottom_left.x()
        # self.rotate = QPoint(x_center, self.bottom_right.y())

        # xCenter = x_center
        # yCenter = int((self.bottom_right.y() - self.top_left.y()) / 2) + self.top_left.y()
        # draw_rectangle.translate(xCenter, yCenter)
        # draw_rectangle.rotate(self.rota_parameter) #*math.pi/180)
        # draw_rectangle.translate(-xCenter, -yCenter)
        self.height_pixel_view = self.main_window.middle_view.main_show.show_image_label.height()
        self.width_pixel_view = self.main_window.middle_view.main_show.show_image_label.width()
        DrawRectangle(self, self.drawing_rect_color, self.background_rectangle, self.top_left, self.bottom_right)
        for index_rec in self.list_info_label:
            if index_rec[1]:
                color_border = QColor(index_rec[3])
                coordinate_rectangle_scale = index_rec[2]
                # convert correct rectangle not scale
                correct_coordinate_rectangle = self.convert_tuple_scale_to_tuple_qpoint(
                    tuple_coordinate_scale=coordinate_rectangle_scale)
                DrawRectangle(self, color_border, self.background_rectangle,
                              QPoint(correct_coordinate_rectangle[0],
                                     correct_coordinate_rectangle[1]),
                              QPoint(correct_coordinate_rectangle[2],
                                     correct_coordinate_rectangle[3]))
        DrawCorner(self, self.drawing_circle_color,
                   self.background_4_corner, self.top_left,
                   self.bottom_left, self.top_right, self.bottom_right, self.rotate)
        # draw_4_corner = QPainter(self)
        # draw_4_corner.setBrush(self.background_4_corner)
        # draw_4_corner.drawRect(self.top_left.x() - 5, self.top_left.y() - 5, BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        # draw_4_corner.drawRect(self.top_right.x() - 5, self.top_right.y() - 5, BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        # draw_4_corner.drawRect(self.bottom_right.x() - 5, self.bottom_right.y() - 5, BUTTON_SIZE_WID,
        #                        BUTTON_SIZE_WID)
        # draw_4_corner.drawRect(self.bottom_left.x() - 5, self.bottom_left.y() - 5, BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        # draw_4_corner.drawRect(self.rotate.x(), self.rotate.y(), BUTTON_SIZE_WID, BUTTON_SIZE_WID)

        # update show row in list label on bottom view
        self.update_set_current_row_show_on_bottom_view()

        if not self.free_cursor_on_side:
            return

    def cursor_on_side(self, e_pos) -> int:  # con tro o ben
        y1, y2 = sorted([self.top_left.y(), self.bottom_right.y()])
        x1, x2 = sorted([self.top_left.x(), self.bottom_right.x()])
        if y1 <= e_pos.y() <= y2:
            if abs(self.top_left.x() - e_pos.x()) <= SUB_LOCATION and \
                    abs(self.top_left.y() - e_pos.y()) <= SUB_LOCATION:
                return CURSOR_ON_TOP_LEFT_SIDE
            elif abs(self.top_right.x() - e_pos.x()) <= SUB_LOCATION and \
                    abs(self.top_right.y() - e_pos.y()) <= SUB_LOCATION:
                return CURSOR_ON_TOP_RIGHT_SIDE
            elif abs(self.bottom_left.x() - e_pos.x()) <= SUB_LOCATION and \
                    abs(self.bottom_left.y() - e_pos.y()) <= SUB_LOCATION:
                return CURSOR_ON_BOTTOM_LEFT_SIDE
            elif abs(self.bottom_right.x() - e_pos.x()) <= SUB_LOCATION and \
                    abs(self.bottom_right.y() - e_pos.y()) <= SUB_LOCATION:
                return CURSOR_ON_BOTTOM_RIGHT_SIDE
            # elif abs(self.rotate.x() - e_pos.x()) <= SUB_LOCATION and \
            #         abs(self.rotate.y() - e_pos.y()) <= SUB_LOCATION:
            #     return CURSOR_ON_BOTTOM_CENTER_SIDE
            elif (self.check_in_rectangle == CURSOR_ON_RECT_) and \
                    (x1 + 2 * SUB_LOCATION <= e_pos.x() <= x2 - 2 * SUB_LOCATION and
                     y1 <= e_pos.y() <= y2 - 3 * SUB_LOCATION):
                return MOVE_RECT

            # check xem vi tri con tro dang nằm ở hcn nào trong tất cả hcn dang show
        if self.check_in_rectangle == CURSOR_ON_RECT_IN_LIST:
            # cursor on rectangle in list
            has_found_in_list = False      #
            reversed_list_info_label = self.list_info_label[::-1]  # dao list hcn
            self.list_info_label = []
            for info_label in reversed_list_info_label:
                # (top_left(x, y), bottom_right(x, y))
                coordinate_rectangle_scale = info_label[2]
                coordinate_rectangle = self.convert_tuple_scale_to_tuple_qpoint(
                    tuple_coordinate_scale=coordinate_rectangle_scale)
                y_min, y_max = sorted([coordinate_rectangle[1], coordinate_rectangle[3]])
                x_min, x_max = sorted([coordinate_rectangle[0], coordinate_rectangle[2]])
                if not has_found_in_list and ((x_min + SUB_LOCATION <= e_pos.x() <= x_max - SUB_LOCATION and
                                               y_min + SUB_LOCATION <= e_pos.y() <= y_max - SUB_LOCATION)):

                    # todo
                    self.top_left_rect_in_list = (coordinate_rectangle[0], coordinate_rectangle[1])
                    self.bottom_right_in_list = (coordinate_rectangle[2], coordinate_rectangle[3])
                    if info_label[1]:
                        has_found_in_list = True
                self.list_info_label.append(info_label)
            self.list_info_label = self.list_info_label[::-1]
            if has_found_in_list:
                return MOVE_A_RECT
            else:
                return CURSOR_ON_OUT_SIDE

        if not (x1 <= e_pos.x() <= x2 and y1 <= e_pos.y() <= y2):
            return CURSOR_ON_OUT_SIDE
        return 0

    def mousePressEvent(self, event: QMouseEvent):
        print(event.pos())
        print("list", self.list_info_label)
        if event.button() == Qt.LeftButton:
            self.last_global_pos = event.globalPos()
            self.begin_pos = event.pos()
            side = self.cursor_on_side(event.pos())
            if side == CURSOR_ON_TOP_LEFT_SIDE:
                self.state = TOP_LEFT_EDIT
            elif side == CURSOR_ON_TOP_RIGHT_SIDE:
                self.state = TOP_RIGHT_EDIT
            elif side == CURSOR_ON_BOTTOM_LEFT_SIDE:
                self.state = BOTTOM_LEFT_EDIT
            elif side == CURSOR_ON_BOTTOM_RIGHT_SIDE:
                self.state = BOTTOM_RIGHT_EDIT
            elif side == CURSOR_ON_BOTTOM_CENTER_SIDE:
                self.state = BOTTOM_CENTER_EDIT
            elif side == MOVE_RECT:
                self.check_in_rectangle = CURSOR_ON_RECT_  # rectangle not in list
                self.state = MOVE_RECT_EDIT

            elif side == MOVE_A_RECT:
                self.check_in_rectangle = CURSOR_ON_RECT_IN_LIST
                self.state = MOVE_A_RECT_EDIT
            else:
                if self.flag_draw:
                    self.setup_color_drawing()
                    self.state = BUILDING_SQUARE
                    self.top_left = event.pos()
                    self.bottom_right = event.pos()
                    self.check_in_rectangle = CURSOR_ON_RECT_
                    self.update()

    def apply_event(self, event: QMouseEvent):
        print(self.state)
        if self.state == BUILDING_SQUARE:
            self.check_in_rectangle = CURSOR_ON_RECT_
            self.end_pos = event.pos()
            self.bottom_right = event.pos()
        elif self.state == TOP_LEFT_EDIT:
            self.top_left = self.top_left + event.globalPos() - self.last_global_pos
            if self.check_in_rectangle == CURSOR_ON_RECT_IN_LIST:
                self.edit_coor_a_rectangle_selected_in_list()
        elif self.state == TOP_RIGHT_EDIT:
            self.bottom_right.setX(self.bottom_right.x() + event.globalPos().x() - self.last_global_pos.x())
            self.top_left.setY(self.top_left.y() + event.globalPos().y() - self.last_global_pos.y())
            if self.check_in_rectangle == CURSOR_ON_RECT_IN_LIST:
                self.edit_coor_a_rectangle_selected_in_list()
        elif self.state == BOTTOM_LEFT_EDIT:
            self.top_left.setX(self.top_left.x() + event.globalPos().x() - self.last_global_pos.x())
            self.bottom_right.setY(self.bottom_right.y() + event.globalPos().y() - self.last_global_pos.y())
            if self.check_in_rectangle == CURSOR_ON_RECT_IN_LIST:
                self.edit_coor_a_rectangle_selected_in_list()
        elif self.state == BOTTOM_RIGHT_EDIT:
            self.bottom_right = self.bottom_right + event.globalPos() - self.last_global_pos
            if self.check_in_rectangle == CURSOR_ON_RECT_IN_LIST:
                self.edit_coor_a_rectangle_selected_in_list()
        elif self.state == BOTTOM_CENTER_EDIT:
            if event.globalPos().x() > self.last_global_pos.x():
                self.move_counter_clockwise = False
                print("xuoi")
                self.rota_parameter += STEP_ROTATE
                self.last_global_pos = event.globalPos()
            elif event.globalPos().x() < self.last_global_pos.x():
                self.move_counter_clockwise = True
                self.rota_parameter += -STEP_ROTATE
                self.last_global_pos = event.globalPos()
        elif self.state == MOVE_RECT_EDIT:
            self.top_left = self.top_left + event.globalPos() - self.last_global_pos
            self.bottom_right = self.bottom_right + event.globalPos() - self.last_global_pos
        elif self.state == MOVE_A_RECT_EDIT:
            self.top_left = self.top_left + event.globalPos() - self.last_global_pos
            self.bottom_right = self.bottom_right + event.globalPos() - self.last_global_pos
            self.edit_coor_a_rectangle_selected_in_list()
        self.call_calculate_coordinates()
        self.last_global_pos = event.globalPos()
        self.check_limit()

    width_pixel_view = None
    height_pixel_view = None

    def mouseMoveEvent(self, event: QMouseEvent):
        # self.width_pixel_view = self.width()
        # self.height_pixel_view = self.height()
        if self.state == FREE_STATE:
            self.top_right = QPoint(self.bottom_right.x(), self.top_left.y())
            self.bottom_left = QPoint(self.top_left.x(), self.bottom_right.y())
            x = int((self.bottom_right.x() - self.bottom_left.x()) / 2) + self.bottom_left.x()
            self.rotate = QPoint(x, self.bottom_right.y())
            self.free_cursor_on_side = self.cursor_on_side(event.pos())

            if self.free_cursor_on_side == CURSOR_ON_TOP_LEFT_SIDE or\
                    self.free_cursor_on_side == CURSOR_ON_BOTTOM_RIGHT_SIDE:
                self.setCursor(Qt.SizeFDiagCursor)                              # show icon
            elif self.free_cursor_on_side == CURSOR_ON_TOP_RIGHT_SIDE or\
                    self.free_cursor_on_side == CURSOR_ON_BOTTOM_LEFT_SIDE:
                self.setCursor(Qt.SizeBDiagCursor)
            elif self.free_cursor_on_side == CURSOR_ON_BOTTOM_CENTER_SIDE:
                self.setCursor(Qt.SizeHorCursor)
            elif self.free_cursor_on_side == MOVE_RECT:
                self.setCursor(Qt.SizeAllCursor)
            elif self.free_cursor_on_side == MOVE_A_RECT_EDIT:
                # gan toa do của hcn trong list cho đối tượng hiện tại
                self.top_left = QPoint(self.top_left_rect_in_list[0], self.top_left_rect_in_list[1])
                self.bottom_right = QPoint(self.bottom_right_in_list[0], self.bottom_right_in_list[1])
                self.setCursor(Qt.SizeAllCursor)
            else:
                self.unsetCursor()
            self.update()
        else:
            self.apply_event(event)
            self.update()

    def mouseReleaseEvent(self, event):
        if self.state == BUILDING_SQUARE:
            self.edit_label_window = EditLabelWindow(parent=self, main_window=self.main_window)
        self.flag_draw = False
        self.correct_point()
        self.update()
        self.state = FREE_STATE

    def call_calculate_coordinates(self):
        self.coordinate_rectangle_rotate(self.top_left.x(), self.top_left.y(), self.bottom_right.x(),
                                         self.bottom_right.y(), self.rota_parameter)

    def coordinate_rectangle_rotate(self, x1, y1, x2, y2, theta):  # calculate tọa độ các dinh khi xoay
        theta = (theta % 180) * math.pi / 180
        dx = int(x2-x1)/2
        dy = int(y2-y1)/2
        self.coor_c.setX(int(-dx * math.cos(theta) - dy * math.sin(theta) + x1 + dx))
        self.coor_c.setY(int(-dx * math.sin(theta) + dy * math.cos(theta) + y1 + dy))

        self.coor_d.setX(int(dx * math.cos(theta) - dy * math.sin(theta) + x1 + dx))   # bottomRight
        self.coor_d.setY(int(dx * math.sin(theta) + dy * math.cos(theta) + y1 + dy))

        self.coor_b.setX(int(dx * math.cos(theta) + dy * math.sin(theta) + x1 + dx))
        self.coor_b.setY(int(dx * math.sin(theta) - dy * math.cos(theta) + y1 + dy))

        self.coor_a.setX(int(-dx * math.cos(theta) + dy * math.sin(theta) + x1 + dx))   # topLeft
        self.coor_a.setY(int(-dx * math.sin(theta) - dy * math.cos(theta) + y1 + dy))

        if self.move_counter_clockwise:
            tmp1 = self.coor_a
            self.coor_a = self.coor_d
            self.coor_d = tmp1
            tmp1 = self.coor_c
            self.coor_c = self.coor_b
            self.coor_b = tmp1
    menu: QMenu
    add_area_action: QAction
    show_area: QAction
    delete_area_in_list_action: QAction
    delete_select_area_action: QAction
    draw_rect_action: QAction
    edit_label_action: QAction
    copy_label_action: QAction

    def contextMenuEvent(self, event):
        self.menu = QMenu()
        self.draw_rect_action = QAction("Draw rectangle", self)
        self.add_area_action = QAction('Add Area', self)
        self.edit_label_action = QAction("Edit", self)
        self.copy_label_action = QAction("Copy", self)
        self.delete_area_in_list_action = QAction('Del Area In List', self)
        self.delete_select_area_action = QAction('Del Select Area', self)
        # triggered connect
        self.delete_area_in_list_action.triggered.connect(self.delete_all_area)
        self.delete_select_area_action.triggered.connect(self.delete_a_area)
        self.add_area_action.triggered.connect(self.add_label)
        self.edit_label_action.triggered.connect(self.edit_label)
        self.copy_label_action.triggered.connect(self.copy_label)
        self.draw_rect_action.triggered.connect(self.function_draw_rec)

        if self.cursor_on_side(event.pos()) == MOVE_RECT:
            self.menu.addAction(self.add_area_action)
            self.menu.popup(QCursor.pos())
        elif self.cursor_on_side(event.pos()) == MOVE_A_RECT:
            self.menu.addAction(self.edit_label_action)
            self.menu.addAction(self.copy_label_action)
            self.menu.addAction(self.delete_select_area_action)
            self.menu.addAction(self.delete_area_in_list_action)
            self.menu.popup(QCursor.pos())
        else:
            self.menu.addAction(self.draw_rect_action)
            self.menu.addAction(self.delete_area_in_list_action)
            self.menu.popup(QCursor.pos())

    def function_draw_rec(self):
        self.flag_draw = True
        print("Can draw!")

    edit_label_window: EditLabelWindow

    def add_label(self):
        self.check_in_rectangle = CURSOR_ON_RECT_IN_LIST
        coordinate_rect_tuple = self.convert_two_qpoint_to_tuple(self.top_left, self.bottom_right)
        coordinate_rect_tuple_scale = self.convert_tuple_qpoint_to_tuple_scale(
            tuple_qpoint_coordinate=coordinate_rect_tuple)
        name_label = self.edit_label_window.new_name_label
        status_show = True
        try:
            color = self.edit_label_window.color_btn.color
        except NameError:
            color = None
        numpy_image = None

        label_info = []
        label_info.append(name_label)
        label_info.append(status_show)
        label_info.append(coordinate_rect_tuple_scale)
        label_info.append(color)
        label_info.append(numpy_image)

        if label_info not in self.list_info_label:
            self.list_info_label.append(label_info)
        self.main_window.bottom_view.laybeling.setting_label.list_lbl_view.add_label(label_info)
    index: int

    def edit_label(self):
        index = self.get_index_label_in_list_info_label_by_coordinate()
        name_label = self.list_info_label[index][0]
        self.current_color_border_rectangle = self.list_info_label[index][3]
        self.edit_label_window = EditLabelWindow(parent=self, main_window=self.main_window,
                                                 name_label=name_label, index_label=index)
        print("edit_Show Window label")

    def copy_label(self):
        index = self.get_index_label_in_list_info_label_by_coordinate()
        new_rectangle_coordinates = self.list_info_label[index].copy()

        self.list_info_label.append(new_rectangle_coordinates)
        self.main_window.bottom_view.laybeling.setting_label.list_lbl_view.add_label(new_rectangle_coordinates)

    def delete_a_area(self):
        print("delete area")
        index = self.get_index_label_in_list_info_label_by_coordinate()
        self.list_info_label.remove(self.list_info_label[index])
        self.delete_a_label(index)
        self.top_left = QPoint()
        self.bottom_right = QPoint()
        self.update()

    def delete_all_area(self):
        print("delete all area")
        self.delete_all_label()
        self.list_info_label = []
        self.setup_color_begin()
        self.check_in_rectangle = CURSOR_ON_RECT_
        self.top_left, self.bottom_right = QPoint(), QPoint()
        self.update()

    def check_limit(self):
        self.check_limit_point(self.top_left)
        self.check_limit_point(self.bottom_right)
        if self.check_in_rectangle == CURSOR_ON_RECT_IN_LIST:
            self.edit_coor_a_rectangle_selected_in_list()

    def check_limit_point(self, point: QPoint):
        self.check_limit_x(point)
        self.check_limit_y(point)

    def check_limit_x(self, point: QPoint):
        if point.x() <= 0:
            point.setX(0)
        if point.x() >= self.width():
            point.setX(self.width())
        return point

    def check_limit_y(self, point: QPoint):
        if point.y() <= 0:
            point.setY(0)
        if point.y() >= self.height():
            point.setY(self.height())
        return point

    def correct_point(self):
        x_min, x_max = sorted(list((self.top_left.x(), self.bottom_right.x())))
        y_min, y_max = sorted(list((self.top_left.y(), self.bottom_right.y())))
        self.top_left = QPoint(x_min, y_min)
        self.bottom_right = QPoint(x_max, y_max)

    def print_coordinates(self):
        # print(f"topL: {self.top_left.x()}-{self.top_left.y()}")
        # print(f"topR: {self.top_right.x()}-{self.top_right.y()}")
        # print(f"BottomL: {self.bottom_left.x()}-{self.bottom_left.y()}")
        # print(f"BottomR: {self.bottom_right.x()}-{self.bottom_right.y()}")
        print(f"{self.top_left.x()}, {self.top_left.y()}, {self.bottom_right.x()}, {self.bottom_right.y()}")

    def convert_two_qpoint_to_tuple(self, point: QPoint, point2: QPoint):
        coordinate = (point.x(), point.y(), point2.x(), point2.y())
        return coordinate

    def convert_tuple_qpoint_to_tuple_scale(self, tuple_qpoint_coordinate: tuple):
        list_coordinate = list(tuple_qpoint_coordinate)
        try:
            list_coordinate_scale = [
                list_coordinate[0] / self.width_pixel_view, list_coordinate[1] / self.height_pixel_view,
                list_coordinate[2] / self.width_pixel_view, list_coordinate[3] / self.height_pixel_view
            ]
        except:
            return
        return tuple(list_coordinate_scale)

    def convert_tuple_scale_to_tuple_qpoint(self, tuple_coordinate_scale: tuple):
        list_coordinate = list(tuple_coordinate_scale)
        list_corr = list_coordinate.copy()
        try:
            tuple_coordinate_qpoint = (
                int(list_corr[0] * self.width_pixel_view), int(list_corr[1] * self.height_pixel_view),
                int(list_corr[2] * self.width_pixel_view), int(list_corr[3] * self.height_pixel_view)
            )
        except:
            return
        # self.top_left, self.bottom_right = self.convert_tuple_to_two_qpoint(tuple_coordinate_current)
        return tuple_coordinate_qpoint

    def convert_tuple_to_two_qpoint(self, tuple):
        coordinate = tuple
        top_left = QPoint(coordinate[0], coordinate[1])
        bottom_right = QPoint(coordinate[2], coordinate[3])
        return top_left, bottom_right

    def correct_point_for_list_rectangle(self, tuple_point):
        x_min, x_max = sorted(list((tuple_point[0], tuple_point[2])))
        y_min, y_max = sorted(list((tuple_point[1], tuple_point[3])))
        return (x_min, y_min, x_max, y_max)

    def edit_coor_a_rectangle_selected_in_list(self):
        index = self.get_index_label_in_list_info_label_by_coordinate()
        coordinate = self.convert_two_qpoint_to_tuple(self.top_left, self.bottom_right)
        correct_coordinate = self.correct_point_for_list_rectangle(coordinate)

        correct_coordinate_scale = self.convert_tuple_qpoint_to_tuple_scale(tuple_qpoint_coordinate=correct_coordinate)
        self.list_info_label[index][2] = correct_coordinate_scale
        self.current_click_a_rectangle_selected_in_list = correct_coordinate

    def get_index_label_in_list_info_label_by_coordinate(self):
        index = None
        acceptable_error = 2
        for index_label, info_label in enumerate(self.list_info_label, 0):
            coordinate_scale = info_label[2]
            coordinate_point = self.convert_tuple_scale_to_tuple_qpoint(tuple_coordinate_scale=coordinate_scale)
            current_point = self.current_click_a_rectangle_selected_in_list
            err = []
            for index_, value in enumerate(coordinate_point, 0):
                err.append(abs(value-current_point[index_]))
            if max(err) <= acceptable_error:
                index = index_label
                break
        return index

    def edit_name_label(self, name_change):
        color_border_change = self.edit_label_window.color_btn.color
        index = self.get_index_label_in_list_info_label_by_coordinate()
        self.list_info_label[index][0] = name_change
        self.list_info_label[index][3] = color_border_change
        print("Successfully edit label in list drawing not in view")
        self.main_window.bottom_view.laybeling.setting_label.update_list_name_label(self.list_info_label, index)

    def delete_a_label(self, index):
        self.main_window.bottom_view.laybeling.setting_label.delete_a_label(index)

    def delete_all_label(self):
        self.main_window.bottom_view.laybeling.setting_label.delete_all_label()

    def update_painter_from_setting_label(self):
        self.khoi_tao()
        self.update()

    def update_show_rectangle_by_current_item_index_selected(self, index_in_list_label_bottom_view):
        coordinate_rectangle_scale = self.list_info_label[index_in_list_label_bottom_view][2]
        coordinate_rectangle_not_scale = self.convert_tuple_scale_to_tuple_qpoint(
            tuple_coordinate_scale=coordinate_rectangle_scale)
        self.top_left, self.bottom_right = self.convert_tuple_to_two_qpoint(coordinate_rectangle_not_scale)
        if self.list_info_label[index_in_list_label_bottom_view][1]:
            self.update()
        else:
            self.khoi_tao()
            self.update()

    def update_set_current_row_show_on_bottom_view(self):
        index_row_label = self.get_index_label_in_list_info_label_by_coordinate()
        if index_row_label is not None:
            self.main_window.bottom_view.laybeling.setting_label.\
                list_lbl_view.show_current_item_selected(index_row_label)

    def load_labels(self, list_info_label):
        self.list_info_label = list_info_label
        for label_info in self.list_info_label:
            self.main_window.bottom_view.laybeling.setting_label.list_lbl_view.add_label(label_info)
            self.top_left, self.top_right = self.convert_tuple_to_two_qpoint(tuple=label_info[2])

        self.check_in_rectangle = CURSOR_ON_RECT_IN_LIST
        self.update()

