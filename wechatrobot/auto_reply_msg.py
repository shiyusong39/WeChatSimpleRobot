##机器人自动回复消息
import itchat
from itchat.content import *
import time
import os
import mp3_2_wav
import sizhi_robot


##个人聊天
#文本信息
@itchat.msg_register([itchat.content.TEXT,itchat.content.RECORDING],isFriendChat=True)
def private_text_chat(private_msg):
    if private_msg['ToUserName'] == 'filehelper' :
        #获取好友昵称
        nick_name = '自己'
        from_user_name = 'filehelper'
    else:
        nick_name = private_msg['User']['NickName']
        from_user_name = private_msg['FromUserName']

    #语音识别及处理
    if private_msg['MsgType'] == 34:
        #保存语音到本地
        voice_file = private_msg['FileName']
        private_msg['Text'](voice_file)

        #调用语音识别方法
        filePath = os.getcwd()+'\\'+voice_file
        fileName = voice_file.replace('mp3','wav')
        isDeal = mp3_2_wav.dealMp3(filePath, fileName)
        if isDeal:
            content = mp3_2_wav.voice2Text(fileName)
            print('Google翻译：'+content)

        #删除语音文件
        if os.path.exists(os.getcwd()+'\\'+fileName):
            #删除文件，可使用以下两种方法。
            os.remove(os.getcwd()+'\\'+fileName)
        msg = content

    else:
        #获取好友消息
        msg = private_msg['Text']
        print(nick_name +":"+msg)
    #请求机器人
    replymsg = sizhi_robot.sizhi_msg(msg)
    #返回消息
    itchat.send(msg = replymsg, toUserName = from_user_name)

#图片、录音、文件、视频、位置、名片、通知、分享等消息的处理
@itchat.msg_register([itchat.content.PICTURE,itchat.content.ATTACHMENT,itchat.content.VIDEO],isFriendChat=True)
def private_other_chat(other_msg):
    if other_msg['ToUserName'] == 'filehelper' :
        #获取好友昵称
        from_user_name = 'filehelper'
        nick_name = '自己'
    else:
        from_user_name = other_msg['FromUserName']
        nick_name = other_msg['User']['NickName']
    #获取消息类型
    other_msg_type = other_msg['MsgType']
    save_type = [3, 62, 34, 47];
    #图片、录音、文件、视频保存一下子
    if other_msg_type in save_type :
        # other_msg['Text'](other_msg['FileName'])
        itchat.send_image('defult.jpg',from_user_name)
    elif other_msg_type == 49:
        #红包消息给微信助手发提示信息
        itchat.send(nick_name+'给你发红包了！！！', toUserName=from_user_name)
    else:
        #默认回复
        itchat.send_image('defult.jpg',from_user_name)

##群聊
@itchat.msg_register([itchat.content.TEXT,itchat.content.PICTURE,itchat.content.RECORDING,itchat.content.ATTACHMENT,itchat.content.VIDEO], isGroupChat=True)
def group_chat(group_msg):
    # 消息来自于哪个群聊
    chatroom_id = group_msg['FromUserName']
    # 群聊名
    chatroom_name = group_msg['User']['NickName']
    # 发送者在群中的昵称
    username = group_msg['ActualNickName']

    # 通过群聊名查找群
    chat_lists = itchat.search_chatrooms(name = chatroom_name)

    #常聊的群
    chatroom_ids = ['ღ皇朝洗浴SPA会所ღ']
    #自己的群聊昵称
    self_nick_name = ['本群最帅的男人']

    if group_msg['MsgType'] == 1:
        print('['+chatroom_name+'(群)]->'+username+":"+group_msg['Content'])

    #如果是艾特我的,不要立即返回，休息2秒
    if group_msg['isAt'] :
        time.sleep(2)
        replymsg = sizhi_robot.sizhi_msg(group_msg['Content'])
        if group_msg['MsgType'] == 1:
            itchat.send(replymsg, chat_lists[0]['UserName'])
        else:
            itchat.send_image('defult.jpg',chat_lists[0]['UserName'])

    #判断消息是不是来自常聊的群，如果不是，直接不管
    elif chatroom_name in chatroom_ids:
        #判断消息是不是自己在群里发的消息
        if len(chat_lists) > 0 and (not username in self_nick_name) and username != '':
            replymsg = sizhi_robot.sizhi_msg(group_msg['Content'])
            if group_msg['MsgType'] == 1:
                itchat.send(replymsg, chat_lists[0]['UserName'])
            else:
                itchat.send_image('defult.jpg',chat_lists[0]['UserName'])

#微信热启动
itchat.auto_login(hotReload=True)
itchat.run()





# def main():
#     reply = SiZhiRobot.sizhi_msg("你好啊")
#     print(reply)
#     # os.remove(os.getcwd()+'\\190724-163946.mp3')
#
#     #如果该py文件作为脚本来执行时，会执行'__mian__'方法，如果作为第三方model被引用，则不会执行
# if __name__ == '__main__':
#     main()

