import math
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

FREE_STATE = 11         #Trạng thái tự do
BUILDING_SQUARE = 22     #Xây dựng

TOP_LEFT_EDIT = 1     #chỉnh sửa resize 4goc
TOP_RIGHT_EDIT = 2
BOTTOM_LEFT_EDIT = 3
BOTTOM_RIGHT_EDIT = 4
BOTTOM_CENTER_EDIT = 5
MOVE_RECT_EDIT = 6

CURSOR_ON_TOP_LEFT_SIDE = 1    #Con trỏ ở ?
CURSOR_ON_TOP_RIGHT_SIDE = 2
CURSOR_ON_BOTTOM_LEFT_SIDE = 3
CURSOR_ON_BOTTOM_RIGHT_SIDE = 4
CURSOR_ON_BOTTOM_CENTER_SIDE = 5
MOVE_RECT = 6
CURSOR_ON_OUT_SIDE = 7

SUB_LOCATION = 5
BUTTON_SIZE_WID = 10
BUTTON_SIZE_HEI = 10

STEP_ROTATE = 1
saveBegin: QPoint
saveEnd: QPoint


class RectangleProcess(QWidget):
    last_global_pos = None
    top_right: QPoint

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.begin_pos, self.end_pos = QPoint(), QPoint()

        self.saveBegin, self.saveEnd = QPoint(), QPoint()

        self.top_left, self.top_right = QPoint(), QPoint()
        self.bottom_right, self.bottom_left = QPoint(), QPoint()

        self.rota = QPoint()
        self.rota_parameter = 0

        self.state = FREE_STATE
        self.br = QBrush(QColor("transparent"))
        self.br2 = QBrush(QColor("transparent"))
        self.setMouseTracking(True)   #mui ten chinh khoang cach
        self.free_cursor_on_side = 0  #con tro o ben
        self.notPress = True
        # self.drawing_edit = True

        self.coor_a = self.top_left
        self.coor_b = self.top_right
        self.coor_c = self.bottom_left
        self.coor_d = self.bottom_right

        self.move_counter_clockwise = False
        # quy uoc goc rectangle
        #  1         2       a      b
        #  3         4       c      d
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setBrush(self.br)
        self.top_right = QPoint(self.bottom_right.x(), self.top_left.y())
        self.bottom_left = QPoint(self.top_left.x(), self.bottom_right.y())

        x_center = int((self.bottom_right.x() - self.bottom_left.x()) / 2) + self.bottom_left.x()
        self.rota = QPoint(x_center, self.bottom_right.y())

        xCenter = x_center
        yCenter = int((self.bottom_right.y() - self.top_left.y()) / 2) + self.top_left.y()
        qp.translate(xCenter, yCenter)
        qp.rotate(self.rota_parameter)#*math.pi/180)
        qp.translate(-xCenter, -yCenter)
        qp.drawRect(QRect(self.top_left, self.bottom_right))

        rec = QPainter(self)

        rec.setBrush(self.br2)

        rec.drawRect(self.top_left.x() - 5, self.top_left.y() - 5, BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        rec.drawRect(self.top_right.x() - 5, self.top_right.y() - 5, BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        rec.drawRect(self.bottom_right.x() - 5, self.bottom_right.y() - 5, BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        rec.drawRect(self.bottom_left.x() - 5, self.bottom_left.y() - 5, BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        rec.drawRect(self.rota.x(), self.rota.y(), BUTTON_SIZE_WID, BUTTON_SIZE_WID)

        if not self.free_cursor_on_side:
            return

    def cursor_on_side(self, e_pos) -> int:  # con tro o ben
        y1, y2 = sorted([self.top_left.y(), self.bottom_right.y()])
        x1, x2 = sorted([self.top_left.x(), self.bottom_right.x()])
        if y1 <= e_pos.y() <= y2:
            if abs(self.top_left.x() - e_pos.x()) <= SUB_LOCATION and abs(self.top_left.y() - e_pos.y()) <= SUB_LOCATION:
                return CURSOR_ON_TOP_LEFT_SIDE
            elif abs(self.top_right.x() - e_pos.x()) <= SUB_LOCATION and abs(self.top_right.y() - e_pos.y()) <= SUB_LOCATION:
                return CURSOR_ON_TOP_RIGHT_SIDE
            elif abs(self.bottom_left.x() - e_pos.x()) <= SUB_LOCATION and abs(self.bottom_left.y() - e_pos.y()) <= SUB_LOCATION:
                return CURSOR_ON_BOTTOM_LEFT_SIDE
            elif abs(self.bottom_right.x() - e_pos.x()) <= SUB_LOCATION and abs(self.bottom_right.y() - e_pos.y()) <= SUB_LOCATION:
                return CURSOR_ON_BOTTOM_RIGHT_SIDE
            elif abs(self.rota.x() - e_pos.x()) <= SUB_LOCATION and abs(self.rota.y() - e_pos.y()) <= SUB_LOCATION:
                return CURSOR_ON_BOTTOM_CENTER_SIDE
            elif x1 + 2 * SUB_LOCATION <= e_pos.x() <= x2 - 2 * SUB_LOCATION and y1 <= e_pos.y() <= y2 - 3 * SUB_LOCATION:
                return MOVE_RECT
        if not (x1 <= e_pos.x() <= x2 and y1 <= e_pos.y() <= y2):
            return CURSOR_ON_OUT_SIDE
        return 0

    def contextMenuEvent(self, event):
        self.menu = QMenu()
        Act1 = QAction('Add Area', self)
        Act2 = QAction('Show Area', self)
        Act3 = QAction('Del Area', self)
        Act4 = QAction('Del Select Area', self)

        Act4.triggered.connect(self.deleteAdded)
        Act3.triggered.connect(self.delete)
        Act2.triggered.connect(self.Show)
        Act1.triggered.connect(self.Add)
        if self.cursor_on_side(event.pos()) == MOVE_RECT:
            self.menu.addAction(Act1)
            self.menu.addAction(Act3)
            self.menu.popup(QCursor.pos())
        else:
            self.menu.addAction(Act2)
            self.menu.addAction(Act4)
            self.menu.popup(QCursor.pos())

    def Add(self):
        self.saveBegin = self.top_left
        self.saveEnd = self.bottom_right
        print(f"ADD{self.saveBegin} {self.saveEnd}")

    def Show(self):
        self.top_left = self.saveBegin
        self.bottom_right = self.saveEnd
        self.update()
        print(f"SHOW {self.saveBegin} {self.saveEnd}")

    def delete(self):
        print("delete")
        self.br2 = QBrush(QColor("transparent"))
        self.top_left = QPoint()
        self.bottom_right = QPoint()
        self.update()

    def deleteAdded(self):
        self.delete()
        self.saveEnd, self.saveBegin = QPoint(), QPoint()
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        self.br2 = QBrush(QColor("yellow"))
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
            self.state = MOVE_RECT_EDIT

            if not self.notPress:
                self.notPress = True
            else:
                print(event.pos())
                self.notPress = False
        else:
            self.state = BUILDING_SQUARE
            self.top_left = event.pos()
            self.bottom_right = event.pos()
            self.update()

    def apply_event(self, event: QMouseEvent):
        if self.state == BUILDING_SQUARE:
            self.end_pos = event.pos()
            self.bottom_right = event.pos()
        elif self.state == TOP_LEFT_EDIT:
            self.top_left = self.top_left + event.globalPos() - self.last_global_pos
        elif self.state == TOP_RIGHT_EDIT:
            self.bottom_right.setX(self.bottom_right.x() + event.globalPos().x() - self.last_global_pos.x())
            self.top_left.setY(self.top_left.y() + event.globalPos().y() - self.last_global_pos.y())
        elif self.state == BOTTOM_LEFT_EDIT:
            self.top_left.setX(self.top_left.x() + event.globalPos().x() - self.last_global_pos.x())
            self.bottom_right.setY(self.bottom_right.y() + event.globalPos().y() - self.last_global_pos.y())
        elif self.state == BOTTOM_RIGHT_EDIT:
            self.bottom_right = self.bottom_right + event.globalPos() - self.last_global_pos
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
        self.call_calculate_coor()
        self.last_global_pos = event.globalPos()
        self.check_limit()

    def call_calculate_coor(self):
        self.coordinate_rectangleRotate(self.top_left.x(), self.top_left.y(), self.bottom_right.x(),
                                        self.bottom_right.y(), self.rota_parameter)

    def coordinate_rectangleRotate(self, x1, y1, x2, y2, theta): #tính toán tọa độ các đỉnh khi xoay
        theta = (theta%180) *math.pi/180
        dx = int(x2-x1)/2
        dy = int(y2-y1)/2
        self.coor_c.setX(int(-dx * math.cos(theta) - dy * math.sin(theta) +x1+dx))
        self.coor_c.setY(int(-dx * math.sin(theta) + dy * math.cos(theta) +y1+dy))

        self.coor_d.setX(int(dx * math.cos(theta) - dy * math.sin(theta) + x1+dx))   #bottomRight
        self.coor_d.setY(int(dx * math.sin(theta) + dy * math.cos(theta) + y1+dy))

        self.coor_b.setX(int(dx * math.cos(theta) + dy * math.sin(theta) +x1+dx))
        self.coor_b.setY(int(dx * math.sin(theta) - dy * math.cos(theta) +y1+dy))

        self.coor_a.setX(int(-dx * math.cos(theta) + dy * math.sin(theta) + x1+dx))   #topLeft
        self.coor_a.setY(int(-dx * math.sin(theta) - dy * math.cos(theta) + y1+dy))

        if self.move_counter_clockwise:
            tmp1 = self.coor_a
            self.coor_a = self.coor_d
            self.coor_d = tmp1
            tmp1 = self.coor_c
            self.coor_c = self.coor_b
            self.coor_b = tmp1

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.state == FREE_STATE:
            self.top_right = QPoint(self.bottom_right.x(), self.top_left.y())
            self.bottom_left = QPoint(self.top_left.x(), self.bottom_right.y())
            x = int((self.bottom_right.x() - self.bottom_left.x()) / 2) + self.bottom_left.x()
            self.rota = QPoint(x, self.bottom_right.y())
            self.free_cursor_on_side = self.cursor_on_side(event.pos())

            if self.free_cursor_on_side == CURSOR_ON_TOP_LEFT_SIDE or\
                    self.free_cursor_on_side == CURSOR_ON_BOTTOM_RIGHT_SIDE:
                self.setCursor(Qt.SizeFDiagCursor)                              #show icon
            elif self.free_cursor_on_side == CURSOR_ON_TOP_RIGHT_SIDE or\
                    self.free_cursor_on_side == CURSOR_ON_BOTTOM_LEFT_SIDE:
                self.setCursor(Qt.SizeBDiagCursor)
            elif self.free_cursor_on_side == CURSOR_ON_BOTTOM_CENTER_SIDE:
                self.setCursor(Qt.SizeHorCursor)
            elif self.free_cursor_on_side == MOVE_RECT:
                self.setCursor(Qt.SizeAllCursor)
            else:
                self.unsetCursor()
            self.update()
        else:
            self.apply_event(event)
            self.update()
        # print(event.pos())

    def check_limit(self):
        self.check_limit_point(self.top_left)
        self.check_limit_point(self.bottom_right)

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

    def mouseReleaseEvent(self, event):
        self.correct_point()
        self.update()
        self.state = FREE_STATE

    def printDec(self):
        print(f"topL: {self.top_left.x()}-{self.top_left.y()}")
        print(f"topR: {self.top_right.x()}-{self.top_right.y()}")
        print(f"BottomL: {self.bottom_left.x()}-{self.bottom_left.y()}")
        print(f"BottomR: {self.bottom_right.x()}-{self.bottom_right.y()}")


class MainWindow(QMainWindow,):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(300, 200, 950, 620)
        self.setFixedSize(950, 620)
        self.startUIWindow()

    def startUIWindow(self):
        self.Frame = QFrame(parent=self)
        self.Frame.resize(self.width(), self.height())
        self.Frame.move(0, 0)
        self.Frame.setStyleSheet("background: red")

        self.label = QLabel(parent=self.Frame)
        self.label.move(10, 10)
        self.label.resize(self.Frame.width()-20, self.Frame.height()-20)
        self.label.setPixmap(QPixmap("project.jpg"))

        self.setWindowTitle("pythonw")
        self.Window = RectangleProcess()
        self.setCentralWidget(self.Window)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
