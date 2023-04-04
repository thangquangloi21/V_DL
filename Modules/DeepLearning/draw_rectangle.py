from PyQt5.QtCore import *
from PyQt5.QtGui import *

BUTTON_SIZE_WID = 7
BUTTON_SIZE_HEI = 7


class ColorDrawing:
    color_transparent = QColor("transparent")
    color_green = QColor(0, 255, 0)
    color_yellow = QColor("yellow")


class DrawRectangle:
    def __init__(self, parent, pen, background, point1, point2):
        draw_rectangle = QPainter(parent)
        draw_rectangle.setPen(QPen(pen, 3))
        draw_rectangle.setBrush(background)
        draw_rectangle.drawRect(QRect(point1, point2))


class ListRectange:
    def __init__(self):
        self.yellow = QBrush(QColor("yellow"))

    def show_all_rectangle(self, list_rectangle):
        for index_rec in list_rectangle:
            DrawRectangle(self.yellow, index_rec[0], index_rec[1])


class DrawCorner:
    def __init__(self, parent, pen, background, l_top, l_bottom, r_top, r_bottom, rotate):
        self.parent = parent
        self.pen = pen
        self.background = background
        self.l_top = l_top
        self.l_bottom = l_bottom
        self.r_top = r_top
        self.r_bottom = r_bottom
        self.rotate = rotate
        self.draw_corner()

    def draw_corner(self):
        draw_4_corner = QPainter(self.parent)
        draw_4_corner.setPen(QPen(self.pen, 3))
        draw_4_corner.setBrush(self.background)
        draw_4_corner.drawEllipse(QPoint(self.l_top.x(), self.l_top.y()), BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        draw_4_corner.drawEllipse(QPoint(self.r_top.x(), self.r_top.y()), BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        draw_4_corner.drawEllipse(QPoint(self.r_bottom.x(), self.r_bottom.y()), BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        draw_4_corner.drawEllipse(QPoint(self.l_bottom.x(), self.l_bottom.y()), BUTTON_SIZE_WID, BUTTON_SIZE_WID)
        # draw_4_corner.drawRect(self.rotate.x(), self.rotate.y(), BUTTON_SIZE_WID, BUTTON_SIZE_WID)

