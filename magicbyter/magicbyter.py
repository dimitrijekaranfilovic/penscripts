import argparse

magic_bytes: dict[str, bytes] = {
    'jpeg':     b'\xFF\xD8\xFF\xDB',
    'jpg':      b'\xFF\xD8\xFF\xDB',
    'png':      b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A',
    'sqlitedb': b'\x53\x51\x4C\x69\x74\x65\x20\x66\x6F\x72\x6D\x61\x74\x20\x33\x00',
    'ico':      b'\x00\x00\x01\x00',
    'tarz':     b'\x1F\x9D',
    'gif':      b'\x47\x49\x46\x38\x37\x61',
    'exe':      b'\x4D\x5A',
    'zip':      b'\x50\x4B\x03\x04',
    'rar':      b'\x52\x61\x72\x21\x1A\x07\x00',
    'elf':      b'\x7F\x45\x4C\x46',
    'class':    b'\xCA\xFE\xBA\xBE',
    'txt':      b'\xEF\xBB\xBF',
    'mp3':      b'\xFF\xFB',
    'iso':      b'\x43\x44\x30\x30\x31',
    'msoffice': b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1',
    'tar':      b'\x75\x73\x74\x61\x72\x00\x30\x30',
    '7z':       b'\x37\x7A\xBC\xAF\x27\x1C',
    'xml':      b'\x3C\x00\x3F\x00\x78\x00\x6D\x00\x6C\x00\x20',
    'rtf':      b'\x7B\x5C\x72\x74\x66\x31'
}


def main(filename: str, format: str, output: str | None):
    content: bytes = None
    with open(filename, 'rb') as read_file:
        content = read_file.read()

    new_filename = f'{filename}.{format}' if output is None else output

    with open(new_filename, 'wb') as write_file:
        write_file.write(magic_bytes[format] + content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='magicbyter.py',
                                     description='Creates a new file with the same content and specified magic bytes')

    parser.add_argument('-f', '--format', help='Format of the output file', choices=list(magic_bytes.keys()), required=True)
    parser.add_argument('-o', '--output', help='Output file, defaults to <filename>.<format>', required=False)
    parser.add_argument('filename', help='File to be read')
    args = parser.parse_args()
    main(args.filename, args.format, args.output)