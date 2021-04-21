import unicodedata


def get_starting_jp_index(string) -> int:
    for i, c in enumerate(string):
        if is_japanese(c):
            return i
    return len(string) - 1


def is_japanese(c):
    name = unicodedata.name(c)
    if "CJK UNIFIED" in name or "HIRAGANA" in name or "KATAKANA" in name:
        return True
    return False


def delete_comma(string) -> str:
    return string.replace(',', '')


def delete_space(string) -> str:
    return string.replace(' ', '')


def reformat_record(string) -> str:
    print(f'in: {string}')
    first_jp_index = get_starting_jp_index(string)
    others, jp = string[:first_jp_index], string[first_jp_index:]
    others = delete_comma(others)
    print(others + ',' + jp)
    return others + ',' + jp


def reformat_file(file_path):
    lines = []
    for_write_lines = []
    with open(file_path, 'r') as f:
        lines = f.read().split('\n')
        print(lines)
    for line in lines:
        if line:
            for_write_lines.append(reformat_record(line))
    for_write_str = '\r'.join(for_write_lines)
    with open(file_path, 'w') as f:
        f.write(for_write_str)


if __name__ == '__main__':
    reformat_file('memorable_word/gogen_answer.txt')
    reformat_record('gre(ss), grad 行く、進む')
