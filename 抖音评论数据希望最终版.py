from DrissionPage import ChromiumPage
from time import sleep
import datetime
import csv

f = open('data.csv',mode='w',encoding='utf-8-sig',newline='')
csv_writer = csv.DictWriter(f, fieldnames=['昵称','地区','时间','评论内容','点赞数'])
csv_writer.writeheader()

# 创建一个ChromiumPage实例
driver = ChromiumPage()

# 开始监听网络请求
driver.listen.start('aweme/v1/web/comment/list/')

# 打开抖音登录页面
driver.get('https://www.douyin.com/user/self?modal_id=7362158512966847807&showTab=favorite_collection')
for page in range(50):
    print(f'正在采集第{page+1}页的数据内容')
    driver.scroll.to_bottom()


    resp = driver.listen.wait()

        # 获取JSON响应体
    json_data = resp.response.body
    comments = json_data['comments']
    for index in comments:
        text = index ['text']
        nickname = index['user']['nickname']
        create_time = index['create_time']
        digg_count = index['digg_count']
        date = str(datetime.datetime.fromtimestamp(create_time))
        ip_label = index['ip_label']
        dit = {
            '昵称':nickname,
            '地区':ip_label,
            '时间':date,
            '评论内容':text,
            '点赞数':digg_count
        }


        csv_writer.writerow(dit)
        print(dit)


