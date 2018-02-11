import pymysql.cursors

'''
 * @authors china_wangyu (china_wangyu@aliyun.com)
 * @date    2018-02-11 12:39:30
 * @version 1.0.1
'''


class EsModel(object):

    def __init__(self):
        self.connect = ''
        self.cursor = ''
        self.table = ''

    def connection(self, host='localhost', db='', user='', password='', port='3306', charset='utf8mb4'):
        '''
        连接数据库，使用python3扩展pymysql
        :param host: 数据库地址
        :param db: 数据库名称
        :param user: 用户名
        :param password: 密码
        :param port: 端口
        :param charset:数据库编码
        :return:连接句柄游标
        '''
        self.connect = pymysql.connect(host=host,
                                       user=user,
                                       passwd=password,
                                       db=db,
                                       charset=charset)
        self.cursor = self.connect.cursor()

    def set_table(self, table_name):
        self.table = table_name

    def insert(self, data=''):
        if not self.connect:
            return print('请先链接数据库~！')
        if not self.table:
            return print('没有要插入的数据表~！')
        if not data:
            return print('没有要插入的数据~！')
        table_keys = ','.join(data.keys())
        table_value = ''
        for key in data:
            if data[key]:
                table_value += "'" + data[key] + "',"
        sql = "INSERT INTO " + self.table + " (" + table_keys + ") VALUES (" + table_value.strip(',') + ");"
        print(sql)
        self.cursor.execute(sql)
        self.connect.commit()
