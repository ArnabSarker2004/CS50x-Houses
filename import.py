from cs50 import SQL
from sys import argv, exit
import csv

db = SQL("sqlite:///students.db")

if len(argv) != 2: #Command line argument counter requests user with the following prompt if the varoius files were not entered
    print("Usage: python import.py students.db")
    exit(1) # Exit programn

PyFile = open(argv[1], "r") #reads over student.db and stores in 'PyFile'

CSV = csv.reader(PyFile)  #goes into csv PyFile and stores in 'CSV'

for row in CSV:

    if row[0] == "name": # if the first row is name
        continue

    name = ""
    name = ' '.join(row) #join everything between spaces
    splname = name.split() #split the string in an list of words
    NameCounter = len(splname)

    if NameCounter == 5: #if the length of the list is 5 there is a middle name
        db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", splname[0], splname[1], splname[2], splname[3], splname[4])

    elif NameCounter == 4: #if the length of the list is 4 there is not a middle name
        db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES (?, NULL, ?, ?, ?)", splname[0], splname[1], splname[2], splname[3])

exit(0) #Exit program
