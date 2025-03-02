class LightSwitch:
    def __init__(self):
        self.switch_is_on = False

    def turn_on(self):
        # Turn the switch on
        self.switch_is_on = True

    def turn_off(self):
        # Turn the switch off
        self.switch_is_on = False

    def show(self):
        # Added for testing
        print(self.switch_is_on)


# Main code
light_switch_1 = LightSwitch()
light_switch_2 = LightSwitch()

# Test code
light_switch_1.show()
light_switch_2.show()

light_switch_1.turn_on()
light_switch_2.turn_off()

light_switch_1.show()
light_switch_2.show()

print(type(light_switch_1))
