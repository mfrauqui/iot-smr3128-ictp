# boot.py -- run on boot-up
from machine import UART
uart = UART(0, 115200)
os.dupterm(uart)