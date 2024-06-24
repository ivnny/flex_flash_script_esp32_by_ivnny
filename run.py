from __future__ import absolute_import
from __future__ import print_function, unicode_literals

import codecs
import os
import sys
import threading
import glob

import esptool

import serial

from serial.tools.list_ports import comports
from serial.tools import hexlify_codec


from pprint import pprint
import urllib.request

def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/cu[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/cu.usbserial*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result



def flashFirmware(answers):
    print("Port: "+answers['port'])
    print("Firmware: "+answers['firmware'])


port_array = {}
# port_array.append('Cancel')
if(len(sys.argv)>1):
    print('sys args present')
    print(sys.argv[1])
    if(sys.argv[1] == "dev" or sys.argv[1] == "-dev"):
        print('running dev')
        dev = True
    if(sys.argv[1] == "ns" or sys.argv[1] == "-ns"):
        print('not flashing spiffs')
        spiffs = False
    if(sys.argv[1] == "-sota" or sys.argv[1] == "sota"):
        print('Sota Firmware');
        sota = True

print('COM ports:')
for serial_port in serial_ports():
    sp_key = len(port_array)+1
    port_array.update({str(sp_key): serial_port})

for serial_port in port_array:
    print('[' + serial_port + ']: ' + port_array.get(serial_port))
print('')
target_port_key = input('Select COM ?: ')

# try:
print('')
print('')
print('press a BOOT button to start flashing if not started automatically')
print('')
print('')

espmodule = esptool.main(['--chip', 'esp32', '--port', port_array.get(target_port_key), '--baud', '921600', '--before', 'default_reset', '--after', 'hard_reset', 'write_flash', '-z', '--flash_mode', 'dio', '--flash_freq', '40m', '--flash_size', 'detect', '0x1000', 'firmwares/bootloader.bin', '0x8000', 'firmwares/partitions.bin', '0x10000', 'firmwares/firmware.bin'])