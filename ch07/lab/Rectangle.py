class Rectangle:
    def __init__(self, x=0, y=0, h=0, w=0):
        """
        Initializes Rectangle object
        args: x, y, height, width
        """
        self.x = max(0, x)
        self.y = max(0, y)
        self.height = max(0, h)
        self.width = max(0, w)

    def __str__(self):
        """
        Replaces the default str method and returns all variables values of the object
        args: self
        return: str
        """
        return f"(x:{self.x}, y:{self.y}, height:{self.height}, width:{self.width})"
