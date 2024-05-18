import smtplib
from email.message import EmailMessage


def send_mail(mailto, msg, subject):
    email_from = 'sonbinh160958@gmail.com'  # email người gửi
    email_to = mailto  # email người nhận
    password = '123'  # password phải sinh ra trong bảo vệ 2 lớp bảo mật của google
    subject = subject
    body = msg
    em = EmailMessage()
    em['From'] = email_from
    em['To'] = email_to
    em['Subject'] = subject
    em.set_content(body)
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()  # Định danh trong stmp server
        smtp.starttls()  # Thiết lập kết nối smtp trong chế độ TLS
        smtp.login(email_from, password)  # Đăng nhập vào tài khoản email sender
        smtp.send_message(em)  # Gửi mail
        print('Check your email ;)')


def cart_stats(cart):
    total_amount, total_quantity = 0, 0

    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_amount += c['quantity'] * c['price']

    return {
        'total_quantity': total_quantity,
        'total_amount': total_amount
    }


def set_tg_bay_toi_thieu(tgbay):
    if tgbay:
        return tgbay
