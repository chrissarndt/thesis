import os
import sys

if len(sys.argv) != 4:
    print ("Usage: python rename.py [target] [bpm] [mode]")
    exit

target = sys.argv[1]
bpm = sys.argv[2]
mode = sys.argv[3]

os.chdir(target)

x = 0
for filename in os.listdir('.'):
    os.rename(filename, bpm + mode + str(x) + '.mid')
    x += 1
    
   
