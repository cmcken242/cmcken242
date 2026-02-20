"""Unit tests for the starter app."""

import unittest

from app import greet


class TestGreet(unittest.TestCase):
    def test_default_greeting(self) -> None:
        self.assertEqual(greet(), "Hello, world!")

    def test_named_greeting(self) -> None:
        self.assertEqual(greet("newcomer"), "Hello, newcomer!")


if __name__ == "__main__":
    unittest.main()
