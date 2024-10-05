import reflex as rx

from about_jorgec.styles.colors import TextColor
from about_jorgec.styles.fonts import FontSize
from about_jorgec.styles.styles import Size

def footer() -> rx.Component:
    return rx.vstack(
            rx.image(
                src="/safe_icon.png",
                height="7em",
                width="6em",
                alt="Safe icon certificate"
            ),
            rx.text(
                "Jorge Vinagre is a Certified SAFe® 6 Practitioner.",
                font_size=FontSize.SMALL.value
            ),
        padding=Size.BIG.value,
        align="center",
        bottom="0"
    )