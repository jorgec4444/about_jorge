from enum import Enum


class Font(Enum):
    DEFAULT = "Poppins, sans-serif"
    TITLE = "Montserrat', sans-serif"
    LOGO = "Montserrat', sans-serif"

class FontSize(Enum):
    SMALL = "0.8em"
    DEFAULT = "1.1em"
    MEDIUM = "1.3em"
    BIG = "1.5em"
    VERY_BIG = "3em"

class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "550"