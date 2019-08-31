import time
import smbus
import sys
import configparser
import smtplib
from email.message import EmailMessage

config = configparser.ConfigParser()
config.read('../etc/water_heater.cfg')
config.sections()

RELAY = int(config['WATERHEATER']['RELAY'])
SLT = int(config['WATERHEATER']['SLT'])
DEVICE_BUS = int(config['I2C']['DEVICE_BUS'])
MESSAGE_1 = config['MAIL']['MESSAGE_1']
MESSAGE_2 = config['MAIL']['MESSAGE_2']
SENDER = config['MAIL']['SENDER']
RECIPIENT = config['MAIL']['RECIPIENT']
DEVICE_ADDR = 0x10

bus = smbus.SMBus(DEVICE_BUS)

with open(MESSAGE_1) as fp:
	msg = EmailMessage()
	msg.set_content(fp.read())
	
msg['Subject'] = 'The Water Heater is turned ON'
msg['From'] = SENDER
msg['To'] = RECIPIENT

#send =smtplib.SMTP('localhost')
#send.send_message(msg)
#send.quit()

bus.write_byte_data(DEVICE_ADDR, RELAY, 0xFF)
print('Relay '+config['WATERHEATER']['RELAY']+' is on')
time.sleep(SLT)

bus.write_byte_data(DEVICE_ADDR, RELAY, 0x00)
print('Relay '+config['WATERHEATER']['RELAY']+' is off')
time.sleep(1)

with open(MESSAGE_2) as fp:
	msg = EmailMessage()
	msg.set_content(fp.read())
	
msg['Subject'] = 'The Water Heater is turned OFF'
msg['From'] = SENDER
msg['To'] = RECIPIENT

#send =smtplib.SMTP('localhost')
#send.send_message(msg)
#send.quit()


sys.exit()
