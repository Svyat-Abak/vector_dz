from PySide6.QtWidgets import QToolBar, QColorDialog
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal

class ToolPanel(QToolBar):
    color_selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__("Панель", parent)
        pal_act = QAction("Выбрать цвет...", self)
        pal_act.triggered.connect(self._open_palette)
        self.addAction(pal_act)
        self.addSeparator()

    def _open_palette(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_selected.emit(color.name())