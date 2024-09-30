import reflex as rx

def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.image(
                src="/safe_icon.png",
                height="8em",
                width="7em",
                alt="Safe icon certificate"
            ),
            rx.text(
                "Jorge Vinagre is a Certified SAFe® 6 Practitioner."
            ),
            align="center",
            padding="2.5em",
            position="absolute",
            bottom="0",
            width= "100vw"
        )
    )