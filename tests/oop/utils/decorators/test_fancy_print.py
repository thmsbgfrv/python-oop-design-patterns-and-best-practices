"""Test fancy_print decorator"""

import unittest
from contextlib import redirect_stdout
from io import StringIO

from src.oop.utils.decorators.fancy_print import fancy_print


class MyClass:
    """Example Class to test decorator"""

    @fancy_print
    def my_method(self) -> str:
        """This is my_method."""
        return "Method executed."


class TestFancyPrintDecorator(unittest.TestCase):
    """Test fancy_print with Example MyClass"""

    def test_method_output(self) -> None:
        """test method output right"""
        obj: MyClass = MyClass()
        result: str = obj.my_method()
        self.assertEqual(result, "Method executed.")

    def test_function_metadata(self) -> None:
        """test decorator can read original method metadata"""
        obj: MyClass = MyClass()
        self.assertEqual(obj.my_method.__name__, "my_method")
        self.assertEqual(obj.my_method.__doc__, "This is my_method.")

    def test_print_statements(self) -> None:
        """Test result is expected include prints"""
        obj: MyClass = MyClass()
        with StringIO() as buf, redirect_stdout(buf):
            obj.my_method()
            output: str = buf.getvalue()
        expected: str = f"{'_'*45} my_method {'_'*45}"
        self.assertIn(expected, output)
