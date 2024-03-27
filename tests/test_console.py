import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def test_empty_line(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), '')

    def test_quit_command(self):
        """Test that quit command actually exits"""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def test_EOF_command(self):
        """Test EOF sends newline and exits"""
        with self.assertRaises(SystemExit): HBNBCommand().onecmd("EOF")

    def test_create_missing_class_name(self):
        """Test 'create' command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_create_invalid_class_name(self):
        """Test 'create' command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyClass")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_show_missing_class(self):
        """Test 'show' command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_show_missing_id(self):
        """Test 'show' command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

    def test_destroy_missing_class(self):
        """Test 'destroy' command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_all_nonexistent_class(self):
        """Test 'all' command with nonexistent class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyClass")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_update_missing_class_name(self):
        """Test 'update' command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_update_missing_id(self):
        """Test 'update' command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

    def test_do_count_no_class(self):
        """Test 'count' command with no class given"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            self.assertEqual("", f.getvalue())

    def test_do_count_invalid_class(self):
        """Test 'count' command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count MyClass")
            self.assertEqual("0\n", f.getvalue())


if __name__ == "__main__":
    unittest.main()
