import smtplib
import argparse
from time import sleep
from datetime import datetime, date
'''
ARGS
-s -> For Silent mode, script will not ask to start. Needs email and pass 
-u -> Email address - Requires a pass
-p -> Password. Required with Email address
'''
def parseArgs():
    parser = argparse.ArgumentParser(description='It is wednesday, my dudes')
    parser.add_argument('-s', '--silent', dest='silentMode', action='store_true')
    
    return parser.parse_args()    

def isWednesday():
    return datetime.now().strftime('%a') == 'Wed'


if __name__ == '__main__':
    args = parseArgs()
    
    while True:
        # wait until tmr 
        # sleep(24*60*60)
        sleep(1)
        if isWednesday():
            print("IT IS WEDNESDAY MY DUDES")
        else:
            print("It is not wednesday :(")

