# -*- coding: utf-8 -*-
# @Author: ioriiod0
# @Date:   2017-07-12 13:25:03
# @Last Modified by:   ioriiod0
# @Last Modified time: 2017-07-13 23:51:27

from flask_server import redis
import json
import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/chatbot')
sys.path.append(os.getcwd()+'/chatbot/corpus')

args_in = '--device gpu0 ' \
          '--test daemon ' \
          '--modelTag xiaohuangji_2l_lr002_dr09_emb256_len20_vocab8000 ' \
          '--vocabularySize 8000 --maxLength 20 ' \
          '--learningRate 0.002 --dropout 0.9 ' \
          '--rootDir /var/www/chitbot/DeepQA ' \
          '--saveEvery 500 ' \
          '--corpus xiaohuangji '.split() # --datasetTag wechat ' \


from chatbot import chatbot
def init():
    bot = chatbot.Chatbot()
    bot.main(args_in)
    return bot

def predict(bot, query):
    print(query)
    response = bot.daemonPredict(query)
    _save_to_redis(query, response)
    return response.replace(" ", "")



def _save_to_redis(query, response):
    k = "chatbot"
    v = json.dumps({"query": query, "response": response}, ensure_ascii=False)
    redis.lpush(k,v)

