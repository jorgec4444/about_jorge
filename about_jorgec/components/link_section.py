import reflex as rx

from about_jorgec.styles.colors import Color
from about_jorgec.styles.styles import Size

def link_section(heading: str, text: str, href:str, ) -> rx.Component:
    return rx.section(
        rx.heading(
            rx.link(
                heading,
                href=href,
                is_external=True
            ),
            padding_bottom=Size.SMALL.value
        ),
        text,
        padding=Size.LARGE.value,
        border="2.7px solid",
        border_radius="15px",
        border_color=Color.MY_BLUE,
        margin_bottom=Size.BIG.value
    )