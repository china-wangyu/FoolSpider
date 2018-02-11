from huaban.lib import Page, Agent, EsModel
from bs4 import BeautifulSoup

'''
 * @authors china_wangyu (china_wangyu@aliyun.com)
 * @date    2018-02-11 12:39:30
 * @version 1.0.1
'''

if __name__ == '__main__':
    EsModel = EsModel.EsModel()
    EsModel.connection(db='test', user='root', password='root')
    EsModel.set_table("user")
    data = {
        'name': 'test',
        'url': '123.html'
    }
    EsModel.insert(data)
    # url = 'http://www.meisupic.com/topic.php?topic_id=90'
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19"
    # }
    # agent = Agent.Agent()
    # page = Page.Page(url, headers)
    # page.set_proxy(agent.ip)
    # result = page.get_page()
    # params = {
    #     'home': 3,
    # }
    # page.set_params(params)
    # result1 = page.get_page()
    # print(result1)
