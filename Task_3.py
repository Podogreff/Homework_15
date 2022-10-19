
class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.default_channel = CHANNELS[0]

    def first_channel(self):
        self.default_channel = CHANNELS[0]
        return CHANNELS[0]

    def last_channel(self):
        self.default_channel = CHANNELS[-1]
        return CHANNELS[-1]

    def turn_channel(self, number):
        if 0 < number < 4:
            self.default_channel = CHANNELS[number-1]
            return CHANNELS[number-1]
        else:
            return "ERROR! Please enter the number between 1 - 3"

    def next_channel(self):
        if self.default_channel == CHANNELS[0]:
            self.default_channel = CHANNELS[1]
            return self.default_channel
        elif self.default_channel == CHANNELS[1]:
            self.default_channel = CHANNELS[2]
            return self.default_channel
        else:
            self.default_channel = CHANNELS[0]
            return self.default_channel

    def previous_channel(self):
        if self.default_channel == CHANNELS[0]:
            self.default_channel = CHANNELS[2]
            return self.default_channel
        elif self.default_channel == CHANNELS[1]:
            self.default_channel = CHANNELS[0]
            return self.default_channel
        else:
            self.default_channel = CHANNELS[1]
            return self.default_channel

    def current_channel(self):
        return self.default_channel

    def is_exist(self, name):
        if isinstance(name, int) and 0 < name < 3 or name in self.channels:
            return "YEAH!"
        else:
            return "NOPE!"


CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
