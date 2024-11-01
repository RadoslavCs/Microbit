#ToDo zistit preco na riadku 32 je chyba
from microbit import i2c
from microbit import *

RTC_ADDR = 0x68

def bcd2bin(v):
    return v - 6 * (v >> 4)

def bin2bcd(v):
    return v + 6 * (v // 10)

def rtc_gettime():
    i2c.write(RTC_ADDR, b'\x00')
    value = i2c.read(RTC_ADDR, 7)
    ss = bcd2bin(value[0] & 0x7F)
    mm = bcd2bin(value[1])
    hh = bcd2bin(value[2])
    d = bcd2bin(value[4])
    m = bcd2bin(value[5])
    y = bcd2bin(value[6]) + 2000
    return [y, m, d, hh, mm, ss]

def rtc_settime(y, m, d, hh, mm, ss):
    value = []
    value.append(bin2bcd(ss))
    value.append(bin2bcd(mm))
    value.append(bin2bcd(hh))
    value.append(bin2bcd(0))
    value.append(bin2bcd(d))
    value.append(bin2bcd(m))
    value.append(bin2bcd(y - 2000))
    i2c.write(RTC_ADDR, b'\x00' + bytearray(value))

# rtc_gettime()
rtc_settime(2024, 11, 1, 11, 15, 0)
rtc_gettime()


tm = get_time()
str_time = '{0:02d}'.format(tm[0]) + ":" + '{0:02d}'.format(tm[1]) + ":" + '{0:02d}'.format(tm[2])
display.scroll(str_time)
