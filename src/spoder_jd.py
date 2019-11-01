import requests

from lxml import html


def spider(sn):
    """爬取京东"""
    url = 'https://search.jd.com/Search'
    url1 = 'https://www.baidu.com/s?wd={0}'
    url2 = 'http://www.weidea.net/?s={0}'
    headers = {
        'authority': 'search.jd.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'sec-fetch-site': 'none',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,tr;q=0.7',
        'cookie': '__jdu=15649905307632116855848; areaId=16; ipLoc-djd=16-1315-1316-0; shshshfpa=3beb084c-5729-aa35-9dfb-5256070abb29-1566177110; shshshfpb=jOQbfL^%^2F6MA7SZf4XlMT3N^%^20g^%^3D^%^3D; user-key=f4e88d87-6e3c-4678-8d28-2a21689d2b44; cn=0; unpl=V2_ZzNtbRAERxYnDEYDeEwIAGIBRg0SA0FBJgpPXHpLWAZuVhYOclRCFX0UR11nGl8UZwUZX0tcQhZFCEdkexhdBWUFF11DVnMlRQtGZHsYbAVjBBdVSlZHF3QOQVZ4GVwCbgcWVEdecyVyCE9kS0IJa2MDQg8RV0NFdwtPVi4pXAxmBBFfS1NBE0UJdlRyGl0HYwUbX0FnCHt0RUZQfBxUDWYHEFxEUEEWdQhBXX8dVQBuMxNtQQ^%^3d^%^3d; __jdv=122270672^|2929gou.com^|t_1001374100_^|tuiguang^|cb52c51f2de443eaae3eb3890c528d5b^|1566466684389; PCSYCityID=CN_350000_350200_350203; xtest=9483.cf6b6759; qrsc=3; __jda=122270672.15649905307632116855848.1564990530.1566903226.1566954282.17; __jdc=122270672; shshshfp=02576658cbc86e312671641352243c7a; rkv=V0200; 3AB9D23F7A4B3C9B=C5P2BVU2SRGQ4IVXTKGCHCBY6S24ZIWL4GCLKVR4H2O5QZC3DHFKD4Z36PDJKFN65LDGR45255EEKSOL6P2LE2ABMY; __jdb=122270672.4.15649905307632116855848^|17.1566954282; shshshsID=edd0d675de964e7f445356e87d36a392_4_1566954292277',
    }

    params = (
        ('keyword', sn),
    )

    response = requests.get(url, headers=headers, params=params)
    print(url)
    response.encoding = 'utf-8'
    # # 获取xpathd对象
    selector = html.fromstring(response.text)
    # # 找到列表集合
    ul_list = selector.xpath('//*[@id="J_goodsList"]/ul/li')
    print(ul_list)
    print(len(ul_list))
    # # 解析对应的内容, 标题, 价格, 连接
    # 标题
    for ul in ul_list:
        title = ul.xpath('div/div[@class="p-name"]/a//text()')
        print(title)




if __name__ == '__main__':
    spider("html")