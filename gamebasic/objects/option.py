from dataclasses import dataclass, field


@dataclass
class OptionData:
    screen_width: int = 800
    screen_height: int = 600
    debug:bool = True
    FPS: int = 60