import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import tqdm
import os

class sendEmail:
    def __init__(self, subject, message, filename):
        self.subject = subject
        self.filename = filename
        self.message = message
        self.sender_email = 'dhunt10@gmail.com'
        self.password = '**********'
        self.p = MIMEBase('application', 'octet-stream')
        self.filename = self.filename
        self.attachment = open(filename, "rb")
        self.p.set_payload((self.attachment).read())
        encoders.encode_base64(self.p)
        self.p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        self.s = smtplib.SMTP('smtp.gmail.com', 587)
        self.s.starttls()
        self.s.login(self.sender_email, self.password)

    def prepare_email(self, data):
        """

        :param data:
        :return:
        """
        for i in range(len(data)):
            print(data)
            self.sendEmail(data['name'][i], data['email'][i])
            print('{}/{} Sent'.format(i, len(data)))
            print('Email has been sent to {} at {}'.format(data['name'][i], data['email'][i]))
        self.s.quit()

    def sendEmail(self, name, email):
        msg = MIMEMultipart()
        message = self.message.format(name) + '\n\n'
        msg['From'] = self.sender_email
        msg['To'] = email
        msg['Subject'] = self.subject
        msg.attach(MIMEText(message, 'plain'))
        msg.attach(self.p)
        text = msg.as_string()
        self.s.sendmail(self.sender_email, email, text)


