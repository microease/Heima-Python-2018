# coding:utf-8
from lxml import etree
text = """
  <div class="new">
      <ul>
                <li><span>2019-04-08</span><a href="http://sz.91.cn/ccy/1357.html">怎样去痘印青春痘疤痕</a></li>
                <li><span>2019-04-08</span><a href="http://sz.91.cn/sgz/1356.html">油性皮肤应该怎样护肤</a></li>
                <li><span>2019-04-08</span><a href="http://sz.91.cn/hhb/1355.html">维生素e擦脸多久祛斑</a></li>
                <li><span>2019-04-08</span><a href="http://sz.91.cn/qdd/1354.html">手机玩多了脸上长痘痘</a></li>
                <li><span>2019-04-08</span><a href="http://sz.91.cn/hgl/1353.html">深圳治疗汗管瘤的医院</a></li>
                <li><span>2019-04-08</span><a href="http://sz.91.cn/jtlb/1352.html">深圳哪家医院可以隆鼻</a></li>
                <li><span>2019-04-08</span><a href="http://sz.91.cn/slz/1351.html">打瘦脸针5个月了好丑</a></li>
                <li><span>2019-04-04</span><a href="http://sz.91.cn/zfl/1350.html">眼睛下面长脂肪粒怎么</a></li>
                <li><span>2019-04-04</span><a href="http://sz.91.cn/ztzf/1349.html">深圳阳光整形怎么样自</a></li>
                <li><span>2019-04-04</span><a href="http://sz.91.cn/qyd/1348.html">深圳市祛眼袋的医院哪</a></li>
                <li><span>2019-04-04</span><a href="http://sz.91.cn/hhb/1347.html">深圳市祛斑的医院哪家</a></li>
                <li><span>2019-04-04</span><a href="http://sz.91.cn/hyq/1346.html">去黑眼圈比较有效的方</a></li>
                <li><span>2019-04-04</span><a href="http://sz.91.cn/slz/1345.html">脸瘫过的人可以打瘦脸</a></li>
                <li><span>2019-04-04</span><a href="http://sz.91.cn/hhb/1344.html">黄褐斑的简单去除方法</a></li>
                <li><span>2019-04-04</span><a href="http://sz.91.cn/tbtm/1343.html">深圳脱毛医院排名</a></li>
                      </ul>
    </div>


"""
html = etree.HTML(text)
print(html)
print(etree.tostring(html).decode())