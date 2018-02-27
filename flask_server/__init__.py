# -*- coding: utf-8 -*- 
# @Author: Shuang0420 
# @Date: 2017-08-30 16:53:31 
# @Last Modified by:   Shuang0420 
# @Last Modified time: 2017-08-30 16:53:31 


from flask import Flask
from flask_redis import FlaskRedis

app = Flask("Chatbot_API")
app.config.from_object("flask_server.config")
redis = FlaskRedis(app, decode_responses=True)

import flask_server.views
import flask_server.models
