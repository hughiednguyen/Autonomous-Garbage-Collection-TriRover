# Author: hungie1122
# Purpose: Update statistics and Display all topics as they come

import json
import time
from time import sleep
import os
import paho.mqtt.client as mqtt
import copy
import zlib

import auth_info
from config_constants import *
from trirover_test_data import *


def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))


def on_log(client, obj, level, string):
    print(string)


def checksum(sequence, path, color, position):
    new_string = "sensors_status" + sequence + path + color + position
    # print(new_string)
    return hex(zlib.crc32(new_string.encode()) & 0xffffffff)


def main():
    # initializes client
    client = mqtt.Client()

    # Assign event callbacks
    #client.on_connect = on_connect

    # Uncomment to enable debug messages
    # client.on_log = on_log

    # Connect
    # client.username_pw_set(auth_info.username, auth_info.password)
    client.connect(auth_info.server_address, auth_info.port)

    # loop forever with autoreconnect
    client.loop_start()

    sequence = 0
    while(True):

        test_number = int(input("enter test #"))
        data = sample_data[test_number]
        sequence += 1
        for key in data:
            if key != 'board_id':
                if key == 'sequence':
                    data[key] = sequence
                elif key == 'checksum':
                    new_checksum = checksum(str(data['sequence']), str(
                        data['pathable']), str(data['color']), str(data['position']))
                    data[key] = new_checksum

        payload = json.dumps(data)
        print(payload)
        client.publish("sensors_status", payload, qos_level, False)

        #input("Press Enter to continue...")


if __name__ == "__main__":
    print("Observer Running!")
    main()
