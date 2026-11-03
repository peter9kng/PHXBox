#!/usr/bin/env python3

from lib.download_log import download_log
import sys

usage = '''
usage:
  $ python download_log.py 192.168.4.1

'''

if len(sys.argv) != 2:
    print(usage)
else:
    HOST = sys.argv[1]
    PORT = 7788
    filename = download_log(HOST, PORT)
    # print(filename)
