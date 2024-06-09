class FontManager:
    def __init__(self, font="Arial", size=10, weight="normal", color="black"):
        self.font = font
        self.size = size
        self.weight = weight
        self.color = color

    def get_font(self):
        return self.font, self.size, self.weight

    def get_color(self):
        return self.color

    def set_font(self, font, size, weight):
        self.font = font
        self.size = size
        self.weight = weight

    def set_color(self, color):
        self.color = color
