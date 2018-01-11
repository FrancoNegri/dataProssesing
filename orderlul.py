import os, errno
f = open("datos.txt")
for line in f:
    line = line.split('\t')
    if not os.path.exists(line[0]):
        os.makedirs(line[0])
    if not os.path.exists(line[0] +  "/" +line[1]):
        os.makedirs(line[0] +  "/" +line[1])
    y = open(line[0] +  "/" +line[1] + "/" + "data.txt", "a")
    y.write(line[6])


