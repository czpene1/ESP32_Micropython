import network
import time
import ntptime

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points

wlan.connect('SSID', 'Password')
wlan.ifconfig()


ntptime.settime()
time.time() # returns time in the format of number of seconds
time.localtime() # returns time in the format of (Y, M, D, H. S,...)
(2024, 1, 1, 13, 6, 11, 0, 1)

UTC_OFFSET = 1 * 60 * 60
time.localtime(time.time() + UTC_OFFSET)