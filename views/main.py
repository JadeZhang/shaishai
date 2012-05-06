# -*- coding: utf-8 -*-
'''
Created on 2012-5-6

@author: jade
'''
from flask import Blueprint
from flask import g, request, session
from flask import redirect, url_for, jsonify, flash, current_app, render_template, json
from flask import make_response
import models as m
from models.tables import *
import uuid
# Flask 模块对象
module = Blueprint('main_module', __name__)


@module.route("/", methods=['GET'])
def main():
    user = m.session.query(User).one()
    raise
    return render_template("index.html",user=user)

@module.route("/login/", methods=['GET'])
def login():
    if session and session.sid and 'user_id' in session:
        return redirect('/square/')
    error = None
    email=''
    if request.method == 'POST' and "email" in request.form:
        email = request.form["email"]
        isCipher = request.form.get("isCipher", "").lower() == 'true'
        remember = request.form.get('remember', None) == 'on'
        try:
            user = m.session.query(User).filter_by(email = email).one()
        except:
            user = None
        if user:
            password = request.form.get("password", "")
            if not isCipher:
                password = hashlib.md5(password).hexdigest()
            if user.password == password:                
                _update_session(user)
                session['client_type'] = 'browser'
                if remember:
                    session.permanent = True
                if user.password_status == 1:
                    return redirect('/firstlogin/')
                if 'next' in request.args:
                    return redirect(request.args['next'])
                return redirect("/home/")
            else:
                error = 'invalid'
        else:
            error = 'invalid'
    return render_template("login.html", error = error,email=email)
