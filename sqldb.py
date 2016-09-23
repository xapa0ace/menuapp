#!/user/bin/env python
# -*- coding: utf-8 -*-
# テスト用コード
import sqlite3,sys,os

dbname = 'database_0.db'

conn = sqlite3.connect(dbname)
con = conn.cursor()
dbdeta = u'CREATE TABLE menu(id serial, name text, price int, category text)'
con.execute(dbdeta)

sql = 'INSERT INTO menu (name, price, category) VALUES (?,?,?)'
menu = (u'からあげ', 500, u'一品盛り')
con.execute(sql, menu)

insert_sql = 'INSERT INTO menu (name, price, category) VALUES (?,?,?)'
menu = [
    (u'串盛り', 1000, u'一品盛り'),
    (u'ビール', 400, u'飲み物'),
    (u'カクテル', 450, u'飲み物'),
    (u'ポテトフライ', 350, u'一品盛り')
]
con.executemany(insert_sql, menu)
conn.commit()

select_sql = 'select * from menu'
for row in con.execute(select_sql):
    print(row)

conn.close()
