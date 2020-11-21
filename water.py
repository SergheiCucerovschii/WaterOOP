class Water:
    def __init__(self, volume, unit= "L"):
        self.volume = volume
        self.unit = unit

    def __str__(self):
        return f"WATER({self.volume}{self.unit}) "

    def __len__(self):
        return self.volume

    def __add__(self, w):
        if w.unit == "ml":
            w.volume = (w.volume / 1000)
        return Water( self.volume + w.volume )

    def __sub__(self, w):
        if w.unit == "ml":
            w.volume = (w.volume / 1000)
        return Water(self.volume - w.volume)

    def __gt__(self, w):
        return self.volume > w.volume

    def __ge__(self, other):
        pass




water1 = Water(2, "L")
water2 = Water(300, "ml")
water3 = Water(500, "ml")

water = water1 + water2 + water3

print(water)