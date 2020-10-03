import subprocess
import tempfile
import unittest


class CommandTest(unittest.TestCase):

    def test_format_with_newline(self):
        with tempfile.TemporaryDirectory() as dir:
            with open(dir + '/input.txt', 'w') as fp:
                fp.write('abc\ndef\nghi\n')

            subprocess.call(['autonl', dir + '/input.txt'])

            with open(dir + '/input.txt', 'r') as fp:
                actual = fp.read()

        expected = 'abc\ndef\nghi\n'

        self.assertEqual(expected, actual)

    def test_format_without_newline(self):
        with tempfile.TemporaryDirectory() as dir:
            with open(dir + '/input.txt', 'w') as fp:
                fp.write('abc\ndef\nghi')

            subprocess.call(['autonl', dir + '/input.txt'])

            with open(dir + '/input.txt', 'r') as fp:
                actual = fp.read()

        expected = 'abc\ndef\nghi\n'

        self.assertEqual(expected, actual)

    def test_format_with_multiple_files(self):
        with tempfile.TemporaryDirectory() as dir:
            with open(dir + '/input1.txt', 'w') as fp:
                fp.write('abc\ndef\nghi\n')

            with open(dir + '/input2.txt', 'w') as fp:
                fp.write('abc\ndef\nghi')

            subprocess.call(['autonl', dir + '/input1.txt', dir + '/input2.txt'])

            with open(dir + '/input1.txt', 'r') as fp:
                actual1 = fp.read()

            with open(dir + '/input2.txt', 'r') as fp:
                actual2 = fp.read()

        expected = 'abc\ndef\nghi\n'

        self.assertEqual(expected, actual1)
        self.assertEqual(expected, actual2)
