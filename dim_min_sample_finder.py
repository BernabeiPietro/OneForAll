import os
import codecs
import pandas as pd
import numpy as np

def dim_min_sample(mp,md):
    os.system("7z e "+ mp.path_qiime + "/ASV-" + mp.project_name + ".qzv"+" -o"+mp.path_qiime+" overview.html -r")
    fv = +mp.path_qiime+"overview.html"
    oh=pd.read_html(fv)
    return oh[0].values[0,1]
