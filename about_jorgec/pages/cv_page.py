import reflex as rx

from about_jorgec.components.cv_section import cv_section
from about_jorgec.styles.colors import TextColor
from about_jorgec.styles.fonts import FontSize
from about_jorgec.styles.styles import Size


def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

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
                                    href="https://drive.google.com/file/d/1RoY-7AArT1ms_EStbHklRMeBc12jtvj0/view?usp=sharing",
                                    is_external=True,
                                ),
                                "and have a look."
                            ),
                            text_align="start",
                            color=TextColor.BODY.value
                        )
                    ),
                    cv_section(
                        "Ferrimax",
                        read_file("about_jorgec/data/ferrimax_description.txt"),
                        href="https://ferrimax.com/es"
                    ),
                    cv_section(
                        "Immfly",
                        read_file("about_jorgec/data/immfly_description.txt"),
                        href="https://www.immfly.com/"
                    ),
                    cv_section(
                        "Merkle",
                        read_file("about_jorgec/data/merkle_description.txt"),
                        href="https://www.merkle.com/es"
                    ),
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
                    cv_section("Curriculum Vitae", "", ""),
                    cv_section(
                        "Ferrimax",
                        read_file("about_jorgec/data/ferrimax_description.txt"),
                        href="https://ferrimax.com/es"
                    ),
                    cv_section(
                        "Immfly",
                        read_file("about_jorgec/data/immfly_description.txt"),
                        href="https://www.immfly.com/"
                    ),
                    cv_section(
                        "Merkle",
                        read_file("about_jorgec/data/merkle_description.txt"),
                        href="https://www.merkle.com/es"
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