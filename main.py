import sys

from pprint import pprint
from yaml import load, FullLoader
from outmail import send_mail
from pathlib import Path
from outlooksender import get_maillist

def get_work_dir(work_dir_name=None):
    home_dir = Path.home()
    if work_dir_name is None:
        work_dir_name = Path('send_mail')
    work_dir = home_dir / work_dir_name
    if not work_dir.exists():
        Path.mkdir(work_dir)
    return work_dir


def run(config_name):
    work_dir = get_work_dir()
    default_suffix = 'cfg'
    send_mail_config_file_name = Path(config_name)
    if not send_mail_config_file_name.suffix == default_suffix:
        send_mail_config_file_name = Path('.'.join([str(send_mail_config_file_name.stem), default_suffix]))
    send_mail_config_file = work_dir / send_mail_config_file_name
    if not send_mail_config_file.exists():
        print(f"Конфига {send_mail_config_file_name} нет!!!\nСоздаем новый.")
        input()
        create_mail_config_file(file_path=send_mail_config_file)
    config = get_send_mail_cfg(send_mail_config_file)
    pprint(config)
    send_mail(*config)


def create_mail_config_file(file_path=None):
    default_cfg = 'e_addr: alan_gibizov@center.rt.ru;Anna.L.Sokolnikova@rt.ru\ngroup: test1\nsubject: Тестовое письмо\nbody_text: Текст тестового письма\nattach_path: None\nreport: None\n'
    if not file_path:
        file_path = Path.home() / Path('send_mail/send_mail.cfg')
    with open(file_path, 'w') as config_file:
        config_file.write(default_cfg)


def get_send_mail_cfg(send_mail_config_file):
    with open(send_mail_config_file, 'r') as send_mail_cfg:
        config = load(send_mail_cfg, Loader=FullLoader)
        try:
            e_addr = config['e_addr']
        except Exception('Нет адреса!'):
            pass
        if e_addr is None:
            e_addr = get_maillist(config['group'])
        subject = config['subject']
        body_text = config['body_text']
        attach_path = config['attach_path']
        report = config['report']
        data = (e_addr, subject, body_text, attach_path, report)
        return data


if __name__ == '__main__':
    try:
        config_name = sys.argv[1]
    except IndexError:
        config_name = 'test1.cfg'
    run(config_name=config_name)
