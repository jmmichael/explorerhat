#https://github.com.sandyjmacdonald/explorer-hat/tree

import explorerhat

def oh(channel, event):
    print ("oh! touch a button: {}".format(channel))
explorerhat.touch.one.pressed(oh)
