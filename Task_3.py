
class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.default_channel = CHANNELS[0]

    def first_channel(self):
        self.default_channel = CHANNELS[0]
        print(CHANNELS[0])

    def last_channel(self):
        self.default_channel = CHANNELS[-1]
        print(CHANNELS[-1])

    def turn_channel(self, number):
        self.default_channel = CHANNELS[number-1]
        print(CHANNELS[number-1])

    def next_channel(self):
        if self.default_channel == CHANNELS[0]:
            self.default_channel = CHANNELS[1]
            print(self.default_channel)
        elif self.default_channel == CHANNELS[1]:
            self.default_channel = CHANNELS[2]
            print(self.default_channel)
        else:
            self.default_channel = CHANNELS[0]
            print(self.default_channel)

    def previous_channel(self):
        if self.default_channel == CHANNELS[0]:
            self.default_channel = CHANNELS[2]
            print(self.default_channel)
        elif self.default_channel == CHANNELS[1]:
            self.default_channel = CHANNELS[0]
            print(self.default_channel)
        else:
            self.default_channel = CHANNELS[1]
            print(self.default_channel)

    def current_channel(self):
        print(self.default_channel)

    def is_exist(self, name):
        if isinstance(name, int) and 0 < name < 3 or name in CHANNELS:
            print("YEAH!")
        else:
            print("NOPE!")


CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist(4)
controller.is_exist("BBC")
