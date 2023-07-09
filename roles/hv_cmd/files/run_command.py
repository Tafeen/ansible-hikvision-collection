#!/usr/bin/env python3
import sys
from netmiko import ConnectHandler

HOST=sys.argv[1]
USERNAME=sys.argv[2]
PASS=sys.argv[3]
COMMAND=sys.argv[4]

def main():
    connection = ConnectHandler(host=HOST, port='22', username=USERNAME, password=PASS, device_type='cisco_ios')
    output = connection.send_command(COMMAND)
    print(output)
    connection.disconnect()

main()