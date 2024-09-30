import reflex as rx

from about_jorgec.components.navbar import navbar
from about_jorgec.components.footer import footer
from about_jorgec.views.header.header import header

class State(rx.State):
    """The app state."""
    ...


def base_page(content: rx.Component) -> rx.Component:
    return rx.box(
        navbar(),
        content,
        footer(),
        bg="#0C151D",
        color="white",
        min_height="100vh"
    )

@rx.page(route="/", title="jorgecDev")
def index() -> rx.Component:
    return base_page(
        header()
    )

@rx.page(route="/about", title="Algo sobre mí")
def about() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Sobre jorgec4444", size="7"),
            rx.text("Aqui explicaré algo mas sobre mí"),
            min_height="85vh",
            justify="center",
            align="center"
        )
    )

@rx.page(route="/cv", title="Mi CV")
def cv() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("CV", size="7"),
            rx.text("Aqui explicaré mi CV y lo añadiré como pdf"),
            min_height="84vh",
            justify="center",
            align="center"
        )
    )

@rx.page(route="/projects", title="Proyectos")
def projects() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Proyectos", size="7"),
            rx.text("Aqui explicaré mis proyectos con ejemplos"),
            min_height="84vh",
            justify="center",
            align="center"
        )
    )

app = rx.App()
app.add_page(index,
             title="Jorgec4444 | Software developer",
             description="""Hola, mi nombre es Jorge Vinagre. Soy ingeniero de software y esta es una aplicación web 
             para que me conozcáis mejor y pueda practicar el development con python""",
             image="/rose_icon.svg")
app.add_page(about)
app.add_page(cv)
app.add_page(projects)
