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




for i in files_list:

	space = i.find(" ")

	if space != -1:
		os.system("mv " + "/Ej3" + i + " " + "/Ej3" + i.replace(" ", "_"))



for i in files_list:

	#456789012
	#A01632274
	pos_a = i.find("a");

	x = i[pos_a+5:13]

	space = i.find(" ")

	if space != -1:
		os.system("mv "  + i + " "  + i.replace(" ", "_"))
		print("hi")

	if os.path.exists(x) == False:
		os.system("mkdir " + x)


	os.system("mv " + i + " " + x)


	#mv ~/Desktop/MyFile.rtf /Volumes/Backup/MyFolder




