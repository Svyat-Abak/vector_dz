from PySide6.QtGui import QUndoCommand
from PySide6.QtWidgets import QGraphicsItem

class CreateCommand(QUndoCommand):
    def __init__(self, scene, shape):
        super().__init__("Создать")
        self.scene, self.shape = scene, shape
    def redo(self): self.scene.addItem(self.shape)
    def undo(self): self.scene.removeItem(self.shape)

class ChangeColorCommand(QUndoCommand):
    def __init__(self, items, new_color):
        super().__init__("Изменить цвет")
        self.items = items
        self.new_color = new_color
        self.old_colors = [item._color_name for item in items]

    def redo(self):
        for item in self.items: item.update_color(self.new_color)

    def undo(self):
        for item, old_color in zip(self.items, self.old_colors):
            item.update_color(old_color)

class GroupCommand(QUndoCommand):
    def __init__(self, scene, group):
        super().__init__("Группировка")
        self.scene, self.group = scene, group
        self.items = group.childItems()
    def redo(self):
        self.scene.addItem(self.group)
        self.group.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
    def undo(self):
        for item in self.items:
            self.group.removeFromGroup(item)
            self.scene.addItem(item)
        self.scene.removeItem(self.group)