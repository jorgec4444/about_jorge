import reflex as rx

def projects_page():
    return rx.vstack(
        rx.heading("Projects", size="8", width="50%"),
        justify="center",
        align="center",
        width="100%"
    )