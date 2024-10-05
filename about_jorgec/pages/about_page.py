import reflex as rx

from about_jorgec.styles.colors import TextColor, Color
from about_jorgec.styles.fonts import FontSize
from about_jorgec.styles.styles import Size
import about_jorgec.constants as const


def about_page():
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.box(
                    rx.section(
                        rx.heading(
                            "About me",
                            padding_bottom=Size.MEDIUM.value,
                        ),
                        rx.text(
                            rx.fragment(
                                """
                                I was born in Barcelona on April, 2000. During high school I started developing my first 
                                programming skills working with an Arduino robot. I started a Computer Science degree in 2018 at
                                Universitat de Barcelona (UB), graduating 5 years later in June 2023. I enjoyed working on 
                                """,
                                rx.link(
                                    "my bachelor thesis project about Natural Language Processing (NLP). ",
                                    href=const.BACHELOR_THESIS_URL
                                ),
                                "During this period I worked at ",
                                rx.link(
                                    "Ferrimax",
                                    href=const.FERRIMAX_URL,
                                    is_external=True
                                ), ", ",
                                rx.link(
                                    "Immfly",
                                    href=const.IMMFLY_URL,
                                    is_external=True
                                ), ", ",
                                rx.link(
                                    "Merkle",
                                    href=const.MERKLE_URL,
                                    is_external=True
                                ),
                                " and now a days I´m currently working at ",
                                rx.link(
                                    "Carver.",
                                    href=const.CARVER_URL,
                                    is_external=True
                                ),
                                rx.text(
                                    """
                                    With each passing year, my desire to develop and discover new parts of software development 
                                    increases. and in September 2024 I started developing this link in bio web app to learn
                                    about Reflex framework and web development. My idea is not just about developing a frontend 
                                    app but exploring all possible fields such as servers, database or online shopping.
                                    """,
                                    padding_top="2em"
                                ),
                                rx.text(
                                    "On November 2024 I will start a postgraduate course in ",
                                    rx.link(
                                        "Quantum Engineering ",
                                        href=const.QUANTUM_POSTGRADUATE_UPC_LINK),
                                    "at Universitat Politècnica de Catalunya (UPC) to learn about its applications and to be "
                                    "able to apply this knowledge in my development.",
                                    padding_top="2em"
                                ),
                                rx.text(
                                    """
                                    On a personal level, I like doing multiple sports like football ⚽, padel 🎾 or going hiking
                                    ⛰️ but I'm always ready to do any different activities. I also use to play video games 🎮 
                                    with friends when I have free time.
                                    """,
                                    padding_top="2em"
                                )
                            ),
                            text_align="start",
                            color=TextColor.BODY.value,
                            padding=Size.LARGE.value,
                            border="2.7px solid",
                            border_radius="15px",
                            border_color=Color.MY_BLUE
                        )
                    ),
                    width="60%",
                    justify="center",
                    font_size=FontSize.DEFAULT.value
                ),
                align="center",
                width="100%"
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.box(
                    rx.section(
                        rx.heading(
                            "About me",
                            padding_bottom=Size.MEDIUM.value,
                        ),
                        rx.text(
                            rx.fragment(
                                """
                                I was born in Barcelona on April, 2000. During high school I started developing my first 
                                programming skills working with an Arduino robot. I started a Computer Science degree in 2018 at
                                Universitat de Barcelona (UB), graduating 5 years later in June 2023. I enjoyed working on 
                                """,
                                rx.link(
                                    "my bachelor thesis project about Natural Language Processing (NLP). ",
                                    href=const.BACHELOR_THESIS_URL
                                ),
                                "During this period I worked at ",
                                rx.link(
                                    "Ferrimax",
                                    href=const.FERRIMAX_URL,
                                    is_external=True
                                ), ", ",
                                rx.link(
                                    "Immfly",
                                    href=const.IMMFLY_URL,
                                    is_external=True
                                ), ", ",
                                rx.link(
                                    "Merkle",
                                    href=const.MERKLE_URL,
                                    is_external=True
                                ),
                                " and now a days I´m currently working at ",
                                rx.link(
                                    "Carver.",
                                    href=const.CARVER_URL,
                                    is_external=True
                                ),
                                rx.text(
                                    """
                                    With each passing year, my desire to develop and discover new parts of software development 
                                    increases. and in September 2024 I started developing this link in bio web app to learn
                                    about Reflex framework and web development. My idea is not just about developing a frontend 
                                    app but exploring all possible fields such as servers, database or online shopping.
                                    """,
                                    padding_top="2em"
                                ),
                                rx.text(
                                    "On November 2024 I will start a postgraduate course in ",
                                    rx.link(
                                        "Quantum Engineering ",
                                        href=const.QUANTUM_POSTGRADUATE_UPC_LINK),
                                    "at Universitat Politècnica de Catalunya (UPC) to learn about its applications and to be "
                                    "able to apply this knowledge in my development.",
                                    padding_top="2em"
                                ),
                                rx.text(
                                    """
                                    On a personal level, I like doing multiple sports like football ⚽, padel 🎾 or going hiking
                                    ⛰️ but I'm always ready to do any different activities. I also use to play video games 🎮 
                                    with friends when I have free time.
                                    """,
                                    padding_top="2em"
                                )
                            ),
                            text_align="start",
                            color=TextColor.BODY.value,
                            padding=Size.LARGE.value,
                            border="2.7px solid",
                            border_radius="15px",
                            border_color=Color.MY_BLUE
                        )
                    ),
                    width="90%",
                    justify="center",
                    font_size=FontSize.DEFAULT.value
                ),
                align="center",
                width="100%",
            )
        )
    ),