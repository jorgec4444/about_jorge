import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(
                    rx.heading(
                        "jorgec4444", size="6", weight="bold"
                    ),
                    href="/",
                    text_decoration="none",
                    _hover="{}"
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", "/about"),
                    navbar_link("CV", "/"),
                    navbar_link("Projects", "/"),
                    spacing="5",
                ),
                rx.avatar(
                    src="rose_icon.svg",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.heading(
                    "jorgec4444", size="5", weight="bold"
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.image(src="rose_icon.svg"),
                            size="2",
                            radius="full",
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
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        z_index="999",
        width="100%",
    )