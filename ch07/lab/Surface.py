from Rectangle import Rectangle


class Surface:
    def __init__(self, filename, x=0, y=0, h=0, w=0):
        """
        Initializes Surface Object
        args: filename, x, y, height, width
        """
        self.image = filename
        self.rect = Rectangle(x, y, h, w)

    def getRect(self):
        """
        Returns the rectangle of the surface
        return: Rectangle
        """
        return self.rect
