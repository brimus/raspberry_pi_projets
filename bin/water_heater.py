import time
import smbus
import sys
import configparser

config = configparser.ConfigParser()
config.read('../etc/water_heater.cfg')
config.sections()

RELAY = int(config['WATERHEATER']['RELAY'])
SLT = int(config['WATERHEATER']['SLT'])
DEVICE_BUS = int(config['I2C']['DEVICE_BUS'])
DEVICE_ADDR = 0x10


bus = smbus.SMBus(DEVICE_BUS)


bus.write_byte_data(DEVICE_ADDR, RELAY, 0xFF)
print('Relay '+config['WATERHEATER']['RELAY']+' is on')
time.sleep(SLT)

bus.write_byte_data(DEVICE_ADDR, RELAY, 0x00)
print('Relay '+config['WATERHEATER']['RELAY']+' is off')
time.sleep(1)

sys.exit()
