import requests


class Question5():
    def __init__(self):
        self.url = 'http://match.yuanrenxue.com/api/match/5?page={}&m=1610885245242&f=1610885244000'
        self.headers_front = {
            "Host": "match.yuanrenxue.com",
            "Connection": "keep-alive",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://match.yuanrenxue.com/match/3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        self.headers_last = {
            "Host": "match.yuanrenxue.com",
            "Connection": "keep-alive",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "yuanrenxue.project",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://match.yuanrenxue.com/match/3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }

    def get_response(self, page):
        if page <= 3:
            response = requests.get(self.url.format(page), headers=self.headers_front)
        else:
            response = requests.get(self.url.format(page), headers=self.headers_last)
        print(response.content.decode())
        print(response.status_code)

    def run(self):
        self.get_response(4)


if __name__ == '__main__':
    q5 = Question5()
    q5.run()
