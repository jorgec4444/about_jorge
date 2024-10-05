import reflex as rx

from about_jorgec.styles.colors import TextColor, Color
from about_jorgec.styles.styles import Size


def check(heading):
    return heading == "Curriculum Vitae"


class CvSectionState(rx.State):
    isCvHeader: bool = False


def cv_section(heading: str, text: str, href:str) -> rx.Component:
    return rx.cond(
        check(heading),
        rx.section(
            rx.heading(
                heading,
                padding_bottom=Size.SMALL.value,
            ),
            rx.text(
                rx.fragment(
                    "Here you can find my detailed work experience in different companies with a brief summary of my "
                    "role in each of them. However you can always ",
                    rx.link(
                        "download my CV in .pdf format ",
                        href="https://drive.google.com/file/d/1RoY-7AArT1ms_EStbHklRMeBc12jtvj0/view?usp=sharing",
                        is_external=True,
                    ),
                    "and have a look."
                ),
                text_align="start",
                color=TextColor.BODY.value
            )
        ),
        rx.section(
            rx.heading(
                rx.link(
                    heading,
                    href=href,
                    is_external=True
                ),
                padding_bottom=Size.SMALL.value
            ),
            rx.text(
                text,
                text_align="start",
                color=TextColor.BODY.value
            ),
            padding=Size.LARGE.value,
            border="2.7px solid",
            border_radius="15px",
            border_color=Color.BORDER,
            margin_bottom=Size.BIG.value
        ),
    )