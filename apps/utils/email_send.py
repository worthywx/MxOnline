# coding=utf-8
__author__ = "worthy"
__date__ = '2017/10/30 20:28'
from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = generate_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = u""
    email_body = u""

    if send_type == "register":
        email_title = u"慕学在线网注册激活链接"
        email_body = u"请点击下面的链接激活账号: http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = u"慕学在线网密码重置链接"
        email_body = u"请点击下面的链接重置: http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

def generate_random_str(randomlength=8):
    str = ''
    chars = 'ABCDEFGHIJKLIMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
