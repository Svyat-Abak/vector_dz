from PyQt6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QColorDialog,
    QGraphicsScene
)
from PyQt6.QtGui import QAction, QColor
from PyQt6.QtCore import Qt

from graphics.view import VectorEditor
from core.tools import SelectTool, CreationTool
from core.commands import ChangeColorCommand, GroupCommand


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vector Editor")

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 800, 600)

        self.view = VectorEditor(self.scene)
        self.setCentralWidget(self.view)

        self._create_toolbar()

    def _create_toolbar(self):
        toolbar = QToolBar("Tools")
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)

        select_action = QAction("Select", self)
        rect_action = QAction("Rectangle", self)
        ellipse_action = QAction("Ellipse", self)
        color_action = QAction("Color", self)
        group_action = QAction("Group", self)

        select_action.triggered.connect(
            lambda: self.view.set_tool(SelectTool())
        )
        rect_action.triggered.connect(
            lambda: self.view.set_tool(CreationTool("rect"))
        )
        ellipse_action.triggered.connect(
            lambda: self.view.set_tool(CreationTool("ellipse"))
        )
        color_action.triggered.connect(self.change_color)
        group_action.triggered.connect(self.group_items)

        toolbar.addAction(select_action)
        toolbar.addAction(rect_action)
        toolbar.addAction(ellipse_action)
        toolbar.addAction(color_action)
        toolbar.addAction(group_action)

    def change_color(self):
        color = QColorDialog.getColor()
        if not color.isValid():
            return

        for item in self.scene.selectedItems():
            self.view.undo_stack.push(
                ChangeColorCommand(item, color)
            )

    def group_items(self):
        items = self.scene.selectedItems()
        if len(items) > 1:
            self.view.undo_stack.push(
                GroupCommand(self.scene, items)
            )
