import reflex as rx

from about_jorgec.components.cv_section import cv_section
from about_jorgec.styles.fonts import FontSize

def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

def cv_page():
    return rx.box(
        rx.desktop_only(
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