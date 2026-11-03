#!/usr/bin/env python3

from lib.run_lua_on import run_lua_on
import sys

usage = '''
usage:
  $ python run_lua_on.py 192.168.4.1 'return 1+1'
  $ python run_lua_on.py 192.168.4.1 'return VERSION'
  $ python run_lua_on.py 192.168.4.1 'return list_globals()'
  $ python run_lua_on.py 192.168.4.1 'buzz(". . . -")'

  $ python run_lua_on.py 192.168.4.1 'return get_log_buf()'
  $ python run_lua_on.py 192.168.4.1 'return sd_log_last_lines(1024)'

  $ python run_lua_on.py 192.168.4.1 'return date()'
  $ python run_lua_on.py 192.168.4.1 'set_date(2026,1,1,13,10,0)'

  $ python run_lua_on.py 192.168.4.1 'return getIP("device_2")'
  $ python run_lua_on.py 192.168.4.1 'init_device("gateway", GATEWAY_MODE, "wifi", "password");reboot(0)'
  $ python run_lua_on.py 192.168.4.1 'init_device("gateway", WIFI_GATEWAY_MODE, "wifi", "password");reboot(0)'
  $ python run_lua_on.py 192.168.4.1 'init_device("device_2", DEVICE_MODE, "wifi", "password", "192.168.4.1");reboot(0)'

'''

if len(sys.argv) != 3:
    print(usage)
else:
    HOST = sys.argv[1]
    PORT = 7788
    lua_script = sys.argv[2]
    ret = run_lua_on(HOST, PORT, lua_script)
    # print(ret)
