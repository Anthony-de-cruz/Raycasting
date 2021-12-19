from dataclasses import dataclass

# todo To be stored and read from an ini file
@dataclass
class Settings:

    """Class for keeping track of settings"""

    window_name: str
    window_width: int
    window_height: int
    fps: int


SETTINGS = Settings("Raycasting", 1000, 500, 60)
