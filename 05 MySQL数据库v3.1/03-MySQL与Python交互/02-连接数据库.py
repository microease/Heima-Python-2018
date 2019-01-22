from pymysql import *


class JD(object):
    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='root', password='mysql', database='jing_dong',
                            charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        sql = "select * from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    @staticmethod
    def price_menu():
        print("京东")
        print("1:显示所有的商品")
        print("2:所有的商品分类")
        print("3：所有的商品品牌分类")
        return input("请输入功能对应的序号")

    def run(self):
        while True:
            num = self.price_menu()
            if num == "1":
                self.show_all_items()
            elif num == "2":
                self.show_cates()
            elif num == "3":
                self.show_brands()
            else:
                print("输入有误")


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()
