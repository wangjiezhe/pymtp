#!/usr/bin/env python3
#
# A PyMTP Shell - Automagically initiates the MTP device, makes it
# easier to develop and test stuff.
# (C) 2008 Nick Devito
#

import sys
sys.path.insert(0, "../")  # So examples work on first try

import pymtp


def callback(sent, total):
    """
        A generic traffic sent/total callback
    """
    print("Sent: %s; Total: %s" % (sent, total))


def main():
    mtp = pymtp.MTP()
    mtp.connect()
    print("Welcome to the PyMTP Shell")
    print("You are currently connected to '%s'" % (mtp.get_devicename()))
    print("Your MTP object is '%s'" % ("mtp"))
    print("Your progress callback object is '%s'" % ("callback"))
    print("To exit, type 'quit'")
    while True:
        try:
            if mtp.device:
                result = input("(connected) >>> ")
            else:
                result = input("(disconnected) >>> ")
            if result.startswith("quit"):
                mtp.disconnect()
                sys.exit()
            else:
                exec(result)
        except Exception as message:
            print("An exception occurred:")
            print(message)

if __name__ == "__main__":
    main()
