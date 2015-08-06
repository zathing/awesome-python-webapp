#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zathing'

from models import User, Blog, Comment
from transwarp import db

db.create_engine(user='www-data', password='www-data', database='awesome')

# u = User(name='Admin', email='admin@example.com', password='123456', image='about:blank')
# u.insert()
# print('new user id:', u.id)
# u1 = User.find_all()
# print('find user\'s name:', u1.name)
# u1.delete()
# u2 = User.find_first('where email=?', 'test@example.com')
# print('find user:', u2)

b = Blog(user_id='001438829058093496ac7e066b740b8b8f14b20f5e8a035000', user_name='Admin', user_image='about:blank', name = '子牙说', summary='一个全新的开始！', content = 'test')
b.insert()
print('Done')