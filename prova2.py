import os
import codecs
import pandas as pd
import numpy as np
import os


def parser_table(file):
    string_to_parse=file.read()
    string_to_parse=string_to_parse[string_to_parse.find(">>Per base sequence quality"):]
    string_to_parse=string_to_parse[string_to_parse.find("#"):string_to_parse.find(">>END_MODULE")-1:]
    column=(string_to_parse[:(value:=string_to_parse.find('\n'))]).split('\t')
    string_to_parse=string_to_parse[value+1:]
    table=pd.DataFrame([x.split('\t') for x in string_to_parse.split('\n')],columns=column)
    for col in table.columns:
        table[col]=table[col].astype('float')
    return table




def median_table(table):
    min=len(table[0])
    max=len(table[0])
    for x in table:
        if min>len(x):
            min=len(x)
        else:
            max=len(x)
    value = np.zeros(max)
    for x in table:
            value = value + x["Median"]
    result=value/len(table)
    return result
def count_equals(median):
    first = median[0]
    i = 0
    for x in median:
        if x == first:
            i = i + 1
        else:
            return i
path=r"D:\prova\file_txt"
dir_element = filter(lambda x: (".txt" in x), os.listdir(path))
result=[]
for name_of_file in dir_element:
    result.append(parser_table(open(path +"\\"+ name_of_file,"r")))
value=count_equals(median_table(result))
print(value)
