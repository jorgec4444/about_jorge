import reflex as rx
import about_jorgec.constants as const

from about_jorgec.components.link_icon import link_icon


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/avatar.png",
                fallback="JV",
                size="8",
                radius="full",
                border=f"2px solid"
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
                    padding_top="0.5em"
                ),
                padding_left="0.5em",
                width="100%"
            ),
            justify="between"
        ),
        rx.vstack(
            rx.text(
                """
                I´m a passionate software engineer from Barcelona that loves programming and learning new stuff everyday.
                Here you can find out more about me, welcome!
                """,
                text_align="start",
                width="50%"
            ),
            align="center"
        ),
        align_items="center",
        width="100%",
        spacing="6"
    )