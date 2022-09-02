# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex17.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisulhaque <rahisul@icloud.com>              / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2022/08/01 15:32:46 by rahisulhaque     /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2022/09/02 09:40:02 by rahisulhaque                                             #
#                                                                                             #
# ******************************************************************************************* #

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line

in_file = open(from_file)
indata = in_file.read()

print(f"The input data is {len(indata)} bytes long.")
print("Ready, hit RETURN to continue, CRTL-C to abort.")

input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done!")

out_file.close()
in_file.close()
