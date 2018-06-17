f = open('D:/Programming/Pycharm/Lr1/file1.xml')
fw = open('D:/Programming/Pycharm/Lr1/file1.jtr', 'w')
P = CH = False
p = 0
ch = 0
n = 0
lvl = 0
line = f.readline()
while line:
    if "tree" in line:
        line = f.readline()
    if "parents"  in line:
        lvl += 1
        p += 1
        P = True
        CH = False
        p = ch = 0
        line.split()
        line = f.readline()
    elif "children" in line:
        lvl += 1
        p += 1
        CH = True
        P = False
        line = f.readline()
    else:
        if P:
            n += 1
            fw.writelines([str(lvl), "\t", str(0), str(0), line])
        if CH:
            ch += 1
            fw.writelines([str(lvl),"\t", str(n-1), str(n), line])
        line = f.readline()
f.close()
fw.close()