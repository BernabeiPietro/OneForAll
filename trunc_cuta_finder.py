import os
import codecs
import pandas as pd
import numpy as np

os.system("\
         7z e "+mp.seq_qzv+" -o"+mp.path_qiime+" quality-plot.html -r")
fv = +mp.path_qiime+"quality-plot.html"
oh=pd.read_html(fv)

def find_trunc (oh):

    c_f=(oh[0].values[1,1].split(" "))[0]
    c_r=(oh[1].values[1,1].split(" "))[0]
    return min(c_f,c_r) #trunc_cuta return
