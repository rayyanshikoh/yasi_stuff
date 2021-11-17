filename = 'file.txt'
f = open(filename, 'a')
f.writelines("1) Yasi\n2) you\n3) lol\n")
f.close()

f = open(filename, 'r')
contents = f.readlines()
for x in contents:
    print(x)