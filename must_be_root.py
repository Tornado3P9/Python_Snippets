import sys
import os

if not os.geteuid() == 0:
    sys.exit("\nOnly root can run this script\n")

print("Great, you have got root permission!")
