with open ('foo.txt', encoding='utf-8') as f:
    for one_line in f.readlines():
        print(one_line, end='')
    
f.close()

