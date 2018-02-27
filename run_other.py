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
#           '--modelTag other_2l_lr002_dr09_emb64_len20_vocab8000 ' \
#           '--initEmbeddings ' \
#           '--embeddingSource news_12g_baidubaike_20g_novel_90g_embedding_64.bin ' \
#           '--filterVocab 2 ' \
#           '--vocabularySize 8000 --maxLength 20 ' \
#           '--learningRate 0.002 --dropout 0.9 ' \
#           '--rootDir /Users/xushuang/sf/chatbot/DeepQA/ ' \
#           '--saveEvery 500 ' \
#           '--corpus other '.split() # --datasetTag wechat ' \

args_in = '--device gpu0 ' \
          '--modelTag other_2l_lr002_dr09_emb64_len20_vocab8000 ' \
          '--skipLines ' \
          '--filterVocab 2 ' \
          '--vocabularySize 8000 --maxLength 20 ' \
          '--learningRate 0.001 --dropout 0.9 ' \
          '--rootDir /Users/xushuang/sf/chatbot/DeepQA/ ' \
          '--saveEvery 500 ' \
          '--corpus other '.split() # --datasetTag wechat ' \

from chatbot import chatbot
print(args_in)
chatbot = chatbot.Chatbot()
chatbot.main(args_in)
# print(chatbot.daemonPredict("工作"))