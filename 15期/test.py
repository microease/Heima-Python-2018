fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
res = []
fh = open(fname)
for line in fh:
    if line.startswith("From "):
        line = line.strip("From")
        line = line.strip("\n")
        line = line.split(" ")
        line = line[6].split(":")
        res.append(line[0])
List_set = set(res)
res2 = []
for item in List_set:
    # print("%s %d" % (item, res.count(item)))
    res2.append(item+" "+str(res.count(item)))
for i in sorted(res2):
    print(i)