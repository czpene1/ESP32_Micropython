import machine, neopixel

n = 4           # Number of LEDs
np = neopixel.NeoPixel(machine.Pin(5), n)  # Control pin GPIO5

# Green
np[0] = (255, 0, 0)
np[1] = (255, 0, 0)
np[2] = (255, 0, 0)
np[3] = (255, 0, 0)
np.write()

# Red
np[0] = (0, 255, 0)
np[1] = (0, 255, 0)
np[2] = (0, 255, 0)
np[3] = (0, 255, 0)
np.write()

# Blue
np[0] = (0, 0, 255)
np[1] = (0, 0, 255)
np[2] = (0, 0, 255)
np[3] = (0, 0, 255)
np.write()

# Turn off all LEDs
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np[3] = (0, 0, 0)
np.write()
