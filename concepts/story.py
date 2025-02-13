class Person:
    def __init__(self, toothbrush, toothpaste):
        self._my_brush = toothbrush
        self.my_paste = toothpaste
        self._my_teeth = "beautiful teeth"

    def brush_teeth(self):
        self._my_brush.prepare(self.my_paste)
        return self._my_brush.brush(self._my_teeth)


class Toothbrush:
    def __init__(self, colour):
        self.colour = colour

    def prepare(self, toothpaste):
        print(f"Applying {toothpaste} to {self}")

    def brush(self, teeth):
        return f"Brushing {teeth}"

    def __str__(self):
        return f"a {self.colour} toothbrush"


class ElectricToothbrush(Toothbrush):
    def __init__(self, colour, rpm):
        super().__init__(colour)
        self.rpm = rpm

    def brush(self, teeth):
        return f"Brushing {teeth} with {self.rpm} RPM!"


if __name__ == "__main__":
    """
    Run this script in the terminal as `python story.py`
    """
    brian = Person(ElectricToothbrush("red", 1000), "some paste")
    print(brian.brush_teeth())
