# Author: JAP (amdg) 12/16/20

rows = [["Darick", "Eugene", "Kyle", "Azaan"],
["Ryan", "Phil", "Eman", "Alex", "Nicholas"],
["Christian", "Josh", "Matt", "Francesco"],
["Patrick", "Nico", "Trevayne"]]

# Cant change list
last_initials = ["A", "B", "B", "D", "D", "G", "G", "J", "K", "L", "P", "S", "T", "T", "V", "W"]

for row in rows:
    for index, names in enumerate(row):
        for index2, letter in enumerate(last_initials):
            if index == index2:
                row[index] = names + " " + last_initials[index]
                print(row)

          
         
print(row)
