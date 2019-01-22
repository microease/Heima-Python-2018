# with open

f = open('../../xx.xx','a')
f.write("hello world")
f.close()

# 用with
with open("../../xx.xx",'a') as f:
    f.write("hello world")
