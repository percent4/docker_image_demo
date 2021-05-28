# -*- coding: utf-8 -*-
# @Time : 2020/10/21 15:54
# @Author : Jclian91
# @File : run.py
# @Place : Yangpu, Shanghai
from flask import Flask

from common.common import logger
from config.global_conf import PROJECT_DIR

print("中文测试！")
app = Flask(__name__)
logger.info("Initialization...\nProject_dir: {}".format(PROJECT_DIR))


@app.route("/")
def index():
    string = "Hello World!"
    logger.info(string)
    return string


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
