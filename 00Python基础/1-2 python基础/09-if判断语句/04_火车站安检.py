has_ticket = True
knife_length = 122
if has_ticket:
    if knife_length >= 20:
        print("不允许上车")
        exit()
    else:
        print("可以上车")
else:
    print("去买票")
