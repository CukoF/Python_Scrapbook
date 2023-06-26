import xlrd
import collections
import numpy as np

def jaccard(first,second):
    c=0
    d=0
    for f in first:
        if f in second:
            c=c+1
    d=len(first)+len(second)
    return float(c)/float(d)

workbook = xlrd.open_workbook('utterances.xlsx', on_demand = True)
worksheet = workbook.sheet_by_index(0)
first_row = [] #: The row where we stock the name of the column
for col in range(worksheet.ncols):
    first_row.append( worksheet.cell_value(0,col) )
#: transform the workbook to a list of dictionaries
data_none_split =[]
data_split = []
intent_ids = []
for row in range(1, worksheet.nrows):
    elm = {}
    elm_split = {}
    for col in range(worksheet.ncols):
        elm[first_row[col]]=worksheet.cell_value(row,col)
        elm_split[first_row[col]]=worksheet.cell_value(row,col)
    elm_split[first_row[3]]=str(elm[first_row[3]]).split(' ')
    intent_ids.append(elm[first_row[0]])
    data_none_split.append(elm)
    data_split.append(elm_split)


#: Sentence freq in a ExcelSheet
sentence_freq={}
for i in range( len(data_none_split) - 1 ):
    if data_none_split[i]['utterance_katman_text'] not in sentence_freq:
        sentence_freq[data_none_split[i]['utterance_katman_text']] = 1
    else:
        sentence_freq[data_none_split[i]['utterance_katman_text']] += 1

#: Word freq in a ExcelSheet (unique)
word_freq = {}
for i in range( len(data_split) - 1 ):
    for word in data_split[i]['utterance_katman_text']:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

#: Class freq in a ExcelSheet (unique)
counter = collections.Counter(intent_ids)

#: Avg word size in a class
cnt = 0
for i in range( len(data_split) - 1 ):
    cnt = cnt + len(data_split[i]['utterance_katman_text'])

#: Find duplicates 
duplicates={}
for w in sentence_freq:
    if sentence_freq[w] > 1:
        duplicates[w]= sentence_freq[w]

#: print out kismi(yuk olmamasi icin su an commented)
'''
for i in range ( len(data_none_split) - 1 ):
    if data_none_split[i]['utterance_katman_text'] in duplicates:
        print('katman: %s --- id: %d --- original: %s' % (data_none_split[i]['utterance_katman_text'], data_none_split[i]['intent_id'], data_none_split[i]['utterance_text']))
'''

print('Size: ', len(data_none_split) )
print('Vocabulary(unique): ', len(word_freq))
print('Classes(unique): ', len(counter.keys()))
print('Avg word size in a class: ', int(np.mean(list(counter.values()))))
print('Avg word count: ', int(cnt/len(data_none_split)))