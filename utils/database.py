# Author Cuber
# coding=utf-8
# @Time    : 2021/1/30 19:07
# @Site    :
# @File    : database.py
# @Software: PyCharm

# net start mysql
# faker库用于项目测试，可以生成各种伪数据
# ORMk框架：把关系数据库的表结构映射到对象上

from sqlalchemy import Column, String, Integer, create_engine, Index, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from faker import Factory

# faker库用于项目测试，可以生成各种伪数据

# ORMk框架：把关系数据库的表结构映射到对象上

faker = Factory.create()
# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接
engine = create_engine('mysql+pymysql://Cuberan:12345678@127.0.0.1:3306/iotTest')

# 创建数据库中的表，用于还未定义表的数据库，如果在项目中我们就先自己创建好表【根据类与数据库的映射】
# Base.metadata.create_all(engine)

# 创建 Session 类型，即与数据库'对话'进行数据库的增删改查
Session = sessionmaker(bind=engine)

# 创建 session 对象
session = Session()

# 创建 worker 对象，这里使用faker.name()随机生成一个人名
# new_user = (id=4, name=faker.name())

# 添加到 session
# session.add(new_user)

# 提交到数据库
session.commit()

# 创建 Query 查询，filter 是where 条件，最后调用 one() 返回唯一行，如果调用 all() 则返回所有行
# user = session.query(worker).filter(User.id == 4).one()
# print('name:', user.name)

# 关闭 session
session.close()
