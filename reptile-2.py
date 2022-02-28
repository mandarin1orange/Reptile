import requests

def main():
    url = 'http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4750.0 Safari/537.36'
    }
    # 代理
    proxies = {'HTTP':'183.247.207.225:30001'}
    urla = url.format('1')
    print(urla)
    resp = requests.get(url=urla,headers=headers,proxies=proxies,timeout=3)  # timeout=3 设置超时参数
    with open('a.txt','wb+') as f:
        # 写入文件
        f.write(resp.content)
    pass

if __name__ == '__main__':
    main()