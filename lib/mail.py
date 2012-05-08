# -*- coding: utf-8 -*-
'''
Created on 2012-5-8

@author: jade
'''
from flask import current_app, render_template
from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib, datetime
import const

def welcome_mail(to):
    send_email(const.REGISTER_SUBJECT,to,'welcome.html',{'nickname':u'中波'})
    
    
def send_email(subject,to,template,paras):
    #创建一个带附件的实例
    msg = MIMEMultipart('alternative')
    
    #构造附件
    #att = MIMEText(open('f:\\文件名.doc', 'rb').read(), 'base64', 'gb2312')
    #att["Content-Type"] = 'application/octet-stream'
    #att["Content-Disposition"] = 'attachment; filename="文件名.doc"'
    #msg.attach(att)
    
    #加邮件头
    msg['to'] = to
    msg['from'] = current_app.config['EMAIL_FROM']
    msg['subject'] = subject
    
    tmpl=render_template('email/'+template,config=paras)
    print tmpl
    print subject
    html = MIMEText(tmpl, 'html', 'utf8')
    
    msg.attach(html)
    #发送邮件
    server = smtplib.SMTP(current_app.config['EMAIL_HOST'])
    server.login(current_app.config['EMAIL_USERNAME'],current_app.config['EMAIL_PASSWORD'])
    error=server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.close
    print error
