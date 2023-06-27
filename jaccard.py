import xlrd

def jaccard(first,second):
    c=0
    d=0
    for f in first:
        if f in second:
            c=c+1
    d=len(first)+len(second)
    return float(c)/float(d)

workbook = xlrd.open_workbook('example_file.xlsx', on_demand = True)
worksheet = workbook.sheet_by_index(0)
first_row = [] #: The row where we stock the name of the column
for col in range(worksheet.ncols):
    first_row.append( worksheet.cell_value(0,col) )
#: transform the workbook to a list of dictionaries
data =[]
text = []
for row in range(1, worksheet.nrows):
    elm = {}
    for col in range(worksheet.ncols):
        elm[first_row[col]]=worksheet.cell_value(row,col)
    elm[first_row[3]]=str(elm[first_row[3]]).split(' ')
    data.append(elm)

#: search and print jaccard dist
for a in range( len(data) - 1 ):
    for b in range( a+1,  len(data) - a ):
        score = jaccard(data[a]['nlp_layer_text'], data[b]['nlp_layer_text'])
        c1 = ' '.join(data[a]['nlp_layer_text'])
        c2 = ' '.join(data[b]['nlp_layer_text'])
        if score > 0.4: print('%d | id: %s --- %s --- %s | id: %s --- %s --- %s' % (score, data[a]['intent_id'], data[a]['nlp_layer'], c1, data[b]['intent_id'], data[b]['nlp_layer'], c2))
