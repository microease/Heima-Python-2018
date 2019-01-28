# coding=utf-8
import unittest
from login import app
import json


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_empty_user_name_password(self):
        # 测试用户名和密码不完整的情况
        # 创建进行测试的客户端
        client = app.test_client()
        # 利用client发送请求进行测试
        ret = client.post("/login", data={})
        # ret是响应对象，data属性是响应体的数据
        resp = ret.data
        # 因为login视图返回的是json字符串
        resp = json.loads(resp)
        # 拿到返回值之后，开始断言测试
        self.assertIn("code", resp)
        self.assertIn(resp["code"], 1)
        # 测试只传用户名
        ret = client.post("/login", data={
            "user_name": "admin",
        })
        resp = ret.data
        resp = json.loads(resp)
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)
        # 测试只传密码
        ret = client.post("/login", data={"password": "admin"})
        resp = ret.data
        resp = json.loads(resp)
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

    def test_wrong_user_name_password(self):
        # 测试用户名或者密码错误的情况
        ret = self.client.post("/login", data={"user_name": "huyankai", "password": "huyankai"})

    if __name__ == '__main__':
        unittest.main()
