import reflex as rx

def link_icon(icon: str, href:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(icon),
        href=href,
        alt=alt,
        is_external=True
    )