#! /usr/bin/env python3
################################################################################
# Created: Tuesday, October 27 2026
# Author: , ESK

import sys
import threading
import time


def mythread():
    time.sleep(1000) # Seconds I presume

def launcher():
    
    for n in range(1_000_000):
        try:
            t = threading.Thread(target=mythread)
            t.start()
        except:
            print(f"Out of resources: {n=}")
            sys.exit()
            
# End of file
################################################################################
if __name__ == "__main__":
    launcher()
    
