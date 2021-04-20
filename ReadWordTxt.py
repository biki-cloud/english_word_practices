import os
from typing import *


class MyFileNotFoundError(Exception):
    pass


en = NewType('english', str)
jp = NewType('japanese', str)


def lang_separator(txt) -> (en, jp):
    separator_index = txt.index(',')
    return txt[:separator_index], txt[separator_index + 1:]


class WordFile:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            MyFileNotFoundError(f'{file_path} is not found')
        self.file_path = file_path
        self.content_lines = []

    def en_jp_generator(self) -> tuple[str, str]:
        with open(self.file_path, 'r') as f:
            for line in f.read().split('\n'):
                if line:
                    english, japanese = lang_separator(line)
                    yield english, japanese


if __name__ == '__main__':
    wf = WordFile('./memorable_word/ielts3500.txt')
    print(wf.file_path)
    for i in wf.en_jp_generator():
        print('ffff')
        print(i)
