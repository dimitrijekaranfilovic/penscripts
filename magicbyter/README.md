# MagicByter #

Adds magic bytes to the beginning of the file.



```
usage: magicbyter.py [-h] -f {jpeg,jpg,png,sqlitedb,ico,tarz,gif,exe,zip,rar,elf,class,txt,mp3,iso,msoffice,tar,7z,xml,rtf} [-o OUTPUT] filename

Creates a new file with the same content and specified magic bytes

positional arguments:
  filename              File to be read

options:
  -h, --help            show this help message and exit
  -f {jpeg,jpg,png,sqlitedb,ico,tarz,gif,exe,zip,rar,elf,class,txt,mp3,iso,msoffice,tar,7z,xml,rtf}, --format {jpeg,jpg,png,sqlitedb,ico,tarz,gif,exe,zip,rar,elf,class,txt,mp3,iso,msoffice,tar,7z,xml,rtf}
                        Format of the output file
  -o OUTPUT, --output OUTPUT
                        Output file, defaults to <filename>.<format>

```