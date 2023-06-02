from dino_runner.utils.constants import TIME, TIME_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Time(PowerUp):
    def __init__(self):
        self.image = TIME
        self.type = TIME_TYPE
        super().__init__(self.image, self.type)