import reflex as rx

def link_icon(icon: str, href:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            icon,
            alt=alt,
            width="1.5em",
            height="1.5em"
        ),
        href=href,
        is_external=True
    )