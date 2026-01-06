from abc import ABC, abstractmethod

from PyQt6.QtWidgets import (
    QGraphicsView,
    QGraphicsRectItem,
    QGraphicsEllipseItem,
    QGraphicsItem
)
from PyQt6.QtGui import QPen, QBrush
from PyQt6.QtCore import Qt, QRectF, QPointF

from core.commands import AddCommand, MoveCommand


class Tool(ABC):
    @abstractmethod
    def mousePressEvent(self, event, view: QGraphicsView):
        pass

    @abstractmethod
    def mouseReleaseEvent(self, event, view: QGraphicsView):
        pass


class SelectTool(Tool):
    def __init__(self):
        self._item = None
        self._start_pos = None

    def mousePressEvent(self, event, view: QGraphicsView):
        self._item = view.itemAt(event.pos())
        if self._item:
            self._start_pos = self._item.pos()

    def mouseReleaseEvent(self, event, view: QGraphicsView):
        if self._item and self._start_pos:
            new_pos = self._item.pos()
            if new_pos != self._start_pos:
                cmd = MoveCommand(self._item, self._start_pos, new_pos)
                view.undo_stack.push(cmd)
        self._item = None
        self._start_pos = None


class CreationTool(Tool):
    def __init__(self, shape: str):
        self.shape = shape

    def mousePressEvent(self, event, view: QGraphicsView):
        scene_pos = view.mapToScene(event.pos())

        if self.shape == "rect":
            item = QGraphicsRectItem(QRectF(0, 0, 80, 50))
        else:
            item = QGraphicsEllipseItem(QRectF(0, 0, 60, 60))

        item.setBrush(QBrush(Qt.GlobalColor.lightGray))
        item.setPen(QPen(Qt.GlobalColor.black))
        item.setFlags(
            QGraphicsItem.GraphicsItemFlag.ItemIsMovable |
            QGraphicsItem.GraphicsItemFlag.ItemIsSelectable
        )
        item.setPos(scene_pos)

        view.undo_stack.push(AddCommand(view.scene(), item))

    def mouseReleaseEvent(self, event, view: QGraphicsView):
        pass
