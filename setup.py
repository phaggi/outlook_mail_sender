import shutil
from pathlib import Path
from fileman import get_datetime


def prep_copy_message(version, distr_name, dst):
    return f'\n{version} version "{distr_name}" have been copied to {dst}.'


if __name__ == '__main__':
    ignoredirs = ['.git',
                  '__pycache__',
                  'arch',
                  'redmine',
                  'testdir',
                  'secret',
                  'venv',
                  '.gitignore',
                  '.idea']
    distr_name = 'mail_sender'

    version = 'Old'
    src = Path.home() / Path(distr_name)
    dst = Path.home() / Path('_'.join([distr_name, 'archive'])) / Path('_'.join([distr_name, get_datetime(rev=True)]))
    message = f'{version} version "{distr_name}" have been copied to {dst}.'
    if src.exists():
        shutil.copytree(src, dst)
        print(prep_copy_message(version, distr_name, dst))

    version = 'New'
    src = Path.cwd()
    dst = Path.home() / Path(distr_name)
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(str(src), str(dst), ignore=shutil.ignore_patterns(*ignoredirs))
    print(prep_copy_message(version, distr_name, dst))
