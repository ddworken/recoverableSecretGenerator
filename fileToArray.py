#!/bin/python
#A crappy program to convert a text file  delimited by spaces to an array for python. 
#DOES NOT DO ANY ERROR CHECKING!
import csv
csv.QUOTE_ALL=True
filename = raw_input("Name of file containing array data separated by spaces: ")
arrayname = raw_input("What is the name of the array: ")
with open(filename, 'rb') as i:
    reader = csv.reader(i)
    for row in reader:
        print arrayname + " = " + str(row).replace(' ', '\',\'')

