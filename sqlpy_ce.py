#!/user/bin/env python
# -*- coding: utf-8 -*-
# FileName: sqlpy_ce
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric

# SQLiteデータ管理
# ユーザーID、
# 管理用ID、日付、優先度、テーブル、
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
      Column('content', String),
      Column('times', Integer),
      Column('img', String)
    )

class Title_Menu():
    engine = create_engine('sqlite:///db.sqlite3.title_menus', echo=True)
    metadata = MetaData()
    metadata.bind = engine
    menus = Table(
      'menus', metadata,
      Column('id', Integer, primary_key=True),
      Column('name', String),
      Column('category_main', Integer),
      Column('content', String),
      Column('sub_content', String),
      Column('img', String)
    )


class Table_db():
    engine = create_engine('sqlite:///db.sqlite3.table_db', echo=True)
    metadata = MetaData()
    metadata.bind = engine
    menus = Table(
      'menus', metadata,
      Column('id', Integer, primary_key=True),
      Column('table_id', String),
      Column('price', Integer),
      Column('date', Integer),
      Column('times', Integer),
      Column('orders', String),
      Column('content', String)
    )
