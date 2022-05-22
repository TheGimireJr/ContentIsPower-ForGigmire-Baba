from random import randint
import smtplib


def send_mail(DB, subject, body):
    # Quarrying the mail and pass
    all = []
    for dictionary in DB.find():
        all.append(dictionary)
    len_all = len(all)
    index = randint(0, len_all - 1)
    mailDict = all[index]

    mail = mailDict['mail']
    password = mailDict['pass']


    # Sending mail
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(mail, password)


        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(mail, 'Naitik.123.coc@gmail.com', msg)
