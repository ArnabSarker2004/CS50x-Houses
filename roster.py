from cs50 import SQL
from sys import argv

if len(argv) != 2: #Command line argument counter requests user with the following prompt if the varoius files were not entered
    print("Usage: python roster.py House")
    exit(1)

data = SQL("sqlite:///students.db") #Database for student.data

result = {}
result = data.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first;", argv[1])

for row in result:
    n = row["middle"]
    if n != None:
        print(f"{row['first']} {row['middle']} {row['last']}, born {row['birth']}") #print the following if middle name is present
    else:
        print(f"{row['first']} {row['last']}, born {row['birth']}") #print the following if mddle name is not present

exit(0) #exit program
