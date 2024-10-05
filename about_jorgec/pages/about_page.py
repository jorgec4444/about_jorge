import reflex as rx

def about_page():
    return rx.vstack(
        rx.heading("About me", size="8", width="50%"),
        align="center",
        width="100%",
    )