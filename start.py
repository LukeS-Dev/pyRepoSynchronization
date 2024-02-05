import sys
import argparse

sys.path.insert(1, './src')
sys.path.insert(2, './gui')



#Parsing arguments.
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="Starts Config GUI tool",
                    action="store_true")
args = parser.parse_args()

if args.config:
    import guiRender
    guiRender.start()
else: 
    import run
    run.start()
    
    
    