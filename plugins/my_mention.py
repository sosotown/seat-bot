# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない

members = []

@respond_to('hello')
def hello_func(message):
    global members
    userID = '@' + message.channel._client.users[message.body['user']][u'name']
    if userID in members:
      msg = 'もうおるやろ'
      message.react('thinking_face')
    else:
      members.append(userID)
      members_stirng = ', '.join(members)
      msg = '現在、' + members_stirng + ' が座ってます。'
      message.react('+1')
    message.send(msg)

@respond_to('bye')
def hello_func(message):
    global members
    userID = '@' + message.channel._client.users[message.body['user']][u'name']
    if userID in members:
      members.remove(userID)
      members_stirng = ', '.join(members)
      msg = 'お疲れ様でした。現在、' + members_stirng + ' が座ってます。'
      message.react('wave')
    else:
      msg = 'どこにおるねん'
      message.react('thinking_face')
    message.send(msg)

# @default_reply()
# def default_func(message):
#     global count        # 外で定義した変数の値を変えられるようにする
#     count += 1
#     message.reply('%d 回目のデフォルトの返事です' % count)  # メンション

# @listen_to('リッスン')
# def listen_func(message):
#     message.send('誰かがリッスンと投稿したようだ')      # ただの投稿
#     message.reply('君だね？')                           # メンション

# count = 0

# @default_reply()
# def default_func(message):
#     global count        # 外で定義した変数の値を変えられるようにする
#     count += 1
#     message.reply('%d 回目のデフォルトの返事です' % count)  # メンション
