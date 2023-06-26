import pandas as pd
import numpy as np
import itertools as it
import xlsxwriter

#file open
file = open('file_name.txt' , encoding = 'utf-8' )
#file read
data = file.readlines()

#sentences is split in word
def trans(data1):
	liste = []
	for i in data1:
		raw = i.split()
		liste.append( raw )
	#transpose the word list
	liste = list( map( str, it.chain.from_iterable( liste ) ) )
	return liste

liste1 = trans(data)

def replace_char(mlist):
	vowels = 'aeıioöuüAEIİOÖUÜ'
	sibilancy = 'bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ'
	newlist = []
	for word in mlist:
		for char in word:
			#if char in vowels replaced 'E'
			if char in vowels:
				word = word.replace(char,'E')
			#if char in sibilancy replaced 'Z'
			elif char in sibilancy:
				word = word.replace(char,'Z')
			#if char not in sibilancy and vowels stay same char
			else:
				word = word
		newlist.append(word)
	#write the replace char on dataframe
	newlist = pd.DataFrame({ 'Replaced_chars' : newlist })
	#char datafame on dublicates
	newlist = newlist.drop_duplicates( subset = 'Replaced_chars' )
	
	return newlist

ch = replace_char(liste1)

#write to dataframe in file
writer = pd.ExcelWriter( 'replace_chars.xlsx' , engine = 'xlsxwriter' )
ch.to_excel( writer , sheet_name = 'Sheet1' , index = False )
writer.save()