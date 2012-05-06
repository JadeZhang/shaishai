# -*- coding: utf-8 -*-
'''
Created on 2012-5-5

@author: jade
'''

from flask import Flask
import config
import models

app = Flask(__name__)

app.config.from_object(config)
app.debug = app.config.get('DEBUG', False)

# 初始化进程全局的数据模型对象
models.setup(app)


from views import main
# 注册 Flask 应用模块
app.register_blueprint(main.module)

from flask import render_template

@app.errorhandler(404)
def page_not_found(error):    
    return render_template('404.html')

# 设置logger的输出形式
import logging, os 
from logging.handlers import TimedRotatingFileHandler 
base = os.path.abspath(os.path.dirname(__file__)) 
logfile = os.path.join(base, 'logs/shaishai.log') 
handler = TimedRotatingFileHandler(filename=logfile, when='MIDNIGHT', interval=1, backupCount=14) 
handler.setFormatter(logging.Formatter('%(asctime)s  %(levelname)-8s %(message)s')) 
handler.setLevel(logging.DEBUG) 
app.logger.addHandler(handler) 
app.logger.setLevel(logging.DEBUG if app.debug else logging.INFO)


if __name__ == '__main__':
    app.run(threaded=True)


