#!/user/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric

class staff_db():
    engine = create_engine('sqlite:///db.sqlite3.staff', echo=True)
    metadata = MetaData()
    metadata.bind = engine

    menus = Table(
      'menus', metadata,
      Column('id', Integer, primary_key=True),
      Column('name', String),
      Column('password', String)
    )
