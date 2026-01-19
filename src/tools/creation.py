from src.core.shapes import Rectangle, Ellipse
from src.core.undo_redo import CreateCommand

class CreationTool:
    def __init__(self, canvas, stype, color):
        self.canvas, self.stype, self.color = canvas, stype, color
        self.temp = None

    def mouse_press(self, e):
        self.start = self.canvas.mapToScene(e.pos())
        self.temp = Rectangle(self.color) if self.stype == "rect" else Ellipse(self.color)
        self.canvas.scene().addItem(self.temp)

    def mouse_move(self, e):
        if self.temp:
            curr = self.canvas.mapToScene(e.pos())
            self.temp.set_geometry(self.start.x(), self.start.y(), curr.x(), curr.y())

    def mouse_release(self, e):
        if self.temp:
            self.canvas.scene().removeItem(self.temp)
            end = self.canvas.mapToScene(e.pos())
            final = type(self.temp)(self.color)
            final.set_geometry(self.start.x(), self.start.y(), end.x(), end.y())
            self.canvas.undo_stack.push(CreateCommand(self.canvas.scene(), final))
            self.temp = None