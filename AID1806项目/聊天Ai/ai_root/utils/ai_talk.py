import urllib.request
import urllib.parse
import time
import json


class airoot(object):
    """
    智能机器人API接口说明
    支持功能：天气、翻译、藏头诗、笑话、歌词、计算、域名信息/备案/收录查询、IP查询、手机号码归属、人工智能聊天
    接口地址：http://api.qingyunke.com/api.php?key=free&appid=0&msg=关键词
    　　　　　key　固定参数free
    　　　　　appid 设置为0，表示智能识别，可忽略此参数
    　　　　　msg　关键词，请参考下方参数示例，该参数可智能识别，该值请经过 urlencode 处理后再提交
    返回结果：{"result":0,"content":"内容"}
    　　　　　result　状态，0表示正常，其它数字表示错误
    　　　　　content　信息内容

    ☆ msg值在提交前请先经过 urlencode 处理，否则部分字符可能无法正确处理
    ☆ 返回结果中{br}表示换行，请自行替换成需要的代码
    """
    def __init__(self):
        self.url = r'http://api.qingyunke.com/api.php?%s'
        self.data = {
            'key':'free',
            'appid':0,
            'msg':''
        }


    def getword(self, word=''):
        self.data['msg'] = word
        if self.data['msg'] == '':
            self.data['msg'] = '你不说话, 我来撩你吧'
        self.params = urllib.parse.urlencode(self.data)
        self.url = self.url % self.params

        self.page = urllib.request.urlopen(self.url).read()
        self.res = json.loads(self.page)
        self.res['content'] = self.res['content'].replace('{br}',' ')

        print(self.res)
        return self.res
