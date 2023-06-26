import nltk
import string
# Open txt file
file = open("bigram_list_rel.txt", "w")
# Reaing words from csv file
word_data = open('words.csv').read()

# Create a token from nltk 
nltk_tokens = nltk.word_tokenize(word_data)
# Write the created nltk tokens to the file
file.write(str(list(nltk.bigrams(nltk_tokens))))



    
# Close the file
file.close()
