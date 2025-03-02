class TV:
    def __init__(self, brand, location):
        self.brand = brand
        self.location = location

        self.is_on = False
        self.is_muted = False

        # Default list of channels
        self.channel_list = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.n_channels = len(self.channel_list)
        self.channel_index = 0

        self.VOLUME_MINIMUM = 0  # Constant
        self.VOLUME_MAXIMUM = 10  # Constant
        self.volume = self.VOLUME_MAXIMUM // 2  # Integer divide

    def power(self):
        self.is_on = not self.is_on  # Toggle

    def volume_up(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False  # Changing the volume while muted unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volume_down(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False  # Changing the volume while muted unmutes the sound
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channel_up(self):
        if not self.is_on:
            return
        self.channel_index = self.channel_index + 1
        if self.channel_index > self.n_channels:
            self.channel_index = 0  # Wrap around to the first channel

    def channel_down(self):
        if not self.is_on:
            return
        self.channel_index = self.channel_index - 1
        if self.channel_index < 0:
            self.channel_index = self.n_channels - 1  # Wrap around to the first channel

    def mute(self):
        if not self.is_on:
            return
        self.is_muted = not self.is_muted

    def set_channel(self, new_channel):
        if new_channel in self.channel_list:
            self.channel_index = self.channel_list.index(new_channel)
        # If the new_channel is not in our list of channels, don't do anything

    def show_info(self):
        print()
        print("Status of TV:", self.brand)
        print("    Location:", self.location)
        if self.is_on:
            print("    TV is: On")
            print("    Channel is:", self.channel_list[self.channel_index])
            if self.is_muted:
                print("    Volume is:", self.volume, "(sound is muted)")
            else:
                print("    Volume is:", self.volume)
        else:
            print("    TV is: Off")


# Main code
tv_1 = TV("Samsung", "Family room")
tv_2 = TV("Sony", "Bedroom")

# Turn both TVs on
tv_1.power()
tv_2.power()

# Raise the volume of TV 1
tv_1.volume_up()
tv_1.volume_up()

# Raise the volume of TV 2
tv_2.volume_up()
tv_2.volume_up()
tv_2.volume_up()
tv_2.volume_up()
tv_2.volume_up()

# Change TV2's channel, then mute it”
tv_2.set_channel(44)
tv_2.mute()

tv_1.show_info()
tv_2.show_info()
