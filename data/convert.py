import sys
fname = sys.argv[1]
with open(fname, 'r') as fr:
    with open(fname.split('.')[0] + '.conv', 'w') as fw:
        fw.write("E\n")
        for line in fr:
            if len(line)>1:
                fw.write("M %s" % line)
            else:
                fw.write("E\n")
            
