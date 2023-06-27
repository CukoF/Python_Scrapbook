import re

REMOVE_LIST = []
with open('stop_words.txt', encoding = 'utf-8') as fp:
    line = fp.readline()
    while line:
        word = line.strip()
        REMOVE_LIST.append(word)
        line = fp.readline()

remove = '|'.join(REMOVE_LIST)

with open('example_data.txt', encoding = 'utf-8') as fp:
    line = fp.readline()
    while line:
        words = line.strip().split(" ")
        line = ""
        for w in words:
            if w not in REMOVE_LIST:
                line = line + w + " "
        out = line.rstrip()
        out_non_space = re.sub(r'\s+', ' ', out)
        line = fp.readline()
        if not out_non_space.strip(): continue
        print(out_non_space)
