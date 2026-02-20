"""Example entry point for the starter project."""

from .greetings import greet


def main() -> None:
    """Run a tiny CLI demonstration."""
    print(greet())


if __name__ == "__main__":
    main()
