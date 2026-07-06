# Unit Converter CLI

A command-line unit conversion application built with Python.

I created this project to practise Python project structure, packages,
modules, virtual environments, dependency management, Git, and clean
command-line interfaces. Marks day 1 of my 60-day AI/ML learning journey!

## Features

- Convert kilometers to miles
- Convert miles to kilometers
- Convert kilograms to pounds
- Convert pounds to kilograms
- Convert Celsius to Fahrenheit
- Convert Fahrenheit to Celsius
- Interactive terminal menu
- Input validation using Rich prompts

## Project Structure

```text
day01-unit-converter/
│
├── unit_converter/
│   ├── __init__.py
│   ├── length.py
│   ├── temperature.py
│   └── weight.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

clone the repository:
    git clone [UNIT_CONVERTER_REPOSITORY_URL](https://github.com/Mahnoor-Asad-Khan/day01-unit-converter)
    cd day01-unit-converter

create a virtual environment:
    python -m venv .venv

activate it on Windows Powershell
    .\.venv\Scripts\Activate.ps1

install required packages:
    python -m pip install -r requirements.txt

## Usage
run the application:
    python main.py

Select a conversion from the menu and enter a numeric value.

## What I Learned

Difference between Python scripts, modules, and packages
Purpose of __init__.py
Creating and activating a virtual environment
Managing dependencies with requirements.txt
Excluding local files using .gitignore
Writing meaningful Git commits
Creating a multi-file Python application

## Technologies

Python
Rich
Git
GitHub