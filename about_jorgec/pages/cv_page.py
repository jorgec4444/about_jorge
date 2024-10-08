import reflex as rx

from about_jorgec.components.link_section import link_section
import about_jorgec.constants as const
from about_jorgec.styles.colors import TextColor
from about_jorgec.styles.fonts import FontSize
from about_jorgec.styles.styles import Size


def cv_page():
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.box(
                    rx.section(
                        rx.heading(
                            "Curriculum Vitae",
                            padding_bottom=Size.SMALL.value,
                        ),
                        rx.text(
                            rx.fragment(
                                "Here you can find my detailed work experience in different companies with a brief summary of my "
                                "role in each of them. However you can always ",
                                rx.link(
                                    "download my CV in .pdf format ",
                                    href=const.DRIVE_CV_URL,
                                    is_external=True,
                                ),
                                "and have a look."
                            ),
                            text_align="start",
                            color=TextColor.BODY.value
                        )
                    ),
                    link_section(
                        "Ferrimax",
                        rx.text(
                            """
                            From June 2021 until September 2021 I worked as a researcher in a embedded software project 
                            from a safety-boxes company. My job as part of the I+D team during my internship was to 
                            upgrade the safe-deposit boxes embedded software to new languages and frameworks in order
                            to improve the performance of the programs and make the code more adaptable to now a
                            day technologies.
                            """
                        ),
                        href=const.FERRIMAX_URL
                    ),
                    link_section(
                        "Immfly",
                        rx.text(
                            rx.text(
                                """
                                From July 2022 until December 2022 I worked at Immfly, a company that created an
                                entertainment system for the airplanes that allows passengers to play games, watch
                                movies or series or even order products during the flight.
                                """
                            ),
                            rx.text(
                                """
                                My role in the company during my internship was as a data analyst,
                                contributing to the new Data team providing analysis and data structures of all our 
                                solutions for airlines, such as pre-order and retail on board and inflight entertainment.
                                """
                                ,
                                padding_top=Size.BIG.value,
                            ),
                            rx.text(
                                """
                                The team had a wide-range of goals from creating, maintaining and improving data 
                                structures to forecasting and discovering new and insightful KPI's with the use of 
                                Machine Learning. We also helped our partners to perform data-oriented decisions, such
                                as feedback classification for NPS or stock prediction.
                                """
                                ,
                                padding_top=Size.BIG.value,
                            )
                        ),
                        href=const.IMMFLY_URL
                    ),
                    link_section(
                        "Merkle",
                        rx.text(
                            rx.text(
                                """
                                From January 2023 until September 2024 I worked at Merkle as a Software developer
                                cooperating with the Sky company. I joined the company in my last career year and I
                                started to put agile and SAFe methodologies into practice on a daily basis.
                                """
                            ),
                            rx.text(
                                """
                                I worked for the sky customer CARE team providing solutions and giving support on the
                                troubleshooting area going through all phases of a programme's lifecycle. I worked
                                mostly in the backend part of the troubleshooting area managing the troubleshooting
                                program direction managing routers, boosters and devices errors to help sky agents
                                to solve the customer issues.
                                """
                                ,
                                padding_top=Size.BIG.value,
                            )
                        ),
                        href=const.MERKLE_URL
                    ),
                    link_section(
                        "Carver Advanced Systems",
                        "Coming soon...",
                        href=const.CARVER_URL),
                    width = "60%",
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
                            "Curriculum Vitae",
                            padding_bottom=Size.SMALL.value,
                        ),
                        rx.text(
                            rx.fragment(
                                "Here you can find my detailed work experience in different companies with a brief summary of my "
                                "role in each of them. However you can always ",
                                rx.link(
                                    "download my CV in .pdf format ",
                                    href=const.DRIVE_CV_URL,
                                    is_external=True,
                                ),
                                "and have a look."
                            ),
                            text_align="start",
                            color=TextColor.BODY.value
                        )
                    ),
                    link_section(
                        "Ferrimax",
                        rx.text(
                            """
                            From June 2021 until September 2021 I worked as a researcher in a embedded software project 
                            from a safety-boxes company. My job as part of the I+D team during my internship was to 
                            upgrade the safe-deposit boxes embedded software to new languages and frameworks in order
                            to improve the performance of the programs and make the code more adaptable to now a
                            day technologies.
                            """
                        ),
                        href=const.FERRIMAX_URL
                    ),
                    link_section(
                        "Immfly",
                        rx.text(
                            rx.text(
                                """
                                From July 2022 until December 2022 I worked at Immfly, a company that created an
                                entertainment system for the airplanes that allows passengers to play games, watch
                                movies or series or even order products during the flight.
                                """
                            ),
                            rx.text(
                                """
                                My role in the company during my internship was as a data analyst,
                                contributing to the new Data team providing analysis and data structures of all our 
                                solutions for airlines, such as pre-order and retail on board and inflight entertainment.
                                """
                                ,
                                padding_top=Size.BIG.value,
                            ),
                            rx.text(
                                """
                                The team had a wide-range of goals from creating, maintaining and improving data 
                                structures to forecasting and discovering new and insightful KPI's with the use of 
                                Machine Learning. We also helped our partners to perform data-oriented decisions, such
                                as feedback classification for NPS or stock prediction.
                                """
                                ,
                                padding_top=Size.BIG.value,
                            )
                        ),
                        href=const.IMMFLY_URL
                    ),
                    link_section(
                        "Merkle",
                        rx.text(
                            rx.text(
                                """
                                From January 2023 until September 2024 I worked at Merkle as a Software developer
                                cooperating with the Sky company. I joined the company in my last career year and I
                                started to put agile and SAFe methodologies into practice on a daily basis.
                                """
                            ),
                            rx.text(
                                """
                                I worked for the sky customer CARE team providing solutions and giving support on the
                                troubleshooting area going through all phases of a programme's lifecycle. I worked
                                mostly in the backend part of the troubleshooting area managing the troubleshooting
                                program direction managing routers, boosters and devices errors to help sky agents
                                to solve the customer issues.
                                """
                                ,
                                padding_top=Size.BIG.value,
                            )
                        ),
                        href=const.MERKLE_URL
                    ),
                    link_section("Carver Advanced Systems",
                                 "Coming soon...",
                                 href=const.CARVER_URL),
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