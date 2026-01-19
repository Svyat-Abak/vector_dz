from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QAction
from .canvas import EditorCanvas
from .widgets import ToolPanel
from src.tools.creation import CreationTool
from src.tools.selection import SelectionTool


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.color = "#000000"
        self.canvas = EditorCanvas()
        self._setup_ui()

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.toolbar = ToolPanel(self)
        self.toolbar.color_selected.connect(self._handle_color_change)
        self.addToolBar(self.toolbar)

        act_move = QAction("Выделение", self)
        act_move.triggered.connect(lambda: self._set_tool("move"))
        self.toolbar.addAction(act_move)

        for n, t in [("Квадрат", "rect"), ("Круг", "circle")]:
            a = QAction(n, self)
            a.triggered.connect(lambda chk=False, st=t: self._set_tool(st))
            self.toolbar.addAction(a)

        self.toolbar.addSeparator()
        act_group = QAction("Сгруппировать", self)
        act_group.triggered.connect(self.canvas.group_selected)
        self.toolbar.addAction(act_group)

        layout.addWidget(self.canvas)

    def _handle_color_change(self, c):
        self.color = c
        if isinstance(self.canvas.current_tool, SelectionTool):
            self.canvas.current_tool.apply_color(c)

    def _set_tool(self, t):
        if t == "move":
            self.canvas.current_tool = SelectionTool(self.canvas)
        else:
            self.canvas.current_tool = CreationTool(self.canvas, t, self.color)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())