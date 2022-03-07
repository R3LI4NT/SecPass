from banner.banner import *
import random
import time
import sys

banner()
menu()


option = input("(\033[1;37mSecPass\033[0m) >>> ")
						
if option == '1':
	f = open("password.txt", "a")
	lower = "abcdefghijklmnñopqrstuvw"
	upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	numbers = "0123456789"
	symbols = "[]{}();/.,-_@><€%&#!=$~*?¿+'"
	length = 25
	all = lower + upper + numbers + symbols
	password = "".join(random.sample(all,length))
	print('\nNew password: \033[1;32m{}\033[0m'.format(password))
	f.write("New password: {}".format(password)+'\n')
	print('')
	f.close()
	print("Saved on: {}password.txt{}".format(YELLOW,END))

elif option == '2':
	f = open("password.txt", "a")
	lowercase = input('Lowercase [\033[1;37my/\033[0m\033[1;35mn\033[0m]: ')
	capital_letters = input('Capital letters [\033[1;37my/\033[0m\033[1;35mn\033[0m]: ')
	numbers = input('Numbers [\033[1;37my/\033[0m\033[1;35mn\033[0m]: ')
	symbols = input('Symbols [\033[1;37my/\033[0m\033[1;35mn\033[0m]: ')
	length = int(input('Length: '))

	if lowercase == "y":
		lowercase = "abcdefghijklmnñopqrstuvw"
	elif lowercase == "n":
		pass

	if capital_letters == "y":
		capital_letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	elif capital_letters == "n":
		pass

	if numbers == "y":
		numbers = "0123456789"
	elif numbers == "n":
		pass

	if symbols == "y":
		symbols = "[]{}();/.,-_@><€%&#!=$"
	elif symbols == "n":
		pass

	all = lowercase + capital_letters + numbers + symbols
	password = "".join(random.sample(all,length))
	print('\nNew password: \033[1;32m{}\033[0m'.format(password))
	f.write("New password: {}".format(password)+'\n')
	f.close()
	print("Saved on: {}password.txt{}".format(YELLOW,END))

else:
	print("\n\033[1;31m[ERROR] \033[0;31minvalid option, exiting...\033[0m")
	time.sleep(1)
	exit()	
