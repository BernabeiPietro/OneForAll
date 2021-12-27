import os
import pandas as pd


def extract_raw(mp,namezip):#aggiungi al main la funzione di input per il nome dello zip
    os.system("7z e "+mp.path_datainput+namezip+" -o"+mp.path_fastq_raw+ " *.raw_*.gz -r")
    os.system("7z e "+mp.path_datainput+namezip+" -o"+mp.path_base+ " SampleSeq_info.xls -r")

def rename(mp):
    os.system("rename -v 's/_2/_01_L001_R2_001/' "+mp.path_fastq_raw+"/*.gz")
    os.system("rename -v 's/_1/_01_L001_R1_001/' "+mp.path_fastq_raw+"/*.gz")
    os.system("rename -v 's/.fq/.fastq/' "+mp.path_fastq_raw+"*.gz")
    os.system("rename -v 's/.raw//' "+mp.path_fastq_raw+"*.gz" )

def take_barcode(mp,md):
    df = pd.read_excel(r''+mp.path_base+'/SampleSeq_info.xls')
    df["BarcodeSequence_lenght"]=df["BarcodeSequence"].map(len)
    if not is_unique(df["BarcodeSequence_lenght"]):
        print("Non sono tutti uguali")
    else:
        md["Barcode_length"] =df["BarcodeSequence_lenght"][0]

def is_unique(s):
    a = s.to_numpy() # s.values (pandas<0.24)
    return (a[0] == a).all()



df = pd.read_excel(r'/home/pietro/Desktop/temp/result_X204SC21103870-Z01-F001/00.RawData/SampleSeq_info.xls')
a=is_unique(df["BarcodeSequence"].map(len))
print(df)