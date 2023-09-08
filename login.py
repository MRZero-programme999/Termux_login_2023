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

  #####                                                                                      
 #     # ###### #####     ####  #    # #####     ####  ######    #    # ###### #####  ###### 
 #       #        #      #    # #    #   #      #    # #         #    # #      #    # #      
 #  #### #####    #      #    # #    #   #      #    # #####     ###### #####  #    # #####  
 #     # #        #      #    # #    #   #      #    # #         #    # #      #####  #      
 #     # #        #      #    # #    #   #      #    # #         #    # #      #   #  #      
  #####  ######   #       ####   ####    #       ####  #         #    # ###### #    # ###### 
                                                                                             

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
