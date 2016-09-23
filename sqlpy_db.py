#!/user/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlpy_ce import Menu
from db import staff_db

class menus():
    try:
        # id = Column(Integer, primary_key=True)
        # name = Column(String)
        # price = Column(Integer)
        # category_main = Column(Integer)
        # category_sub = Column(Integer)
        # img = Column(String)
        Menu.menus.insert().execute(name=u'たこわさ', price=450, category_main=1, category_sub=1, img='../static/img/takowasa.jpg')


    except:
        Menu.menus.metadata.create_all()
        print ("? Error")


class staffs():
    staff_db.metadata.create_all()
