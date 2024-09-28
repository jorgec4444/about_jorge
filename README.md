# jorgec4444 Porfolio

[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.6.0+-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://fastapi.tiangolo.com)

## Project description
This project is a personal webpage developed with [Python](https://www.python.org/) and [Reflex](https://reflex.dev/), designed to showcase information about my professional journey, my projects, and my curriculum vitae (CV).
The goal of the website is to serve as a summary of my profile as a Software Developer with 2 years of experience and a space to share my future projects and technological experiments.
Additionally, I am about to start a postgraduate program in Quantum Engineering, which represents a new direction in my career, and it might be a topic I explore on this page in the future.

## Requirements

#### Install and create a virtual environment  [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) in the root of the project
Mac/Linux: `python3 -m pip install virtualenv`

Windows: `py -m pip install --user virtualenv`

`python3 -m venv .venv`

#### Activate the virtual environment 
Mac/Linux: `source .venv/bin/activate`

Windows: `.\.venv\Scripts\activate`

To deactivate the virtual environment: `deactivate`

## Dependencies
*(With the virtual environment active)*

`pip install reflex`

You can also find them in `requirements.txt`

`python -m pip install -r requirements.txt`

## Execution
`reflex run`

`reflex run --loglevel debug` *(debug mode)*

Access [http://localhost:3000](http://localhost:3000) (frontend) and [http://localhost:8000](http://localhost:8000) (backend)
