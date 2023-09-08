#!/data/data/com.termux/files/usr/bin/env python

import getpass
import hashlib
import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
txt = '''
_                                 ___                                   
      dM.                                `MM                                   
     ,MMb                                 MM                                   
     d'YM.      ____     ____      ___    MM    ___   ___  __    __  ___   ___ 
    ,P `Mb     6MMMMb\  6MMMMb\  6MMMMb   MM  6MMMMb  `MM 6MMb  6MMb `MM    MM 
    d'  YM.   MM'    ` MM'    ` 8M'  `Mb  MM 8M'  `Mb  MM69 `MM69 `Mb MM    MM 
   ,P   `Mb   YM.      YM.          ,oMM  MM     ,oMM  MM'   MM'   MM MM    MM 
   d'    YM.   YMMMMb   YMMMMb  ,6MM9'MM  MM ,6MM9'MM  MM    MM    MM MM    MM 
  ,MMMMMMMMb       `Mb      `Mb MM'   MM  MM MM'   MM  MM    MM    MM MM    MM 
  d'      YM. L    ,MM L    ,MM MM.  ,MM  MM MM.  ,MM  MM    MM    MM YM.   MM 
_dM_     _dMM_MYMMMM9  MYMMMM9  `YMMM9'Yb_MM_`YMMM9'Yb_MM_  _MM_  _MM_ YMMM9MM

______________________••••••.##....##....###....##..........###....####.##....##.##.....##.##.....##...
______________________•••••• ..##..##....##.##...##.........##.##....##..##...##..##.....##.###...###...
______________________•••••• ...####....##...##..##........##...##...##..##..##...##.....##.####.####...
______________________•••••• ....##....##.....##.##.......##.....##..##..#####....##.....##.##.###.##...
______________________••••••....##....#########.##.......#########..##..##..##...##.....##.##.....##...
______________________••••••....##....##.....##.##.......##.....##..##..##...##..##.....##.##.....##...
______________________••••••....##....##.....##.########.##.....##.####.##....##..#######..##.....##...






                                  
'''

print(bcolors.OKGREEN + txt)

password = getpass.getpass()

filepass = open("/data/data/com.termux/files/usr/share/login/.pass", "r")
filepass = filepass.read().split("\n")[0]

password = password.encode()
password = hashlib.sha1(password).hexdigest()

if password != filepass:
    print("Invalid password")
    os.system("exit")
else:
    prefix = "/data/data/com.termux/files/usr"
    home = "/data/data/com.termux/files/home"
    motd = False
    hush = False

    os.system("clear")

    try:
        open(prefix + "/etc/motd")
        motd = True
    except:
        motd = False

    try:
        open(home + "/.hushlogin")
        hush = True
    except:
        hush = False

    if motd and not hush:
        print(open(prefix + "/etc/motd").read())
    
    os.system(sys.argv[1] + " " + sys.argv[2])
