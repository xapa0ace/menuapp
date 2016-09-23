#!/user/bin/env python
# -*- coding: utf-8 -*-
# FileName: sqlpy_ce
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric

# SQLiteデータ管理
# 管理用ID、日付、優先度、テーブル、ユーザーID、
# 注文ID、子機のID、時間、注文したやつ、数量、状況(進行度)、イメージファイル紐付け
class Menu():
    engine = create_engine('sqlite:///db.sqlite3.menus', echo=True)
    metadata = MetaData()
    metadata.bind = engine
    menus = Table(
      'menus', metadata,
      Column('id', Integer, primary_key=True),
      Column('name', String),
      Column('price', Integer),
      Column('category_main', Integer),
      Column('category_sub', Integer),
      Column('img', String)
    )
