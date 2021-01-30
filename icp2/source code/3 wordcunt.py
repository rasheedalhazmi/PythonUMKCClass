infile = open("text.txt","r")
KeyValues = dict()

line = infile.readline()
while line != "":

    for word in line.split(" "):
        if word.strip() in KeyValues:
            KeyValues[word] += 1
        else:
            KeyValues[word.strip()] = 1
    line = infile.readline()

print(KeyValues)