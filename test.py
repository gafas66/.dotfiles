#! /usr/bin/env python3
################################################################################
# Created: Friday, November 13 2026
# Author: , ESK

import sys
import termios
import tty


def main():
    if len(sys.argv) > 1:
        print("Select:")
        for i,d in enumerate(wdir):
            print(f"[{i}] {d}")
    else:
    #cmd = input("Enter some string text: ")
        try:
            #cmd = int(input(""))
            cmd = int(getch())
        except ValueError:
            print("echo No number was entered")
            sys.exit(0)
        if cmd < 0 or cmd > (len(wdir)-1):
            print("echo Number out of range")
            sys.exit(0)
        #print(f"echo '{cmd} <- was entered'")
        print(f"cd {wdir[cmd]}")

wdir = [
    "/home/demo_10g/Metis_Bringup/metis-bringup-scripts/code",
    "/home/demo_10g/Metis_Bringup/metis-bringup-scripts_cc",
]

def getch():
    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)  # or tty.setraw(fd) if you prefer raw mode's behavior.
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)

# End of file
if __name__=="__main__": main()
################################################################################
