from PySide6.QtWidgets import QGraphicsView
from src.core.undo_redo import ChangeColorCommand
from src.core.shapes import Shape

class SelectionTool:
    def __init__(self, canvas):
        self.canvas = canvas

    def apply_color(self, color):
        selected = [i for i in self.canvas.scene().selectedItems() if isinstance(i, Shape)]
        if selected:
            self.canvas.undo_stack.push(ChangeColorCommand(selected, color))

    def mouse_press(self, e): QGraphicsView.mousePressEvent(self.canvas, e)
    def mouse_move(self, e): QGraphicsView.mouseMoveEvent(self.canvas, e)
    def mouse_release(self, e): QGraphicsView.mouseReleaseEvent(self.canvas, e)