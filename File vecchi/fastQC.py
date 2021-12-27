import os
import codecs
import pandas as pd
import numpy as np



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



def run_fastqc(md,mp):
    os.system("fastqc -o "+mp.path_fastqc+" -t "+md["tread"]+" "+mp.path_datainput+"*.fastq.gz --nogroup --noextract \
    && \
    7z e "+mp.path_fastqc+" -o"+mp.path_fqc_txt+" fastqc_data.txt -aou -tzip -r")
    dir_element = filter(lambda x: (".txt" in x), os.listdir(mp.path_fqc_txt))
    result = []
    for name_of_file in dir_element:
        result.append(parser_table(open(mp.path_fqc_txt + name_of_file, "r")))
    value = count_equals(median_table(result))
    return value# estrae i file e li rinomina automaticamente ora vanno mediati i risultati.

#questo sputa fuori un numero che deve essere nella varaibile: "primer_lenght" e buttata in QIIME2 e Figaro