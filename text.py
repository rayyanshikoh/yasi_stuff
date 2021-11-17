filename = 'file.txt'
with open(filename, 'a') as f:
    f.writelines("1) Yasi\n2) you\n3) lol\n")

with open(filename, 'r') as f:
    contents = f.readlines()
    for x in contents:
        print(x)