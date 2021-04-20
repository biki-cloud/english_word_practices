import json
from typing import *
import random

from ReadWordTxt import WordFile


class DetailFile:
    def __init__(self, word_file):
        self.wf = WordFile(word_file)
        self.detailed_file_path = f'{word_file}_detailed.txt'
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
        with open(self.detailed_file_path, 'w') as f:
            json.dump(self.detailed_list, f, indent=4, ensure_ascii=False)

    def read_from_detailed_file(self) -> List[Dict[str, str]]:
        with open(self.detailed_file_path, 'r') as f:
            return json.load(f)

    def get_random_element(self, num):
        detailed_list = self.read_from_detailed_file()
        return random.sample(detailed_list, num)


if __name__ == '__main__':
    df = DetailFile('./memorable_word/ielts3500.txt')
    print(df.get_random_element(3))
