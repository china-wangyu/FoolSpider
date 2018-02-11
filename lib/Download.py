import time, urllib, os

'''
 * @authors china_wangyu (china_wangyu@aliyun.com)
 * @date    2018-02-11 12:39:30
 * @version 1.0.1
'''


class Download(object):

    def save_img(self, file_path, img_src):
        """
        保存图片
        :param file_path: 下载路径
        :param img_src:  图片src路径
        :return:
        """
        if os.path.exists(file_path) == False:
            os.makedirs(file_path)
        img_name = img_src.rsplit("/", 1)[1]
        down_path = os.path.join(file_path, img_name)
        urllib.urlretrieve(img_src, down_path)
        time.sleep(3)
        print("下载完成")
