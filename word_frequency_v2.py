import re
import string

frequency = {}
document_text= open('garanti_irr_data.txt','r', encoding='utf-8')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{2,20}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])
