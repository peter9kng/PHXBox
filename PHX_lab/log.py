from lib.log import start_log
import sys

usage = '''
usage:
  $ python log.py 192.168.4.1

'''

if len(sys.argv) != 2:
    print(usage)
else:
    HOST = sys.argv[1]
    PORT = 7788
    start_log(HOST, PORT)
