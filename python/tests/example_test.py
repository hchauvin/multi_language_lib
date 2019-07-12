#!/usr/bin/env python
import unittest
import example

class ExampleTest(unittest.TestCase):
    def testSplit(self):
        self.assertEqual(example.split("foo\tbar qux"), ["foo", "bar", "qux"])

if __name__ == '__main__':
    unittest.main()
