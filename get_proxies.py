import requests
import json
from bs4 import BeautifulSoup

SSL = 'https://www.sslproxies.org/'
FREE_PROXY = 'https://free-proxy-list.net/'
SOCK_PROXY = 'https://www.socks-proxy.net/'
ANON_PROXY = 'https://free-proxy-list.net/anonymous-proxy.html'
SPYS_ME = 'https://spys.one/free-proxy-list/'
SPYS_TXT = 'http://spys.me/proxy.txt'
PROXYSCRAPE = 'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=us&ssl=all&anonymity=all'
PROXYNOVA = 'https://www.proxynova.com/proxy-server-list/'
PROXYLIST_DOWNLOAD_HTTP = 'https://www.proxy-list.download/HTTP'
PROXYLIST_DOWNLOAD_HTTPS = 'https://www.proxy-list.download/HTTPS'
PROXYLIST_DOWNLOAD_SOCKS4 = 'https://www.proxy-list.download/SOCKS4'
PROXYLIST_DOWNLOAD_SOCKS5 = 'https://www.proxy-list.download/SOCKS5'

def free_proxy(region):
    total_proxy = []
    
    for i in (SSL,FREE_PROXY,SOCK_PROXY,ANON_PROXY):
        
        proxy_list = []
        
        print(i)
        page  = requests.get(i)
        soup  = BeautifulSoup(page.content, 'html.parser')
        table =  soup.find("table", {"id": "proxylisttable"})
        table_body = table.find('tbody')   

        for row in table_body:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            print(cols)
            if region == "ALL":    
                proxy_list.append([ele for ele in cols if ele])
            else:
                proxy_list.append([ele for ele in cols if cols[2] == region])

        proxy_list = [x for x in proxy_list if x != []]
        print(proxy_list)
        proxy_list = [x[0]+":"+x[1] for x in proxy_list]
        
        print("LIST COME HERE")
        print(proxy_list)
        total_proxy +=proxy_list
    
    return total_proxy