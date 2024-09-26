from tkinter.constants import SOLID
from typing import Tuple

import reflex as rx
from reflex import Component
from reflex.components.radix.themes.base import theme
from reflex_chakra import vstack, Vstack

from about_jorgec.components.navbar import navbar


class State(rx.State):
    """The app state."""

    ...


def base_page(content: rx.Component) -> rx.Component:
    return rx.box(
        navbar(),
        content
    )

@rx.page(route="/", title="jorgec4444")
def index() -> rx.Component:
    return base_page(
        rx.vstack(
        rx.heading("Equi estara la informacion de la pagina principal(fotos etc)", size="7"),
        min_height = "85vh",
        justify = "center",
        align = "center"
        )
    )

@rx.page(route="/about", title="Algo sobre mí")
def about() -> rx.Component:
    return base_page(
        vstack(
            rx.heading("Sobre jorgec4444", size="7"),
            rx.text("Aqui explicare algo mas sobre mí"),
            min_height="85vh",
            justify="center",
            align="center"
        )
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        panel_background=SOLID
    )
)
app.add_page(index,
             title="Jorgec4444 | Software developer",
             description="Hola, mi nombre es Jorge Vinagre. Soy ingeniero de software y esta es una aplicación web para que me conozcáis mejor y pueda practicar el development con python",
             image="rose_icon.svg")
app.add_page(about)
