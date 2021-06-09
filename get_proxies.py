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

def downloadsocks(mode):
	if mode == "socks4":
		f = open("socks4.txt",'wb')
		try:
			r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxyscan.io/download?type=socks4",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",timeout=5)
			f.write(r.content)
			f.close()
		except:
			f.close()
		try:
			r = requests.get("https://www.socks-proxy.net/",timeout=5)
			part = str(r.content)
			part = part.split("<tbody>")
			part = part[1].split("</tbody>")
			part = part[0].split("<tr><td>")
			proxies = ""
			for proxy in part:
				proxy = proxy.split("</td><td>")
				try:
					proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
				except:
					pass
				out_file = open("socks4.txt","a")
				out_file.write(proxies)
				out_file.close()
		except:
			pass
		print("> Have already downloaded socks4 list as socks4.txt")
	if mode == "socks5":
		f = open("socks5.txt",'wb')
		try:
			r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxyscan.io/download?type=socks5",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",timeout=5)
			f.write(r.content)
			f.close()
		except:
			f.close()
		print("> Have already downloaded socks5 list as socks5.txt")

def proxy_archive():

    from datetime import datetime

    archive_api = f"https://checkerproxy.net/api/archive/{datetime.today().strftime('%Y-%m-%d')}"
    proxy_archive = requests.get(archive_api).json()

    proxy_list = [i['addr'] if i['timeout'] < 3001 else None for i in proxy_archive]
    proxy_list = [i for i in proxy_list if i]

    return proxy_list

def free_proxy(region):
    total_proxy = []    
    
    for i in (SSL,FREE_PROXY,SOCK_PROXY,ANON_PROXY):
        
        proxy_list = []
        
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
        
        # print("LIST COME HERE")
        # print(proxy_list)
        total_proxy +=proxy_list
    
    archive = proxy_archive()
    total_proxy += archive

    return total_proxy