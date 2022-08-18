import requests
import json
import pandas as pd


class Question2():
    def __init__(self):
        self.url = 'http://match.yuanrenxue.com/api/match/3?page={}'
        self.logo_url = 'http://match.yuanrenxue.com/logo'
        self.headers_front = {
            "Host": "match.yuanrenxue.com",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Accept": "*/*",
            "Origin": "http://match.yuanrenxue.com",
            "Referer": "http://match.yuanrenxue.com/match/3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        self.headers_last = {
            "Host": "match.yuanrenxue.com",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "User-Agent": "yuanrenxue.project",
            "Accept": "*/*",
            "Origin": "http://match.yuanrenxue.com",
            "Referer": "http://match.yuanrenxue.com/match/3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        self.headers_test = {
            'Proxy-Connection': 'keep-alive',
            'Content-Length': '0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Accept': '*/*',
            'Origin': 'http://match.yuanrenxue.com',
            'Referer': 'http://match.yuanrenxue.com/match/3',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def get_response(self):
        session = requests.session()
        content = []
        for i in range(3):
            session.headers = self.headers_front
            session.post(url=self.logo_url)
            response = session.get(url=self.url.format(i + 1))
            data = json.loads(response.content.decode())['data']
            for k in data:
                k['page'] = i + 1
            content.extend(data)

        for i in range(4, 6):
            session.headers = self.headers_last
            session.post(url=self.logo_url)
            response = session.get(url=self.url.format(i))
            data = json.loads(response.content.decode())['data']
            for k in data:
                k['page'] = i
            content.extend(data)
        # print(content)
        return content

    def save_data(self):
        content = self.get_response()
        df = pd.DataFrame(content)
        df.to_csv('yuanren/question3/question3.csv')

    def cal_sum(self):
        content = self.get_response()
        return sum([data['value'] for data in content])

    def run(self):
        # self.get_response()
        # self.save_data()
        print(self.cal_sum())


if __name__ == '__main__':
    q2 = Question2()
    q2.run()
