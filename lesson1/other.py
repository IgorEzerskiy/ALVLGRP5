class DummyClass:
    pass


class Rectangle:
    height = 5
    width = 15

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    dummy_object = DummyClass()
    print(dir(dummy_object))

    rect = Rectangle(1, 2)
    rect2 = Rectangle(1, 5)

    rect.something_else = 'kekeke'
    print(rect.area())
    print(rect.something_else)
