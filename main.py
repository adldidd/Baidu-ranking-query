import datetime
import pymysql
import Baidu
from time import sleep

web_list = [
            'inmen.cn',
            'dianjintv.cn',
            'dianjinjincai.cn',
            'shuidianjin.cn',
            'ttdianjin.cn',
            'vipdianjin.cn',
            'dianjintop.cn',
            'wedianjin.cn',
            'aidianjincai.cn',
            'dianjinask.cn',
            'www.inmen.cn',
            'www.dianjintv.cn',
            'www.dianjinjincai.cn',
            'www.shuidianjin.cn',
            'www.ttdianjin.cn',
            'www.vipdianjin.cn',
            'www.dianjintop.cn',
            'www.wedianjin.cn',
            'www.aidianjincai.cn',
            'www.dianjinask.cn'
            ]
# 要找的网址库


def push(data):
    if data:
        db = pymysql.connect("45.58.138.2", "kuaipai", "102030as.", "kuaipai")
        sql = "INSERT INTO `paiming` (`id`, `title`, `url`, `page`, `p_index`, `create_time`) VALUES (NULL, '%s', '%s', '%d', '%d','%s');" % data
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()  # 提交到数据库执行，一定要记提交哦
            print(sql, '插入成功')
        except BaseException as e:
            print(e)
            db.rollback()  # 发生错误时回滚
        db.close()
        return


def find_limi():
    baidu = Baidu.BaiDu('电竞竞猜平台', 6)
    for text_list in baidu:
        for itme in text_list:
            if itme['url'] in web_list:
                print('网址匹配')
                data = itme['title'], itme['url'], itme['page'], itme['index'], datetime.datetime.now()
                push(data)

        print('翻页正常，当前页数:%s' % baidu.page)


if __name__ == '__main__':
    find_limi()
