#https://github.com/pimoroni/explorer-hat/blob/504720e4bee2b2c9241430832a9370251ed5bc7e/examples/analog-event.py
#!/usr/bin/env python

import signal

import explorerhat


print("""
This example shows how you can monitor an analog input by attaching a function to its changed event.

You should see the analog value being printed out as it changes.

Try connecting up a rotary potentiometer or analog sensor to input one.

Press CTRL+C to exit.
""")

def handle_analog(pin, value):
    print(pin.name, value)

explorerhat.analog.one.changed(handle_analog)

signal.pause()