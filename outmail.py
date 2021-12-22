import os
import time

import win32com
import win32com.client as win32
from pathlib import Path


def send_mail(e_addr, subject=None, body_text=None, attach_path=None, report=None):
    """

    :param e_addr: "aa@bb.cc; dd@ee.ff"
    :param attach_path: "c:\\my_dir\\my_file.aaa" (not necessary)
    :param subject: "My subject"
    :param body_text: "My body text"
    :return:
    """
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = e_addr
    if not subject:
        subject = attach_path
    mail.Subject = subject
    if not body_text:
        body_text = ''
    mail.Body = body_text
    #mail.HTMLBody = f'<h2>{body_text}</h2>' #this field is optional

    # To attach a file to the email (optional):
    if bool(attach_path):
        if isinstance(attach_path, list):
            for attach in attach_path:
                mail.Attachments.Add(str(attach))
        elif isinstance(attach_path, Path):
            mail.Attachments.Add(str(attach_path))
    mail.Send()
    if report:
        print('The mail has been sent')

def check_mail():
    ol = win32com.client.Dispatch("Outlook.Application")
    inbox = ol.GetNamespace("MAPI").GetDefaultFolder(6)
    result = []
    for message in inbox.Items:
        if message.UnRead == True:
            result.append(message.Subject)  # or whatever command you want to do
            message.Delete()
    return bool(result)

def run_checking_mail(func):
    while True:
        mails = check_mail()
        if bool(mails):
            func()
        time.sleep(5)

if __name__ == '__main__':
    e_address = 'alan_gibizov@center.rt.ru; phaggi@gmail.com'
    subj = 'subject'
    testpath = Path.cwd() / Path('testdir')
    attach_path = [str(testpath / Path(file)) for file in os.listdir(testpath) if 'csv' in file]
    send_mail(e_addr=e_address,
              attach_path=attach_path,
              subject=subj,
              body_text='test')
