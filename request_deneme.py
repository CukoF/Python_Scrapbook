import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

# Opening example files
file = open('German_words_part2.txt', encoding = 'utf-8')
# Reading each lines in the txt file
data = file.readlines()

# To create an empty list for url's
url = []
# To create a loop for converting datas each lines
for i in data:
    # Special Turkish characters
    d_alphabet = "çÇğĞıIşŞ"
    # Target characters for converting
    dalphabet = "cCgGiIsS"
    # Defining the translation between turkish characters and target characters
    ddata = str.maketrans(d_alphabet , dalphabet)
    # Converting the whole line and creating a url format
    urls = i.translate(ddata)
    # Appending the creating new urls
    url.append(urls)

# To set the pandas Series data type with new creating urls
data = pd.Series(url)
# To convert the Data Frame using Series and column named 'Text'
data = pd.DataFrame(data , columns = ['Text'])
# to set the url format - writing '_' sembol between each words in the line
dd = data['Text'].apply(lambda x : "_".join(x.lower() for x in x.split()))

# To set a list the url format
data = list(dd)

# Monitering or Logging the created url format
print(data)
# Openning the file for appending the request results
with open('translated_words_part2.txt' , 'a' , encoding = 'utf-8') as fl:
    # To set the for loop for each url format
    for urls in data:
        # Defining the whole url with created url format line
        site = 'https://de.pons.com/%C3%BCbersetzung/deutsch-t%C3%BCrkisch/' + urls
        # To request at translator website
        r = requests.get(site)
        # To set a soup variable with bs html parser
        soup = bs(r.content, 'html.parser')
        # Finding the translated worlds on the website with using html tags
        words = soup.find('div', id='results-tab-dict').find_all('dl')
        # Trying to catch the data
        try:
            # Monitoring the words which are catched
            print(words[0].find('div', 'target').get_text())
            # Writing words to the file which are catched
            fl.write(words[0].find('div', 'target').get_text())
        except:
            # Print the ERROR to the Log Screen
            print('ERROR!')
            # Write the ERROR message to the file
            fl.write('\nERROR!!')
            continue



