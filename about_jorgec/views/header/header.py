import reflex as rx
import about_jorgec.constants as const

from about_jorgec.components.link_icon import link_icon
from about_jorgec.styles.colors import Color, TextColor
from about_jorgec.styles.styles import Size


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/avatar.png",
                fallback="JV",
                size="8",
                radius="full",
                border="2.7px solid",
                border_color=Color.BORDER.value
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
                    padding_top=Size.SMALL.value
                ),
                padding_left=Size.SMALL.value,
                width="100%"
            ),
            justify="between"
        ),
        rx.desktop_only(
                rx.vstack(
                rx.center(
                    rx.text(
                        """
                        I´m a software engineer from Barcelona that loves programming and learning new stuff everyday.
                        Here you can find out more about me, welcome!
                        """,
                        text_align="start",
                        color=TextColor.BODY.value
                    ),
                    border="2.7px solid",
                    border_radius="15px",
                    border_color=Color.BORDER,
                    padding=Size.LARGE.value,
                    align="center",
                    width="50%"
                ),
                align="center",
                padding=Size.DEFAULT.value
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.center(
                    rx.text(
                        """
                        I´m a software engineer from Barcelona that loves programming and learning new stuff everyday.
                        Here you can find out more about me, welcome!
                        """,
                        text_align="start",
                        color=TextColor.BODY.value
                    ),
                    border="2.7px solid",
                    border_radius="15px",
                    border_color=Color.BORDER,
                    padding=Size.LARGE.value,
                    align="center"
                ),
                align="center",
                padding=Size.DEFAULT.value
            )
        ),
        align_items="center",
        width="100%",
        spacing="6",
        margin_top="4em"
    )
