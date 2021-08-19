import os
import codecs
import pandas as pd
import numpy as np

fv ="D:\seq_sperim_M_microF\c-41a6-b314-f0c2888109f9\data\quality-plot.html"
oh=pd.read_html(fv)

def find_trunc (fv):

    t_f=(oh[0].values[1,1].split(" "))[0]
    t_r=(oh[1].values[1,1].split(" "))[0]
    return min(t_f,t_r) #trunc return
