import os
import codecs
import pandas as pd
import numpy as np

os.system("\
         7z e "+mp.seq_qzv+" -o"+mp.path_qiime+" overview.html -r")
fv = +mp.path_qiime+"overview.html"
oh=pd.read_html(fv)
dim_min_sample = oh[0].values[0,1]

