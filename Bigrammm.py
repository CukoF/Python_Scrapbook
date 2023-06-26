import nltk
import string

file = open("bigram_list_rel.txt", "w")
word_data = open('rel_cumlelerr.csv').read()

#for line in word_data:
    #line = line.strip()

nltk_tokens = nltk.word_tokenize(word_data)
file.write(str(list(nltk.bigrams(nltk_tokens))))

#print(list(nltk.bigrams(nltk_tokens)))

    

file.close()
