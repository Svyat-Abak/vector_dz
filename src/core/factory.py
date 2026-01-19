import logging
from .shapes import Rectangle, Ellipse

class ShapeFactory:
    @staticmethod
    def create(stype, x, y, w, h, color):
        try:
            shape = Rectangle(color) if stype == "Rectangle" else Ellipse(color)
            shape.set_geometry(x, y, x+w, y+h)
            return shape
        except Exception as e:
            logging.error(f"Ошибка Фабрики: {e}")
            return None