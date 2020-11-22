class Water:
    def __init__(self, volume, unit= "L"):
        self.volume = volume
        self.unit = unit

    def __str__(self):
        return f"WATER({self.volume}{self.unit}) "

    def __len__(self):
        return self.volume

    def __add__(self, w):
        if self.unit  == "ml":
            self.volume = (self.volume / 1000)
        if w.unit == "ml":
                w.volume = (w.volume / 1000)
        return Water( self.volume + w.volume )

    #def __sub__(self, w):
        if self.unit == "ml":
            self.volume = (self.volume / 1000)
        if w.unit == "ml":
            w.volume = (w.volume / 1000)

        return Water(self.volume - w.volume)

    def __gt__(self, w):
        if self.unit == "ml":
            self.volume = (self.volume / 1000)
        if w.unit == "ml":
            w.volume = (w.volume / 1000)
        return self.volume > w.volume

    def __ge__(self, w):
        if self.unit == "ml":
            self.volume = (self.volume / 1000)
        if w.unit == "ml":
            w.volume = (w.volume / 1000)
        return self.volume >= w.volume

    def __eq__(self, w):
        if self.unit == "ml":
            self.volume = (self.volume / 1000)
        if w.unit == "ml":
            w.volume = (w.volume / 1000)
        return self.volume == w.volume
    def __le__(self, w):
        if self.unit == "ml":
            self.volume = (self.volume / 1000)
        if w.unit == "ml":
            w.volume = (w.volume / 1000)
        return self.volume < w.volume




water1 = Water(6, "ml")
water2 = Water(50, "ml")

if water1 < water2:
    print("second is more")
#water = water1 + water2 + water3

#print(water)