import json
import requests


#思知机器人API
def get_sizhi_response(msg):
    apiUrl = 'https://api.ownthink.com/bot'
    apiKey = '5e6b7be8087533aed33ef83dfb13fd3f'
    data = {
        "spoken": msg,
        "appid": apiKey,
        "userid": 'asong'
    }
    # 必须是json
    headers = {'content-type': 'application/json'}

    try:
        req = requests.post(apiUrl, headers = headers, data = json.dumps(data))
        return req.json()
    except:
        return

#处理思知机器人返回的json消息
def sizhi_msg(msg):
    #设置一个默认回复。
    return_msg = '我是个笨笨的机器人，我好像挂了~_~![自动回复]'
    replyjson = get_sizhi_response(msg)
    if replyjson['message'] == 'success':
        return_msg = replyjson['data']['info']['text'].replace('小思','伦家').replace('思知机器人','烟火1号');
        print("思知机器人自动回复："+return_msg)
    # a or b --》 如果a不为空就返回a，否则返回b
    return return_msg
