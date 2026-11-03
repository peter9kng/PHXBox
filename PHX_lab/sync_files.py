from lib.sync_files import sync_files
import sys

usage = '''
usage:
  $ python sync_files.py 192.168.4.1 ./case_1/

'''

if len(sys.argv) != 3:
    print(usage)
else:
    HOST = sys.argv[1]
    PORT = 7788
    file_path = sys.argv[2]
    sync_files(HOST, PORT, file_path)