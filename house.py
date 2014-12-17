#!/usr/bin/env python

"""
  Arguments:
    (int) width of house (optional)

  Usage: ./house.py 45

  Todo: the names in this script are hardcoded and need
  to come from the user list instead

"""
import sys
from random import shuffle

house_width = 40
if(len(sys.argv) == 2):
	house_width = int(sys.argv[1])

users = ['Peter', 'Caridad', 'Jadwiga', 'Scottie', 'Edison', 'Dominick', 'Wilbert', 'Jasper', 'Roel', 'Ed', 'Jiskar', 'Alexander', 'Ferdinand', 'Bob']
shuffle(users)

house_middle = ''

while len(users) > 0:
	line_1 = "| "
	line_2 = "| "
	line_3 = "| "
	line_4 = "| "

	to_pop = []
	user_index = 0;

	for user in users:
		if len(line_1) + len(user) + 5 < house_width:
			line_1 += "  _" +"_"*len(user)+ "_  "
			line_2 += " | " +" "*len(user)+ " | "
			line_3 += " | " + user + " | "
			line_4 += " |_" +"_"*len(user)+ "_| "
			to_pop.append(user_index)
		user_index += 1
	
	popped = 0
	for index in to_pop:
		users.pop(index-popped)
		popped += 1

	house_middle += line_1 + ((house_width-len(line_1))*" ") + " |" + "\n"
	house_middle += line_2 + ((house_width-len(line_2))*" ") + " |" + "\n"
	house_middle += line_3 + ((house_width-len(line_3))*" ") + " |" + "\n"
	house_middle += line_4 + ((house_width-len(line_4))*" ") + " |" + "\n"

house_middle = house_middle[:-1] # remove the last newline

house_roof = "    _____________" + ((house_width-25)*" ")+"    (o>\n\
 __|_____________|" + ((house_width-33)*"_")+"_________\( )___ \n\
|"+house_width*" " + "|"

house_bottom = "\
|                                   " + ((house_width-35)*" ")+"|\n\
|   ______     ___________________  " + ((house_width-35)*" ")+"|\n\
|  |  __  |   |  H O M E B R E W  | " + ((house_width-35)*" ")+"|\n\
|  | |  | |   |    S E R V E R    | " + ((house_width-35)*" ")+"|\n\
|  | |__| |   |      C L U B      | " + ((house_width-35)*" ")+"|\n\
|  |o     |   |___________________| " + ((house_width-35)*" ")+"|\n\
|  |      |                         " + ((house_width-35)*" ")+"|\n\
|__|______|_________________________" + ((house_width-35)*"_")+"|"

print house_roof
print house_middle
print house_bottom
