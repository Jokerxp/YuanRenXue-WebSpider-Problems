import hashlib
import requests
import pandas as pd
import execjs
import os
import json


class Question1():
    def __init__(self):
        self.url = 'http://match.yuanrenxue.com/api/match/1?page={page}&m={param}%E4%B8%A8{timestamp}'
        self.headers_front = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
        self.headers_last = {'User-Agent': 'yuanrenxue.project'}

    def cal_param(self):
        with open('yuanren/question1/question1.js', 'r', encoding='utf8') as f:
            question1 = f.read()
        psd = execjs.compile(question1).call('get_value')
        return psd['m'], psd['timestamp']

    def get_response(self):
        content = []
        for i in range(3):
            m, timestamp = self.cal_param()
            response = requests.get(url=self.url.format(page=i + 1, param=m, timestamp=timestamp),
                                    headers=self.headers_front)
            data = json.loads(response.content.decode())['data']
            for k in data:
                k['page'] = i + 1
            content.extend(data)

        for i in range(4, 6):
            m, timestamp = self.cal_param()
            response = requests.get(url=self.url.format(page=i, param=m, timestamp=timestamp),
                                    headers=self.headers_last)
            data = json.loads(response.content.decode())['data']
            for k in data:
                k['page'] = i
            content.extend(data)
        return content

    def save_data(self):
        content = self.get_response()
        df = pd.DataFrame(content)
        df.to_csv('yuanren/question1/question1.csv')

    def cal_sum(self):
        content = self.get_response()
        value_list = [data['value'] for data in content]
        res = sum(value_list)
        print(res)

    def run(self):
        # self.get_response()
        self.save_data()
        self.cal_sum()


if __name__ == '__main__':
    print(os.getcwd())
    q1 = Question1()
    q1.run()
