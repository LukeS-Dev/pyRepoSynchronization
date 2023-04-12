import sys
import argparse

sys.path.insert(1, './src')
sys.path.insert(2, './gui')

import run
import guiSetup

#Parsing arguments.
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="Starts Config GUI tool",
                    action="store_true")
args = parser.parse_args()


if args.config:    
    guiSetup.start()
else: 
    run.start()