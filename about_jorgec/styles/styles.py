import reflex as rx

from about_jorgec.styles.colors import Color
from about_jorgec.styles.fonts import Font, FontWeight, FontSize
from enum import Enum


class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    "font_weight": FontWeight.LIGHT.value,
    rx.heading: {
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
        "font_size": FontSize.BIG.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
    },
    rx.link: {
        "color": Color.MY_BLUE,
        "text_decoration": "none",
        "_hover": {}
    },
    rx.mobile_and_tablet: {
        "width": "90%"
    }
}