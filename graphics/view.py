from PyQt6.QtWidgets import QGraphicsView
from PyQt6.QtGui import QPainter, QUndoStack
from PyQt6.QtCore import Qt

from core.tools import SelectTool
from core.commands import DeleteCommand


class VectorEditor(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.undo_stack = QUndoStack(self)
        self.current_tool = SelectTool()

    def set_tool(self, tool):
        self.current_tool = tool

    def mousePressEvent(self, event):
        if self.current_tool:
            self.current_tool.mousePressEvent(event, self)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if self.current_tool:
            self.current_tool.mouseReleaseEvent(event, self)
        super().mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Delete:
            for item in self.scene().selectedItems():
                self.undo_stack.push(DeleteCommand(self.scene(), item))
