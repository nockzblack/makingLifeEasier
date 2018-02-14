#!/usr/local/bin/python3.6

"""
	This program is a tool to organize the obteined files
	by uncompressing the .zip file that it is provided by Blackboard®,
	in order to make esaier the taks of grading.
	By: @Nockzblack -- Fernando Benavides 

"""

import os


files_list = os.listdir() # get a list of all files in the folder 

files_list.remove("test.py") # removing the file itself in order to do not lose it

"""
this for checks if there are items with " " space symbol
and rename the file on the system and updates the files_list var
Future update... Make this loop a functions in order to call the method when it is needed
"""
for strFile in files_list:

	oldName = strFile # Saves the actual file name
	newName = strFile.replace(" ", "_") # get a string replacing the first argument for the second one

	pos = 0 # the pos when the is going to begin to find
	nameChange = False

	# Finds all the " " and insert a \ before
	while (True):
		nameChange = True
		spacePos = strFile.find(" ", pos, len(strFile)) # get the pos of the " ", pos is going altere the substring where it is finded 

		# break of loop in case there isn't a space
		if (spacePos == -1):
			break

		# changes the strFile addign the "\" before the " "
		strFile = strFile[0:spacePos] + "\\" + strFile[spacePos:len(strFile)]
		pos = spacePos + 2 # update two positions because is it added a char in the strFile


	# if the flag is true we rename the file in the system...
	# for that it is needed the strFile with the "\" inserted before the " "
	if (nameChange):
		os.system("mv " + strFile + " " + newName)

	# Last of it is update the name in files_list to use it appropiete later
	index = files_list.index(oldName)
	files_list[index] = newName




for i in files_list:

	#456789012
	#A01632274
	pos_a = i.find("a");

	x = i[pos_a:13]

	if os.path.exists(x) == False:
		os.system("mkdir " + x)


	os.system("mv " + i + " " + x)




