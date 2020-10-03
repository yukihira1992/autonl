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
