# coding:utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}
cookies = "anonymid=jsvxrw7cmr9vch; depovince=GUZ; _r01_=1; ick_login=0928646c-3795-46f5-8f4c-1eecb691ec34; first_login_flag=1; ln_uact=173418535@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; JSESSIONID=abc7vUMxTvO6N_VMbGoLw; jebe_key=e019e1ef-a53a-4df7-9d44-2275b3224a59%7C383de3fdecd673fc8bbad674e1c4afa1%7C1551800215051%7C1%7C1551800215450; wp_fold=0; jebecookies=4549c6dc-9529-40ab-8b4f-937a534b214c|||||; _de=7511FBEBFB2832913399691954C56086696BF75400CE19CC; p=b176148c260c8b0b577c7ea705e182e74; t=250b1fb79e57cf245882e01c84da6cc74; societyguester=250b1fb79e57cf245882e01c84da6cc74; id=863482774; xnsid=b179014a; ver=7.0; loginfrom=null"
cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}
print(cookies)
r = requests.get("http://www.renren.com/863482774/profile", headers=headers, cookies=cookies)
print(r.status_code)
with open("renren3.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())
