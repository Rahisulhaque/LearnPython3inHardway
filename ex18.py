# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex18.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisulhaque <rahisul@icloud.com>              / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2022/09/02 09:42:59 by rahisulhaque     /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2022/09/02 10:37:22 by rahisulhaque                                             #
#                                                                                             #
# ******************************************************************************************* #

#this script is with argv

def print_two(*args):
	arg1, arg2 = args
	print(f"arg1:{arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
	print(f"arg1:{arg1}, arg2: {arg2}")

def print_one(arg1):
	print(f"arg1:{arg1}")

def print_none():
	print(f"I got nothing.")


print_two("Monty", "Python")
print_two_again("Monty", "Python")
print_one("First!")
print_none()
