#! --*-- coding: utf-8 --*--
__author__ = 'gaoxingsheng'

#!/usr/local/bin/python
import sys
import os
import urllib
import re

original = sys.argv[1]

if len(sys.argv) > 2:
    out_file = sys.argv[2]
else:
    out_file = "error.log"


if os.path.isfile("temp"):
    os.remove("temp")

shell_command = 'cat ' + original + " | grep '?data=' >> temp"
os.popen(shell_command)


def parse():
    origion = open("temp", "r")
    parsed = open(out_file, "w")

    get_errors = {}
    key_errors = {}
    for line in origion.readlines():
        error_str = urllib.unquote(line)
        key = re.findall(r"crash/\?data(.*)user_token", error_str)[0]
        if key:
            count = get_errors.get(key, 0)
            if count <= 0:
                get_errors.setdefault(key, 1)
                key_errors.setdefault(key, error_str)
                # parsed.writelines(error_str)
                # parsed.writelines("\n")
            else:
                get_errors[key] = count + 1


    erros = []
    for key in get_errors.keys():
        # print key
        count = get_errors.get(key, 0)
        error_str = key_errors.get(key)
        erros.append(str(count) + " CERROR: " + error_str)

    erros.sort(key = lambda i:int(re.match(r'[0-9]+', i).group()), reverse = True)


    for i in xrange(0, len(erros)):
        error_str = erros[i]
        parsed.writelines(error_str)
        parsed.writelines("\n")

    origion.close()
    parsed.close()

# print get_errors

parse();

if os.path.isfile("temp"):
    os.remove("temp")