class DimmerSwitch:
    def __init__(self, label):
        self.label = label

        self.switch_is_on = False
        self.brightness = 0

    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False

    def raise_level(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lower_level(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    def show(self):
        print("Switch is on?", self.switch_is_on)
        print("Brightness is:", self.brightness)


# Create three DimmerSwitch objects
dimmer_switch_1 = DimmerSwitch("Dimmer 1")
print(type(dimmer_switch_1))
print(dimmer_switch_1)
print()

dimmer_switch_2 = DimmerSwitch("Dimmer 2")
print(type(dimmer_switch_2))
print(dimmer_switch_2)
print()

dimmer_switch_3 = DimmerSwitch("Dimmer 3")
print(type(dimmer_switch_3))
print(dimmer_switch_3)
print()

# Internally, all instance variables of an object are kept as name/value pairs in a
# Python dictionary
print("dimmer_switch_1 variables:", vars(dimmer_switch_1))
