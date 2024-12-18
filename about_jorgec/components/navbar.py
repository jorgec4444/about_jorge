import reflex as rx

from about_jorgec.styles.colors import Color
from about_jorgec.styles.styles import Size
def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"),
        href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(
                    rx.heading(
                        "jorgec4444", size="6", weight="bold"
                    ),
                    href="/"
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", "/about"),
                    navbar_link("CV", "/cv"),
                    navbar_link("Projects", "/projects"),
                    spacing="5",
                ),
                rx.avatar(
                    src="/rose_icon.svg",
                    justify="end",
                ),
                justify="between",
                align_items="center"
            ),
            width="100%",
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.link(
                    rx.heading(
                        "jorgec4444", size="6", weight="bold"
                    ),
                    href="/",
                    text_decoration="none",
                    _hover="{}"
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.image(
                                src="/rose_icon.svg"),
                            size="2",
                            radius="full",
                            color_scheme="indigo",
                            auto_focus="true"
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item(rx.link("Home", href="/")),
                        rx.menu.item(rx.link("About", href="/about")),
                        rx.menu.item(rx.link("CV", href="/cv")),
                        rx.menu.item(rx.link("Projects", href="/projects"))
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center"
            ),
            width="100%"
        ),
        bg="#171F26",
        padding="1em",
        margin_bottom=Size.BIG.value,
        position="sticky",
        z_index="999",
        width="100%"
    )