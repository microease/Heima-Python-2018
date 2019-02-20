import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, '1.jpg',
                     'http://rpic.douyucdn.cn/live-cover/appCovers/2018/04/19/4108896_20180419012844_small.jpg'),
        gevent.spawn(downloader, '2.jpg',
                     'http://rpic.douyucdn.cn/live-cover/appCovers/2018/09/26/1864921_20180926212457_small.jpg')

    ])


if __name__ == '__main__':
    main()
