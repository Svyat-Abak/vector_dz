from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItemGroup
from PySide6.QtGui import QPainter, QUndoStack
from src.core.undo_redo import GroupCommand


class EditorCanvas(QGraphicsView):
    def __init__(self):
        super().__init__()
        self._scene = QGraphicsScene()
        self.setScene(self._scene)
        self.undo_stack = QUndoStack(self)
        self.setRenderHint(QPainter.Antialiasing)
        self.current_tool = None

    def group_selected(self):
        items = self._scene.selectedItems()
        if len(items) < 2: return

        group = QGraphicsItemGroup()
        self._scene.addItem(group)
        for item in items:
            group.addToGroup(item)

        self.undo_stack.push(GroupCommand(self._scene, group))

    def mousePressEvent(self, e):
        if self.current_tool: self.current_tool.mouse_press(e)
        super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if self.current_tool: self.current_tool.mouse_move(e)
        super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        if self.current_tool: self.current_tool.mouse_release(e)
        super().mouseReleaseEvent(e)