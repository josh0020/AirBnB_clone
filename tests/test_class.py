#!/usr/bin/python3
"""Module for test classes"""
import inspect
import unittest
import pep8
import sys

"""Get the current script's directory
Add the parent directory to the Python path
Get the absolute path of the parent directory (project root)"""
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)


class TestClassDocumentation():
    """Class that allow us to test multiples classes"""

    def __init__(self, tests, _class):
        """Constructor"""
        self.tests = tests
        self.name = _class

        # Get all the methods of class @name
        self.functions = inspect.getmembers(self.name, inspect.isfunction)

    def documentation(self):
        """Test documentation of the module, class and methods"""
        with self.tests.subTest(msg='Testing methods'):
            for f in self.functions:
                with self.tests.subTest(msg='Documentation method {}'
                                        .format(f[0])):

                    doc = f[1].__doc__
                    self.tests.assertGreaterEqual(len(doc), 1)

        with self.tests.subTest(msg='Testing class'):
            doc = self.name.__doc__
            self.tests.assertGreaterEqual(len(doc), 1)

    def pep8(self, files):
        """Test linter pep8 over the files"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(files)
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnings)."')

if __name__ == '__main__':
    unittest.main()

