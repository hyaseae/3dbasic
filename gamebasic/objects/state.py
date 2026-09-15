from dataclasses import dataclass, field


@dataclass
class PlayerData:
    name:str = ""


@dataclass
class GameState:
    current_scene_name: str = "HOME"
    player: PlayerData = field(default_factory=PlayerData)
    upgrades: list[str] = field(default_factory=list)
    settings: dict[str, object] = field(default_factory=dict)