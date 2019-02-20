def sum_nums(num):
    print(num)
    if num ==1:
        return
    sum_nums(num -1)

sum_nums(9)