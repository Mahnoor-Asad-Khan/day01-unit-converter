"""Command-line interface for the unit converter."""

from rich.console import Console
from rich.prompt import FloatPrompt, Prompt

from unit_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kg_to_pounds,
    km_to_miles,
    miles_to_km,
    pounds_to_kg,
)

console = Console()


def display_menu() -> None:
    """Display the available conversion options."""
    console.print("\n[bold cyan]Unit Converter[/bold cyan]")
    console.print("[1] Kilometers to miles")
    console.print("[2] Miles to kilometers")
    console.print("[3] Kilograms to pounds")
    console.print("[4] Pounds to kilograms")
    console.print("[5] Celsius to Fahrenheit")
    console.print("[6] Fahrenheit to Celsius")


def perform_conversion(choice: str, value: float) -> tuple[float, str]:
    """Perform the selected conversion and return its result and unit."""

    if choice == "1":
        return km_to_miles(value), "miles"

    if choice == "2":
        return miles_to_km(value), "kilometers"

    if choice == "3":
        return kg_to_pounds(value), "pounds"

    if choice == "4":
        return pounds_to_kg(value), "kilograms"

    if choice == "5":
        return celsius_to_fahrenheit(value), "°F"

    return fahrenheit_to_celsius(value), "°C"


def main() -> None:
    """Run the unit converter application."""
    display_menu()

    choice = Prompt.ask(
        "\nSelect a conversion",
        choices=["1", "2", "3", "4", "5", "6"],
    )

    value = FloatPrompt.ask("Enter the value")

    result, unit = perform_conversion(choice, value)

    console.print(
        f"\n[bold green]Result:[/bold green] "
        f"{value:.2f} converts to {result:.2f} {unit}"
    )


if __name__ == "__main__":
    main()