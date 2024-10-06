import reflex as rx
import about_jorgec.constants as const
import datetime

from about_jorgec.components.link_icon import link_icon
from about_jorgec.styles.colors import Color, TextColor
from about_jorgec.styles.fonts import FontSize
from about_jorgec.styles.styles import Size

def experience() -> str:
    years = str(datetime.date.today().year - 2022)

    return years +"+"

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/avatar.png",
                fallback="JV",
                size="8",
                radius="full",
                border="2.7px solid",
                border_color=Color.MY_BLUE.value
            ),
            rx.vstack(
                rx.heading(
                    "Jorge Vinagre",
                    size="6"
                ),
                rx.text("@jorgec4444"),
                rx.hstack(
                    link_icon("/github.svg", const.GITHUB_URL, "Github"),
                    link_icon("/linkedin.svg", const.LINKEDIN_URL, "Linkedin"),
                    link_icon("/email.svg", "mailto:vinagre444@gmail.com", "Email"),
                    link_icon("/instagram.svg", "https://www.instagram.com/jorgitocvt4/", "Instagram"),
                    padding_top=Size.SMALL.value
                ),
                padding_left=Size.SMALL.value,
                width="100%"
            )
        ),
        rx.vstack(
            rx.box(
                rx.text(
                    f"{experience()}",
                    as_="span",
                    font_weight="bold",
                    color=Color.MY_BLUE
                ),
                " years of experience",
                font_size=Size.DEFAULT.value,
                color=TextColor.BODY.value
            )
        ),
        rx.desktop_only(
                rx.vstack(
                rx.center(
                    rx.text(
                        """
                        I´m a software engineer from Badalona that loves programming and learning new stuff everyday.
                        Here you can find out more about me, welcome!
                        """,
                        text_align="start",
                        color=TextColor.BODY.value
                    ),
                    border="2.7px solid",
                    border_radius="15px",
                    border_color=Color.MY_BLUE,
                    padding=Size.LARGE.value,
                    align="center",
                    width="50%"
                ),
                align="center",
                padding=Size.DEFAULT.value,
                font_size=FontSize.DEFAULT.value
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.center(
                    rx.text(
                        """
                        I´m a software engineer from Badalona that loves programming and learning new stuff everyday.
                        Here you can find out more about me, welcome!
                        """,
                        text_align="start",
                        color=TextColor.BODY.value
                    ),
                    border="2.7px solid",
                    border_radius="15px",
                    border_color=Color.MY_BLUE,
                    padding=Size.LARGE.value,
                    align="center"
                ),
                align="center",
                padding=Size.DEFAULT.value,
                font_size=FontSize.DEFAULT.value
            )
        ),
        align_items="center",
        width="100%",
        spacing="5",
        margin_top="3em"
    )
