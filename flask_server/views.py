# -*- coding: utf-8 -*-
# @Author: Shuang0420
# @Date:   2017-07-12 13:24:54
# @Last Modified by:   Shuang0420
# @Last Modified time: 2017-07-13 23:57:12

from flask import request,redirect,session,g,Response,render_template

from flask_server import app
from flask_server.errors import *
from flask_server.logger import *
from flask_server import models


logger = config_logger('SERVER.VIEWS', 'INFO', 'server.log')

# auth = HTTPTokenAuth('Bearer')

# ISFORMAT="%Y%m%d%H%M%S"

bot = models.init()

mydata = ""

@app.route("/chitbot/", methods=["GET"])
def p():
        return "hello"


@app.route("/chitbot/api/v1/", methods=["GET"])
def parse():
	global mydata
	req = request.args
	# .args.get('username')
	response = models.predict(bot, req['query'])
	return response
	# return {"resultmsg":response,"resultno":ERROR_OK},200
	# return render_template('index.html')

