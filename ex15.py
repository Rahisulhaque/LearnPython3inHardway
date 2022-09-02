# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex15.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisulhaque <rahisul@icloud.com>              / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2022/09/02 08:46:14 by rahisulhaque     /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2022/09/02 08:54:33 by rahisulhaque                                             #
#                                                                                             #
# ******************************************************************************************* #


from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is your {filename}:")
print(txt.read())

print("Type the file name again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
