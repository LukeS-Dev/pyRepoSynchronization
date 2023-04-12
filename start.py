import sys
import argparse

sys.path.insert(1, './src')
sys.path.insert(2, './gui')

import run
import guiRender

#Parsing arguments.
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="Starts Config GUI tool",
                    action="store_true")
args = parser.parse_args()


if args.config:    
    guiRender.start()
else: 
    run.start()