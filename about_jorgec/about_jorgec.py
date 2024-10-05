import reflex as rx

from about_jorgec.components.navbar import navbar
from about_jorgec.components.footer import footer
from about_jorgec.views.header.header import header
from about_jorgec.pages.about_page import about_page
from about_jorgec.pages.cv_page import cv_page
from about_jorgec.pages.projects_page import projects_page
from about_jorgec.styles.styles import BASE_STYLE

#class State(rx.State):
#    """The app state."""
#    ...


def base_page(content: rx.Component) -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            content,
            flex="1",
        ),
        footer(),
        color="white",
        min_height="100vh",
        display="flex",
        flex_direction="column",
        justify_content="space-between"
    )

@rx.page(
    route="/",
    title="Jorgec4444 | Software developer",
    description=
    """
    Hola, mi nombre es Jorge Vinagre. Soy ingeniero de software y esta es una app web para que me conozcáis 
    mejor echa con puro python
    """,
    image="/about_jorgec/assets/rose_icon.svg"
)
def index() -> rx.Component:
    return base_page(
        header()
    )

@rx.page(route="/about", title="About Jorge Vinagre")
def about() -> rx.Component:
    return base_page(
        about_page()
    )

@rx.page(route="/cv", title="Jorge Vinagre CV")
def cv() -> rx.Component:
    return base_page(
        cv_page()
    )

@rx.page(route="/projects", title="Jorge Vinagre projects")
def projects() -> rx.Component:
    return base_page(
        projects_page()
    )

app = rx.App(style=BASE_STYLE)
app.add_page(index)
app.add_page(about)
app.add_page(cv)
app.add_page(projects)
