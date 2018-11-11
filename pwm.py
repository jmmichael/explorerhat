#https://github.com/pimoroni/explorer-hat/commit/504720e4bee2b2c9241430832a9370251ed5bc7e
#https://github.com/pimoroni/explorer-hat/blob/504720e4bee2b2c9241430832a9370251ed5bc7e/library/test.py
#!/usr/bin/env python

import signal
import time

import explorerhat


while True:

    print("Trying raw pwm...")
    explorerhat.light.red.pwm(1, 95)
    time.sleep(1)

    print("Trying raw pwm...")
    explorerhat.light.green.pwm(10, 55)
    time.sleep(1)

    print("Trying raw pwm...")
    explorerhat.light.yellow.pwm(10, 55)
    time.sleep(1)

#explorerhat.touch.pressed(lambda x,y:explorerhat.light.on())

#explorerhat.touch.released(lambda x,y:explorerhat.light.off())

#signal.pause()