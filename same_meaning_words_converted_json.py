import json

#Split the words 
words = []
with open("deneme.txt", encoding='utf-8') as f:
	line = f.readline()
	while line:
		word = line.strip().split(',')
		words.append(word)
		line = f.readline()

kelimeler = {}
for i in words:
	kelimeler[i[0]] = i[1::]


with open('data.json', 'w', encoding = 'utf-8') as f:
	json.dump(kelimeler,f, ensure_ascii= False)