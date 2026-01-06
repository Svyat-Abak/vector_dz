import abc
from PyQt6.QtWidgets import QGraphicsItemGroup, QGraphicsItem

from core.serializable import Serializable


class GraphicsCompositeMeta(type(QGraphicsItemGroup), abc.ABCMeta):
    pass


class ShapeGroup(QGraphicsItemGroup, Serializable, metaclass=GraphicsCompositeMeta):
    def __init__(self):
        super().__init__()
        self.setFlags(
            QGraphicsItem.GraphicsItemFlag.ItemIsMovable |
            QGraphicsItem.GraphicsItemFlag.ItemIsSelectable
        )

    def to_dict(self):
        return {
            "type": "group",
            "x": self.x(),
            "y": self.y()
        }
