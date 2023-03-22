from dino_runner.utils.constants import DEFAULT_TYPE, HEART
from dino_runner.components.power_ups.power_up import PowerUp


class Heart(PowerUp):
    def __init__(self):
        self.image = HEART
        self.type = DEFAULT_TYPE
        super().__init__(self.image, self.type)
