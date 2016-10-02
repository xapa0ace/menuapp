#!/user/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file, url, get, post, response, error
from bottle import abort, redirect, os
import sys, codecs, os
import re
import bottle.ext.sqlalchemy
import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlpy_ce import Menu
from db import staff_db
import webbrowser
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

# リソース受け取りpathセット
# "{{url('static_file', filepath="...")}}"
@route("/")
def html_index():
    return template("index", url=url)

@route('/menu/<name>')
def html_task(name='Stranger'):
    return template("menu", url=url, name=name)

@route("/static/<filepath:path>", name="static_file")
def static(filepath):
    return static_file(filepath, root="./static")

@route("/static/img/<img_filepath:path>", name="static_img")
def static_img(img_filepath):
    return static_img(img_filepath, root="./static/img/")

# 管理画面
@get('/admin')
def admin():
    return template("admin", url=url)

# img ファイルアップロード
@get('/upload')
def upload():
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="submit" value="Upload"></br>
            <input type="file" name="upload"></br>
        </form>
    '''

@route('/upload', method='POST')
def do_upload():
    upload   = request.files.get('upload')

    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return 'File extension not allowed!'
    save_path = get_save_path()
    upload.save(save_path)
    return 'Upload OK. FilePath: .%s%s' % (save_path, upload.filename)

def get_save_path():
    path_dir = "./static/img/"
    return path_dir

###
###
###
@get("/login/staff") # スタッフアカウント追加
def staff():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        return template("staff", url=url, name=username)
        #template("Hello {{name}}. Welcome back.", name=username)
    else:
        return "You are not logged in. Access denied."

@route("/login/staff", method="POST")
def do_staff():
    username = "%s" % (request.forms.get("username"))
    password = "%s" % (request.forms.get("password"))
    if check_team(username, password):
        return "<p>Add OK!</p>"
    else:
        return "<p>No't Data.</p>"
def check_team(username, password):
    if username == "" and password == "":
        return False
    else:
        db.staff_db.menus.insert().execute(name=username, password=password)
        return True



@get("/login/menu_add") # メニュー追加
def menu_add():
    return template("menu_add", url=url)

@route("/login/menu_add", method="POST")
def do_menu_add():

    upload   = request.files.get('upload')

    print upload

    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return 'File extension not allowed!'

    save_path = get_save_img_path()
    upload.save(save_path)

    img = u'.%s%s' % (save_path, upload.filename)

    name = u"%s" % (request.forms.get("name"))
    price = u"%s" % (request.forms.get("price"))
    category_main = u"%s" % (request.forms.get("category_main"))
    category_sub = u"%s" % (request.forms.get("category_sub"))
    print "%s, %s, %s, %s, %s" % (name, price, category_main, category_sub, img)


    if check_request(name, price, category_main, category_sub, img):
        return "<p>Add OK! %s, %s, %s, %s, %s</p></br><a href='../login/menu_add'>Link</a>" % (name, price, category_main, category_sub, img)
    else:
        return "<p>No't Data.</p>"


def get_save_img_path():
    path_dir = "./static/img/"
    return path_dir

def check_request(name, price, category_main, category_sub, img):
    Menu.menus.insert().execute(name=name, price=price, category_main=category_main, category_sub=category_sub, img=img)
    return True

@get("/login")
def login():
    return template("login", url=url)

@route("/login", method="POST")
def do_login():
    username = request.forms.get("username")
    password = request.forms.get("password")
    if check_login(username, password):
        response.set_cookie("account", username, secret="some-secret-key")
        return template("staff", name=username, url=url)
    else:
        # db_data = db.staff_db.menus.select().execute().fetchall()
        return "<p>Failed !</p>"# % (db_data)
def check_login(username, password):
    db_data = db.staff_db.menus.select().execute().fetchall() # IDでstaffのnameをループさせる
    try:
        for db_id in range(10):
            if username == (db_data[db_id].name):
                db_name = "%s" % (db_data[db_id].name)
                db_pw = "%s" % (db_data[db_id].password)
                break
            else:
                if db_data[db_id] == "":
                    break

        if username == db_name and password == db_pw:
            return True
        else:
            return False
    except:
        pass




@error(404)
def error404(error):
    return template("404", url=url)

run(host="0.0.0.0", port=8000, debug=True, reloader=True)
