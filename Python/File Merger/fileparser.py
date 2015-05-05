# File Merger
# Given 2 large files of order of around 10M lines of records each.
# Write a program to efficiently merge these files to get a complete record set
# Dont assume order of records and keep the code memory efficient.
# Merge even the header for columns.
# eg. file1 Id , name , linkedin 1, Randy , linkedin.com
# eg. file. name , company , lead status
# Paul , XYZ, warm lead
# Randy , ABCD , cold lead
#
# eg. output file
# Id , name , linkedin , company, lead status
# 1, Randy , linkedin.com , ABCD, cold lead
# - , Paul, - , XYZ, warm lead


# start script
# python <scriptname> <file1name> <file2name> <outputfilename>
# python fileparser.py File1.txt File2.txt outputFile.txt


# importing argv for arguments management
from sys import argv
from collections import OrderedDict
# taking arguments for first file , second file, and output file
script, firstfile, secondfile, outputfile = argv
# opening first file for reading
file1handler = open(firstfile)
# opening second file for reading
file2handler = open(secondfile)
# opening output file for writing
outputfilehandler = open(outputfile, "w")
# creating two temporary files for better management and less comparison
tempfilehandler = open("tempfile1.txt", "w")
# one will be created later with file 2 handler
# tempfile2handler = open("tempfile2.txt", "w")

# copying content of file 2 for backup as line of file1 is read one by one
# and matched to each line of file 2 if match is found then the line
# is added to output file otherwise to tempfile, for next test
# this tempfile is used and unmatched contents are added to other text file
# copy content in temp string
tempstring = file2handler.read()
# adding content to backup file
tempfilehandler.write(tempstring)
# closing the buffers to save the file and save memory
tempfilehandler.close()
# flags for testing cases
fileSwitchFlag = False  # flag for switching between backup files
rowFoundFlag = False  # flag for adding content of file1 whne no rows are found
# temporary lists and dict for handling of file
# heading lists for storing headers and used for comparisons
heading1 = []  # for file 1
heading2 = []  # for file 2
# line lists for storing values and used for insertion
line1 = []  # for file 1
line2 = []  # for file 2
# Ordered dictionary for remembering the order of insertions
dictionary1 = OrderedDict()


def resetDict():
    '''resets dictionary so as to empty fields for next iteration'''
    for x in heading1:
        # inserting elements of heading of file1 with default value "-"
        # so as to fill empty fields
        OrderedDict.__setitem__(dictionary1, x, "-")
    # print dictionary1
    for x in heading2:
        # inserting elements of heading of file2 also remembering the order
        OrderedDict.__setitem__(dictionary1, x, "-")
    # print dictionary1


def writeFormatter(inputString):
    '''formats input string so as to remove brackets and inverted commas'''
    output = ''
    for x in inputString:
        output = output + x + ', '
    output = output.rstrip(', ')
    return output
# ########################################
# main operations part
# taking input for index value
index = raw_input("The index field for comparison is ")
index = index.upper()

# #######################
# heading creation
# reading first line of file1 to create the dictionaries and headers
# separated by commas
string1 = file1handler.readline().split(',')
for x in string1:  # iterating over each splitted element to add it to heading
    # stripping for spaces and converting to upper case and adding to heading 1
    heading1.append(x.strip().upper())
# print heading1
# reading first line of file2 to create the dictionaries and headers
# separated by commas
file2handler.seek(0)
string2 = file2handler.readline().split(',')
file2handler.close()
for x in string2:  # iterating over each splitted element to add it to heading
    # stripping for spaces and converting to upper case and adding to heading 2
    heading2.append(x.strip().upper())
# print heading2
# index  of indexfield in file 1
index1 = heading1.index(index)
# index  of indexfield in file 1
index2 = heading2.index(index)
# print index1, index2
resetDict()  # resetting dictionary
# outputfilehandler.writelines(str(dictionary1.keys()))
# outputfilehandler.write("\n")
# print "header created"
file1handler.seek(0)
# after creating header repeat the above steps for next fields
string1 = file1handler.readline().split(',')
while string1[0] is not '':  # reading next line until empty for file 1
    for x in string1:  # iterating over each splitted element to add it to line
        # stripping for spaces and converting to upper case and adding to line1
        line1.append(x.strip().upper())
    # print line1
    # reading first line of file2 to create the dictionaries and headers
    # separated by commas
    if fileSwitchFlag is False:
        file2handler = open("tempfile1.txt")
        tempfilehandler = open("tempfile2.txt", "w")
    else:
        file2handler = open("tempfile2.txt")
        tempfilehandler = open("tempfile1.txt", "w")
    tempstring = file2handler.readline()
    string2 = tempstring.split(',')
    while string2[0] is not '':  # reading next line until empty for file 2
        for x in string2:  # iterating over splitted element to add it to line
            # stripping for spaces and converting to upper and adding to line 2
            line2.append(x.strip().upper())
        # print line2
        if line1[index1] in line2[index2]:
            rowFoundFlag = True
            for x in range(0, len(heading1)):
                # inserting elements of heading of file1 with default value "-"
                # so as to fill empty fields
                dictionary1[heading1[x]] = line1[x]
            for x in range(0, len(heading2)):
                # inserting elements of heading of file1 with default value "-"
                # so as to fill empty fields
                dictionary1[heading2[x]] = line2[x]
            # print "adding matched row to output file"
            outputfilehandler.write(writeFormatter(dictionary1.values()))
            resetDict()  # resetting dictionary
            outputfilehandler.write("\n")
        else:
            # print "adding row to temp file"
            tempfilehandler.write(tempstring)
            # tempfilehandler.write("\n")
        tempstring = file2handler.readline()
        string2 = tempstring.split(',')
        line2 = []  # emptying line2 list for new line
    # file2handler.seek(0)
    file2handler.close()
    tempfilehandler.close()
    # handling non matched row of file 1 using rowFound FLag
    if rowFoundFlag is False:  # if row is not found
        # then for every field-key in heading 1
        for x in range(0, len(heading1)):
            # add content of line 1 to output file
            dictionary1[heading1[x]] = line1[x]
        # print "adding row to output file"
        # writing to output file formatted bby function
        outputfilehandler.write(writeFormatter(dictionary1.values()))
        resetDict()  # resetting dictionary
        outputfilehandler.write("\n")
    else:
        rowFoundFlag = False  # if row is found then changing flag value
    # reading next line in first while loop
    string1 = file1handler.readline().split(',')
    line1 = []  # resetting lists as using append mode
    # toggling flag value for switching temp files
    fileSwitchFlag = not fileSwitchFlag
    # print string1
# opening tempfile so as to write left out lines in output file
file2handler = open("tempfile2.txt")
string2 = file2handler.readline().split(',')
while string2[0] is not '':
    for x in string2:  # iterating over splitted element to add it to line
            # stripping for spaces and converting to upper and adding to line 2
        line2.append(x.strip().upper())
    for x in range(0, len(heading2)):
        # inserting elements of heading of file1 with default value "-"
        # so as to fill empty fields
        dictionary1[heading2[x]] = line2[x]
    # print "adding row to output file"
    outputfilehandler.write(writeFormatter(dictionary1.values()))
    resetDict()  # resetting dictionary
    outputfilehandler.write("\n")
    string2 = file2handler.readline().split(',')
    line2 = []
# print 'd', line2
# print dictionary1
# ###########################
# closing all output files for saving
outputfilehandler.close()
print "Output File Created"
tempfilehandler.close()
file2handler.close()
