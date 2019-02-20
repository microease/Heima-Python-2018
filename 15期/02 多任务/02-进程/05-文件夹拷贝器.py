import os
import multiprocessing


# print(os.__file__)
# /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py
def copy_file(file_name, old_folder_name, new_folder_name):
    print(file_name,old_folder_name,new_folder_name)
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()
    new_f = open(new_folder_name + "/", file_name, "wb")
    new_f.write(content)
    new_f.close()


def main():
    # 1:获取用户要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹的名字：")
    # 2：创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "1"
        os.mkdir(new_folder_name)
    except:
        pass
    # 3：获取文件夹内所有文件的名字 listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)
    # 4:创建进程池
    pool = multiprocessing.Pool(5)
    for file_name in file_names:
        pool.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))
    pool.close()
    pool.join()
    # 复制文件夹中的文件到新文件夹中的文件去


if __name__ == '__main__':
    main()
