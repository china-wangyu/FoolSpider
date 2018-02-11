from bs4 import BeautifulSoup
import requests
import random

'''
 * @authors china_wangyu (china_wangyu@aliyun.com)
 * @date    2018-02-11 12:39:30
 * @version 1.0.1
'''


class Agent(object):
    """
    爬虫代理IP
    """

    def __init__(self):
        self.url = 'http://www.xicidaili.com/nn/'
        self.headers = {
            'User-Agent': self.get_random_agent()[0]
        }
        pass
        ip_list = self.get_ip_list(self.url, self.headers)
        ip = self.get_random_ip(ip_list)
        self.ip = ip

    def get_ip_list(self, url, headers):
        """
        获取代理IP列表
        :param url:获取代理IP网站
        :param headers:网站头部信息
        :return:代理IP集合
        """
        web_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(web_data.text, 'html.parser')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[1].text + ':' + tds[2].text)
        return ip_list

    def get_random_ip(self, ip_list):
        """
        获取代理随机IP
        :param ip_list: 代理IP集合
        :return: 随机IP
        """
        proxy_list = []
        for ip in ip_list:
            proxy_list.append('http://' + ip)
        proxy_ip = random.choice(proxy_list)
        proxies = {"http": proxy_ip}
        return proxies

    def get_random_agent(self, boolen=True):
        headers = [
            'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
            'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
            'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
        ]
        if boolen == True:
            return random.sample(headers, 1)
