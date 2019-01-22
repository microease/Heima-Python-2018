#coding=utf-8
import re
url1 = "http://www.interoem.com/messageinfo.asp?id=35"
url2 = "http://3995503.com/class/class09/news_show.asp?id=14"
url3 = "http://lib.wzmc.edu.cn/news/onews.asp?id=769"
url4 = "http://www.zy-ls.com/alfx.asp?newsid=377&id=6"
url5 = "http://www.fincm.com/newslist.asp?id=415"
result = re.sub(r"(http://.+?/).*",lambda x : x.group(1),url2)
print(result)