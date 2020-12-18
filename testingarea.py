rows = [["Darick", "Eugene", "Kyle", "Azaan"],
["Ryan", "Phil", "Eman", "Alex", "Nicholas"],
["Christian", "Josh", "Matt", "Francesco"],
["Patrick", "Nico", "Trevayne"]]


for row in rows:
    total = 0
    for names in row:
        print(row)


last_initials = ["A", "B", "B", "D", "D", "G", "G", "J", "K", "L", "P", "S", "T", "T", "V", "W"]

for index, letters in enumerate(last_initials):
    print(letters, index)

print(str.isupper, last_initials)

