from distutils.core import setup

setup(
    name="hyk_message",
    version="1.0",
    description="消息模块",
    long_description="接收和发送消息模块",
    # auhtor="microease",
    author_email="microease@gmail.com",
    url="http://www.wzxdm.com",
    pymodules=["hyk_message.send_message", "hyk.message.receive_message"]

)
