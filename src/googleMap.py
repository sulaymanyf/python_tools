import requests


def Map():
    url = "https://maps.googleapis.com/maps/api/directions/json"
    headers = {
        'authority': 'maps.googleapis.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'x-client-data': 'CK+1yQEIhLbJAQiltskBCMS2yQEIqZ3KAQioo8oBCOKoygEIl63KAQjNrcoBCO+tygEIy67KAQjKr8oB',
        'sec-fetch-site': 'none',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,tr;q=0.7',
    }

    params = (
        ('key', 'AIzaSyAhwOVsC5Z3tfbt66OBiIWt1avRezvAFKQ'),
        ('mode', 'walking'),
        ('origin', '24.48432900,118.20003000'),
        ('destination', '24.48225100,118.19869800'),
        ('language', 'en'),
        ('units', 'metric'),
        ('region', 'CHN'),
    )

    response = requests.get(url, headers=headers, params=params)

    print(response.json())


if __name__ == '__main__':
    Map()