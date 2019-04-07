# fname = input("Enter file name: ")
# if len(fname) < 1: fname = "mbox-short.txt"
# res = []
# fh = open(fname)
# for line in fh:
#     if line.startswith("From "):
#         line = line.strip("From")
#         line = line.strip("\n")
#         line = line.split(" ")
#         line = line[6].split(":")
#         res.append(line[0])
# List_set = set(res)
# res2 = []
# for item in List_set:
#     # print("%s %d" % (item, res.count(item)))
#     res2.append(item + " " + str(res.count(item)))
# for i in sorted(res2):
#     print(i)
name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
res = []
count = 0
for line in handle:
    if line.startswith("From "):
        line = line.strip("From")
        line = line.strip("\n")
        line = line.split(" ")
        line = line[1].split(":")

        res.append(''.join(line))

# print(set(res))
res2 = dict()
for i in set(res):
    res2[i] = res.count(i)
res2 = sorted(res2.items(), key=lambda x: x[1], reverse=True)
print(res2[0][0] + " " + str(res2[0][1]))
