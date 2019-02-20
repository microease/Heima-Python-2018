import re


def main():
    names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123"]
    for i in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", i)
        if ret:
            print("%s符合要求" % i)
        else:
            print("%s不符合要求" % i)



if __name__ == '__main__':
    main()
