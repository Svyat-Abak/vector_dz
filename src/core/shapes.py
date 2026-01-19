from __future__ import annotations
from PySide6.QtWidgets import QGraphicsPathItem, QGraphicsItem
from PySide6.QtGui import QPainterPath, QColor, QPen, QBrush
from PySide6.QtCore import Qt


class Shape(QGraphicsPathItem):
    def __init__(self, color_name="black"):
        super().__init__()
        self._color_name = color_name
        self.setPen(QPen(QColor("black"), 2))
        self.update_color(color_name)

        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.rect_data = (0, 0, 0, 0)

    def update_color(self, color_name):
        self._color_name = color_name
        self.setBrush(QBrush(QColor(color_name)))

    def to_dict(self):
        p = self.pos()
        return {
            "type": self.__class__.__name__,
            "x": self.rect_data[0] + p.x(),
            "y": self.rect_data[1] + p.y(),
            "w": self.rect_data[2],
            "h": self.rect_data[3],
            "color": self._color_name
        }


class RectangularShape(Shape):
    def set_geometry(self, x1, y1, x2, y2):
        x, y, w, h = min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2)
        self.rect_data = (x, y, w, h)
        path = QPainterPath()
        self.draw_path(path, x, y, w, h)
        self.setPath(path)


class Rectangle(RectangularShape):
    def draw_path(self, path, x, y, w, h): path.addRect(x, y, w, h)


class Ellipse(RectangularShape):
    def draw_path(self, path, x, y, w, h): path.addEllipse(x, y, w, h)