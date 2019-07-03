import nltk
nltk.download('punkt')
import sys
import codecs
import re
import xlrd
xls=xlrd.open_workbook("news_data.xlsx")


# sheetcount = 0
for sheet in xls.sheets():
    header=""
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols
    sheetname = sheet.name
    mylist = []
    text = ""
    for row in range(1, number_of_rows):  
            text += sheet.cell_value(row, 0) + " " + sheet.cell_value(row, 1) + " "
     
    # tokenize the string
    tokens = nltk.word_tokenize(text)

    # remove all unnessary chars
    # get only sinhala unicode charactors
    regex = re.compile(u'[^\u0D80-\u0DFF]', re.UNICODE)
    tokens = [regex.sub('', w) for w in tokens]
    tokens = filter(None, tokens)

    tokens = list(set(tokens)) #this will remove duplicates
    tokens = sorted(tokens)

    # open file to save output
    f = codecs.open("bag_of_words.txt","w+", encoding='utf-8')

    # save term frequencies
    for c in tokens:
            f.write(c + "\n")

    # close file
    f.close() 
