#!/usr/bind/env python
#_*_ coding; utf8 _*_

import os

#COLORS
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'


def banner():
	os.system('clear')
	print("""          
 \033[1;37m███████╗███████╗ ██████╗\033[1;35m██████╗  █████╗ ███████╗███████╗\033[0m
 \033[1;37m██╔════╝██╔════╝██╔════╝\033[1;35m██╔══██╗██╔══██╗██╔════╝██╔════╝\033[0m
 \033[1;37m███████╗█████╗  ██║     \033[1;35m██████╔╝███████║███████╗███████╗\033[0m
 \033[1;37m╚════██║██╔══╝  ██║     \033[1;35m██╔═══╝ ██╔══██║╚════██║╚════██║\033[0m
 \033[1;37m███████║███████╗╚██████╗\033[1;35m██║     ██║  ██║███████║███████║\033[0m
 \033[1;37m╚══════╝╚══════╝ ╚═════╝\033[1;35m╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝\033[0m
                                                        
          \033[1;37mby \033[1;45;37mR3LI4NT\033[0m \033[1;37m~ secure password generator\033[0m
	""")

def menu():
	print("""\n \033[1;37m[1] \033[1;35mRandom\033[0m
 \033[1;37m[2] \033[1;35mCustomize\033[0m
	""")		