# ******************************************************************************************* #
#                                                                                             #
#                                                                                             #
#    ex8.py                                                          __    _            __    #
#                                                        _________ _/ /_  (_)______  __/ /    #
#    By: rahisulhaque <rahisul@icloud.com>              / ___/ __ `/ __ \/ / ___/ / / / /     #
#                                                      / /  / /_/ / / / / (__  ) /_/ / /      #
#    Created: 2022/07/27 15:43:02 by rahisulhaque     /_/   \__,_/_/ /_/_/____/___,_/_/       #
#    Updated: 2022/07/28 08:30:04 by rahisulhaque                                             #
#                                                                                             #
# ******************************************************************************************* #

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your", 
	"Own text here", 
	"Maybe a poem", 
	"Or a song about fear"
	))

