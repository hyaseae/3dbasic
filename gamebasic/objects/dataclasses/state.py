from dataclasses import dataclass, field


@dataclass
class PlayerData:
    name:str = ""


@dataclass
class GameState:
    current_scene_name: str = "HOME"
    save_file_name: str = "save01"
    player: PlayerData = field(default_factory=PlayerData)
    upgrades: list[str] = field(default_factory=list)