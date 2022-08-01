# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex16.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisulhaque <rahisul@icloud.com>              / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2022/08/01 13:58:48 by rahisulhaque     /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2022/08/01 15:26:17 by rahisulhaque                                             #
#                                                                                             #
# ******************************************************************************************* #

from sys import argv

script, filename = argv

print(f"We are going to earse {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Openning the file...")
target = open(filename,'w')

print("Turncating the file. GoodBye")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close the file")
target.close()
