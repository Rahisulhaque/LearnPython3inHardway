# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex14.py                                                         __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisulhaque <rahisul@icloud.com>              / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2022/07/30 15:33:43 by rahisulhaque     /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2022/07/31 11:38:21 by rahisulhaque                                             #
#                                                                                             #
# ******************************************************************************************* #

from sys import argv

script, user_name = argv

prompt = '>'

print(f"Hi, {user_name}, I'm the {script} script.")
print("I would like to ask you some question.")
print(f"Do you like me {user_name}?")

likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
