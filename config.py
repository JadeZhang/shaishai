# -*- coding: utf-8 -*-

DEBUG = True

# 数据库连接配置
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:111111@127.0.0.1:3306/shaishai?charset=utf8'

# 数据库连接池最大连接数
SQLALCHEMY_POOL_SIZE = 45

# 数据库连接池最大允许过载数
SQLALCHEMY_POOL_MAX_OVERFLOW = 45

UPLOAD_FOLDER='/tmp'
