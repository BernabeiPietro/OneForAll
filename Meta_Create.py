import os
import pandas as pd

def metadata(mp):
    os.system("\
             7z e "+mp.seq_qzv+" -o"+mp.path_qiime+" per-sample-fastq-counts.tsv -r")
    fv = +mp.path_qiime+"per-sample-fastq-counts.tsv"
    df=pd.read_csv(fv,sep='\t')
    df["sample ID"].to_csv(r''+mp.path_qiime+'/Metadata.tsv', header=None, index=None, sep='\t', mode='a')
    print("ATTENZIONE FATTO METADATA")
    input("VUOI PROSEGUIRE?");
    input("SICURO?");
    input("SICURO SICURO?");
