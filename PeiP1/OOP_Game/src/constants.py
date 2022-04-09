"Game settings"

from pathlib import Path

MAX_INVENTORY = 11

MAIN_DIR = Path(__file__).parent.parent.absolute()
DATA_DIR = MAIN_DIR / "data"

BASE_HUD_WIDTH = 1937
BASE_HUD_HEIGHT = 196  # Action bar height

HUD_RATIO = BASE_HUD_HEIGHT / BASE_HUD_WIDTH  # HUD height

DEFAULT_TILECOUNT = 1500
DEFAULT_TILESIZE = 32
DEFAULT_UI_SQUARE_SIZE = 64
DEFAULT_ROOMCOUNT = 7

BACKGROUND_COLOR = (60, 25, 60)
