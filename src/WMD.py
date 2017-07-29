import smtplib
import argparse


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


if __name__ == '__main__':
    args = parseArgs()

