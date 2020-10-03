import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', metavar='filename', nargs='+')

    args = parser.parse_args()

    for filename in args.filenames:
        _format(filename)


def _format(filename):
    with open(filename, mode='rb') as fp:
        fp.seek(-1, 2)
        last_byte = fp.read(1)

    if last_byte == b'\n':
        return

    with open(filename, mode='ab') as fp:
        fp.write(b'\n')
