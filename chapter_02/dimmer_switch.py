class DimmerSwitch:
    def __init__(self):
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


# Main code
dimmer_switch = DimmerSwitch()

# Turn switch on, and raise the level 5 times
dimmer_switch.turn_on()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.show()

# Lower the level 2 times, and turn switch off
dimmer_switch.lower_level()
dimmer_switch.lower_level()
dimmer_switch.turn_off()
dimmer_switch.show()

# Turn switch on, and raise the level 3 times
dimmer_switch.turn_on()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.show()
