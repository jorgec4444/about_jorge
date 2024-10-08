import reflex as rx

from about_jorgec.components.link_section import link_section
import about_jorgec.constants as const
from about_jorgec.styles.colors import TextColor, Color
from about_jorgec.styles.fonts import FontSize
from about_jorgec.styles.styles import Size


def projects_page():
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.box(
                    rx.section(
                        rx.heading(
                            "Projects",
                            padding_bottom=Size.SMALL.value,
                        ),
                        rx.text(
                            "Here you can find some of my most relevant projects developed so far.",
                            text_align="start",
                            color=TextColor.BODY.value
                        )
                    ),
                    link_section(
                        "Motonitor Hack UPC (2022)",
                        rx.text(
                            rx.text(
                                """
                                This project makes the calculation based on a basic Machine Learning Model that takes data from 
                                different motorbikes (previously extracted from second-hand motorbike online shops with our tool
                                 Motonitor-Deep-Scrapper) and uses it to make a learning model that will predict with a pretty 
                                 good accuracy (82% scored) an estimated price for the motorcycle.
                                """
                            ),
                            rx.text(
                                """
                                The development of this project was driven by the challenge presented by Mundimoto during 
                                the HackUPC event that took place in the year 2022.
                                """
                                ,
                                padding_top=Size.BIG.value,
                            )
                        ),
                        href=const.MOTONITOR_URL,
                    ),
                    rx.section(
                        rx.heading(
                            rx.link(
                                "Instagram comment classification based on sentiment analysis (2023)",
                                href=const.COMMENT_CLASSIFICATION_THESIS_URL,
                                is_external=True
                            ),
                            padding_bottom=Size.SMALL.value
                        ),
                    rx.text(
                        rx.text(
                            """
                            This project is a part of my bachelor thesis is a study on how to classify the polarity of 
                            offensive comments on social networks, specifically on Instagram and oriented to 
                            professional football players around the world.
                            """
                        ),
                        rx.text(
                            """
                            This project is composed by multiple jupyter notebooks files that make possible the
                            classification of the comments and in each of them a part of the pipeline of the creation
                            of a model from scratch is carried out. You can find the complete project in the title link
                            and read the "memory.pdf" file with more detailed info about all the process and the tools 
                            used.
                            """
                            ,
                            padding_top=Size.BIG.value,
                        ),
                    ),
                    rx.hstack(
                        rx.image(
                            "/thesis_pipeline.png",
                            width="50%",
                            height="50%",
                            border_radius="20px 20px",
                            alt="thesis_pipeline_image",
                        ),
                        rx.image(
                            "/thesis_results.png",
                            width="50%",
                            height="50%",
                            border_radius="20px 20px",
                            alt="thesis_results_example"
                        ),
                        padding_top=Size.BIG.value,
                        spacing="4",
                        align_items="center",
                        width="100%"
                    ),
                        padding=Size.LARGE.value,
                        border="2.7px solid",
                        border_radius="15px",
                        border_color=Color.MY_BLUE,
                        margin_bottom=Size.BIG.value
                    ),
                    link_section(
                        "About jorgec reflex app",
                        rx.text(
                            """
                            This is the project that you are watching, It´s pure Python developed with the Reflex 
                            framework. I started It on middle September 2024 and the main objectives of this web app 
                            are both to learn how to create a web app with python from scratch with all the possible
                            functionalities and create a link in bio web to make myself better known.                     
                            """
                        ),
                        href="/"
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
                            "Projects",
                            padding_bottom=Size.SMALL.value,
                        ),
                        rx.text(
                            "Here you can find some of my most relevant projects developed so far.",
                            text_align="start",
                            color=TextColor.BODY.value
                        )
                    ),
                    link_section(
                        "Motonitor Hack UPC (2022)",
                        rx.text(
                            rx.text(
                            """
                            This project makes the calculation based on a basic Machine Learning Model that takes data from 
                            different motorbikes (previously extracted from second-hand motorbike online shops with our tool
                             Motonitor-Deep-Scrapper) and uses it to make a learning model that will predict with a pretty 
                             good accuracy (82% scored) an estimated price for the motorcycle.
                            """
                            ),
                            rx.text(
                                """
                                The development of this project was driven by the challenge presented by Mundimoto during 
                                the HackUPC event that took place in the year 2022.
                                """
                                ,
                                padding_top=Size.BIG.value,
                            )
                        ),
                        href=const.MOTONITOR_URL,
                    ),
                    rx.section(
                        rx.heading(
                            rx.link(
                                "Instagram comment classification based on sentiment analysis (2023)",
                                href=const.COMMENT_CLASSIFICATION_THESIS_URL,
                                is_external=True
                            ),
                            padding_bottom=Size.SMALL.value
                        ),
                        rx.text(
                            rx.text(
                                """
                                This project is a part of my bachelor thesis is a study on how to classify the polarity of 
                                offensive comments on social networks, specifically on Instagram and oriented to 
                                professional football players around the world.
                                """
                            ),
                            rx.text(
                                """
                                This project is composed by multiple jupyter notebooks files that make possible the
                                classification of the comments and in each of them a part of the pipeline of the creation
                                of a model from scratch is carried out. You can find the complete project in the title link
                                and read the "memory.pdf" file with more detailed info about all the process and the tools 
                                used.
                                """
                                ,
                                padding_top=Size.BIG.value,
                            ),
                        ),
                        rx.vstack(
                            rx.image(
                                "/thesis_pipeline.png",
                                border_radius="20px 20px",
                                alt="thesis_pipeline_image",
                            ),
                            rx.image(
                                "/thesis_results.png",
                                border_radius="20px 20px",
                                alt="thesis_results_example"
                            ),
                            padding_top=Size.BIG.value,
                            spacing="4",
                            align_items="center",
                            width="100%"
                        ),
                        padding=Size.LARGE.value,
                        border="2.7px solid",
                        border_radius="15px",
                        border_color=Color.MY_BLUE,
                        margin_bottom=Size.BIG.value
                    ),
                    link_section(
                        "About jorgec reflex app",
                        rx.text(
                            """
                            This is the project that you are watching, It´s pure Python developed with the Reflex 
                            framework. I started It on middle September 2024 and the main objectives of this web app 
                            are both to learn how to create a web app with python from scratch with all the possible
                            functionalities and create a link in bio web to make myself better known.                     
                            """
                        ),
                        href="/"
                    ),
                    width="90%",
                    justify="center",
                    font_size=FontSize.DEFAULT.value
                ),
                align="center",
                width="100%"
            )
        ),
        align="center",
        width="100%"
    )