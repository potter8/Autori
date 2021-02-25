name = input()
abv = name[0]
for i in range(len(name)):
    if name[i] == "-":
        abv += name[i+1]
print(abv)