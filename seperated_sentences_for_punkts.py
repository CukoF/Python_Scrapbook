from nltk import tokenize
fp = open("mcd_full_data_sikayetvar_katman.txt")
data = fp.read()
sep_data = tokenize.sent_tokenize(data)

for i in range(0, len(sep_data)):
    file = open("./mcd_full_data_sikayetvar_katman_seperated.txt", "a", encoding = "utf-8")
    translated_data = sep_data[i].replace("*","")
    file.write(translated_data + "\n")
    print(translated_data)
    file.close()