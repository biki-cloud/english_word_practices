import json
import os
import random
from typing import *

from ReadWordTxt import WordFile


def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def dict_to_json(dic):
    return json.dumps(dic, ensure_ascii=False, indent=4)


def json_to_dict(json_str):
    return json.loads(json_str)


class DetailFile:
    def __init__(self, word_file):
        self.wf = WordFile(word_file)
        self.detailed_file_path = os.path.join(os.getcwd(), 'details', os.path.basename(word_file))
        self.detailed_list = self.get_detailed_list()
        self.write_to_detailed_file()

    def get_detailed_list(self) -> List[Dict[str, str]]:
        detailed_list = []
        for en, jp in self.wf.en_jp_generator():
            dic = {
                'en': en,
                'jp': jp,
                'collect_num': 0,
                'info': ''
            }
            detailed_list.append(dic)
        return detailed_list

    def write_to_detailed_file(self):
        return write_json(self.detailed_file_path, self.detailed_list)

    def read_from_detailed_file(self) -> List[Dict[str, str]]:
        return read_json(self.detailed_file_path)

    def get_random_element(self, num):
        detailed_list = self.read_from_detailed_file()
        return random.sample(detailed_list, num)

    def add_collect_number(self, en):
        detailed_list = self.read_from_detailed_file()
        for dic in detailed_list:
            if en == dic['en']:
                now_num = dic['collect_num']
                dic['collect_num'] = str(int(now_num) + 1)
        write_json(self.detailed_file_path, detailed_list)


if __name__ == '__main__':
    df = DetailFile('./memorable_word/ielts3500.txt')
    print(df.get_random_element(3))
