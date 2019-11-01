import requests

headers = {
    'authority': 'eksisozluk.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,tr;q=0.7',
    'cookie': 'iq=517d53bdc52c4bc3a692f988dbf696c2; _ga=GA1.2.620573383.1569564129; __gfp_64b=TFXVskCaH4M89N6vgCXqlUb4FQGWsJ31nGqLErY07zv.p7; __gads=ID=6f74f38e4b36295c:T=1569564130:S=ALNI_MYgh2YALK9fYnllwkxVfWDZJrr1Ig; __auc=2352972716d718060ae53eba5d9; cto_lwid=518ab6da-1b6e-4b3e-9b10-f4bcec3cc4ae; OUTFOX_SEARCH_USER_ID_NCOO=812907803.9599394; cto_bundle=CaQHJl96azVSanZYTVZuVGNWTTdFb0FvJTJCN1Z4U2ZmYjZlUjVjdkRLT0M1Mkp6UFlnVTBRbWdFRElpdXNlakpEc2lQeXZiak4yczVTcnlGV2c5dkthVmYyb2ppUlhsT0NZczk0NmZ1cWlVMTB6SzFPb2dQMktwRFlVNkZvd3NBbUJwQmJQOFJtdXB5eEs0JTJCdk1yJTJGOVREYnJleEElM0QlM0Q; a=szixwIEmjlIV2ZcFC67zj9UXDhskZRlBkZSpPdb0CwW5XZkGIVIwK+Pbk3J6AP6kxNsST/io/om+p8hbom40yhdIJLL6p4EGzj3svBtmLToNf4JIi3c4HB+5d6aSlHoIxwMROWCoTVqlGwc8BuHKpHsZJu2OpaDZZoGKZQeBhU4=; sticky_id=82a3c316ed3e3d8a1e5076a1756ad1e5; ASP.NET_SessionId=4vdqzwhqrtvjxqh3dljttqz0; __RequestVerificationToken=lDwZVvD5PNavN2_C24U3O15Ho0vvgmJTQ5VnwO3E4X9UnCUedYs2cB9XdmLzqdmcYX8SQr0ANO3Ik1L_76beiMgpmTD3x1VcjyARv7KuexI1; lastnwcrtid_571=^{^}; _gid=GA1.2.1705696500.1572570061; _gat=1',
}

response = requests.get('https://eksisozluk.com/', headers=headers )


print(response.content.decode())