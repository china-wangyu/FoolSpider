from urllib import request, parse

'''
 * @authors china_wangyu (china_wangyu@aliyun.com)
 * @date    2018-02-11 12:39:30
 * @version 1.0.1
'''


class Page(object):
    """
        创建爬虫类
    """

    def __init__(self, url='', headers={}, params={}):
        self.url = url
        self.headers = headers
        self.params = params
        self.proxy = {}

    def set_url(self, url):
        self.url = url

    def set_headers(self, headers):
        self.headers = headers

    def set_params(self, params={}):
        self.params = params

    def set_proxy(self, proxy=False):
        if not proxy:
            self.proxy = proxy
            proxy = request.ProxyHandler(self.proxy)
            opener = request.build_opener(proxy)
            request.install_opener(opener)

    def get_page(self):
        new_url = "%s?%s" % (self.url, parse.urlencode(self.params))
        req = request.Request(url=new_url, headers=self.headers)
        try:
            connect = request.urlopen(req)
            result = connect.read().decode("utf-8")
        except request.HTTPError:
            result = ''
            pass
        return result
