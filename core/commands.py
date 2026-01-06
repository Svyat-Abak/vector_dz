from PyQt6.QtWidgets import (
    QGraphicsScene,
    QGraphicsItem
)
from PyQt6.QtGui import QUndoCommand, QBrush, QColor
from PyQt6.QtCore import QPointF

from graphics.group import ShapeGroup


class AddCommand(QUndoCommand):
    def __init__(self, scene: QGraphicsScene, item: QGraphicsItem):
        super().__init__("Add item")
        self.scene = scene
        self.item = item

    def redo(self):
        self.scene.addItem(self.item)

    def undo(self):
        self.scene.removeItem(self.item)


class DeleteCommand(QUndoCommand):
    def __init__(self, scene: QGraphicsScene, item: QGraphicsItem):
        super().__init__("Delete item")
        self.scene = scene
        self.item = item

    def redo(self):
        self.scene.removeItem(self.item)

    def undo(self):
        self.scene.addItem(self.item)


class MoveCommand(QUndoCommand):
    def __init__(self, item: QGraphicsItem, old_pos: QPointF, new_pos: QPointF):
        super().__init__("Move item")
        self.item = item
        self.old_pos = old_pos
        self.new_pos = new_pos

    def redo(self):
        self.item.setPos(self.new_pos)

    def undo(self):
        self.item.setPos(self.old_pos)


class GroupCommand(QUndoCommand):
    def __init__(self, scene: QGraphicsScene, items: list[QGraphicsItem]):
        super().__init__("Group items")
        self.scene = scene
        self.items = items
        self.group = ShapeGroup()

    def redo(self):
        for item in self.items:
            self.group.addToGroup(item)
        self.scene.addItem(self.group)

    def undo(self):
        for item in self.items:
            self.group.removeFromGroup(item)
            self.scene.addItem(item)
        self.scene.removeItem(self.group)


class ChangeColorCommand(QUndoCommand):
    def __init__(self, item: QGraphicsItem, color: QColor):
        super().__init__("Change color")
        self.item = item
        self.old_brush = item.brush()
        self.new_brush = QBrush(color)

    def redo(self):
        self.item.setBrush(self.new_brush)

    def undo(self):
        self.item.setBrush(self.old_brush)
