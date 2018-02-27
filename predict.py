"""
Train retrieval-based chatbot on xiaohuangji subtitle dataset.

Use python 3
"""

import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/chatbot')
sys.path.append(os.getcwd()+'/chatbot/corpus')


# args_in = '--device gpu0 ' \
#           '--test daemon ' \
#           '--modelTag other_2l_lr002_dr09_emb64_len20_vocab8000 ' \
#           '--initEmbeddings ' \
#           '--embeddingSource news_12g_baidubaike_20g_novel_90g_embedding_64.bin ' \
#           '--filterVocab 2 ' \
#           '--vocabularySize 8000 --maxLength 20 ' \
#           '--learningRate 0.002 --dropout 0.9 ' \
#           '--rootDir /Users/xushuang/sf/chatbot/DeepQA/ ' \
#           '--saveEvery 20 ' \
#           '--corpus other '.split() # --datasetTag wechat ' \

args_in = '--device gpu0 ' \
          '--test daemon ' \
          '--modelTag other_2l_lr002_dr09_emb64_len20_vocab8000 ' \
          '--skipLines ' \
          '--filterVocab 2 ' \
          '--vocabularySize 8000 --maxLength 20 ' \
          '--learningRate 0.002 --dropout 0.9 ' \
          '--rootDir /Users/xushuang/sf/chatbot/DeepQA/ ' \
          '--saveEvery 500 ' \
          '--corpus other '.split() # --datasetTag wechat ' \


# args_in = '--device gpu0 ' \
#           '--test daemon ' \
#           '--modelTag xiaohuangji_2l_lr002_dr09_emb256_len20_vocab8000 ' \
#           '--vocabularySize 8000 --maxLength 20 ' \
#           '--learningRate 0.002 --dropout 0.9 ' \
#           '--rootDir /Users/xushuang/sf/chatbot/DeepQA/ ' \
#           '--saveEvery 500 ' \
#           '--corpus xiaohuangji '.split() # --datasetTag wechat ' \


from chatbot import chatbot
def init():
    bot = chatbot.Chatbot()
    bot.main(args_in)
    return bot

def predict(bot, query):
    response = bot.daemonPredict(query)
    return response


bot = init()
print(predict(bot, "你好"))
while True:
    print(predict(bot, input("> ")))