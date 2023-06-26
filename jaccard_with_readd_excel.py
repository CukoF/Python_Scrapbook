import xlrd

def jaccard(first,second):
    c=0
    d=0
    for f in first:
        if f in second:
            c=c+1
    d=len(first)+len(second)
    return float(c)/float(d)

workbook = xlrd.open_workbook('Garanti_TestCase_v1-1_train_data_calculation_jaccard.xlsx', on_demand = True)
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
        score = jaccard(data[a]['Katman'], data[b]['Katman'])
        c1 = ' '.join(data[a]['Katman'])
        c2 = ' '.join(data[b]['Katman'])
        if (score > 0.30): print('%f | intent: %s --- %s --- %s | intent: %s --- %s --- %s' % (score, data[a]['Intent'], data[a]['Data'], c1, data[b]['Intent'], data[b]['Data'], c2))