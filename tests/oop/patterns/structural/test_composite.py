"""Module Composite Tests"""
import unittest
from io import StringIO
from typing import Any
from unittest.mock import patch

from oop.patterns.structural.composite import Directory, File


class TestFileSystem(unittest.TestCase):
    """Test cases for the File System Composite pattern."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_file_display(self, mock_stdout: Any) -> None:
        """Test displaying a single file."""
        file = File("test_file.txt")
        file.display()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "File: test_file.txt")

    @patch('sys.stdout', new_callable=StringIO)
    def test_directory_display(self, mock_stdout: Any) -> None:
        """Test displaying a directory with files."""
        dir1 = Directory("test_directory")
        file1 = File("file1.txt")
        file2 = File("file2.txt")
        dir1.add(file1)
        dir1.add(file2)

        dir1.display()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Directory: test_directory\n  File: file1.txt\n  File: file2.txt")

    @patch('sys.stdout', new_callable=StringIO)
    def test_nested_directory_display(self, mock_stdout: Any) -> None:
        """Test displaying a nested directory structure."""
        root = Directory("root")
        sub_dir = Directory("sub_directory")
        file1 = File("file1.txt")
        file2 = File("file2.txt")
        sub_dir.add(file1)
        root.add(sub_dir)
        root.add(file2)

        root.display()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Directory: root\n  Directory: sub_directory\n    File: file1.txt\n  File: file2.txt")
