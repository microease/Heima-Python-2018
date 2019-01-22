card_list = []


def show_menus():
    """显示菜单"""
    print("*" * 30)
    print("欢迎使用【名片管理系统】V1.0")
    print("1：新建名片")
    print("2：显示全部")
    print("3：查询名片")
    print("0：退出系统")
    print("*" * 30)


def new_card():
    """新增名片"""
    print("-" * 30)
    print("新增名片")
    # 1：提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")
    # 2：使用用户输入的名片信息建立字典
    card_dict = {"name": name_str, "phone": phone_str, "qq": qq_str, "email": email_str}
    # 3：将名片字典添加到列表中
    card_list.append(card_dict)
    # 4：提示用户添加成功
    print("添加%s的名片成功！" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 30)
    print("显示所有名片")
    # 判断是否包含名片记录，如果没有提示用户返回
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用添加名片记录")
        return
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    # 打印分割线
    print("")
    print("=" * 50)
    # 遍历名片列表输出信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """搜索名片"""
    print("-" * 30)
    print("搜索名片")
    # 提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")
    # 遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # TODO 针对找到的名片记录执行修改删除操作
            deal_card(card_dict)

            break
    else:
        print("抱歉，没有找到%s" % find_name)


def deal_card(find_dict):
    print(find_dict)
    action_str = input("请选择要执行的操作："
                       "[1]修改 [2]删除 [0]返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名:[回车不修改]")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话:[回车不修改]")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ:[回车不修改]")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱:[回车不修改]")

        print("修改名片成功!")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功!")


def input_card_info(dict_value, tip_message):
    """

    :rtype: object
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
