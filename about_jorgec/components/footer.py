import reflex as rx

from about_jorgec.styles.fonts import FontSize, FontWeight
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
                rx.fragment(
                    "Jorge Vinagre is a Certified",
                    rx.link(
                        " SAFe ",
                        href="https://scaledagileframework.com/",
                        is_external=True,
                        font_weight=FontWeight.MEDIUM,
                    ),
                    "® 6 Practitioner.",
                ),
                font_size=FontSize.SMALL.value
            ),
        padding=Size.BIG.value,
        align="center",
        bottom="0"
    )